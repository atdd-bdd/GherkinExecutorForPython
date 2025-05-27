import sys
import re
from typing import List
from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime


class CSVContents:
    def __init__(self,
                 a: str = ""
                , b: str = ""
                , c: str = ""
                ) -> None:
        self.a = a
        self.b = b
        self.c = c

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _CSVContents = other
        result1 = True
        if not (self.a == "?DNC?" or _CSVContents.a == "?DNC?"):
            if not _CSVContents.a == self.a:
                result1 = False
        if not (self.b == "?DNC?" or _CSVContents.b == "?DNC?"):
            if not _CSVContents.b == self.b:
                result1 = False
        if not (self.c == "?DNC?" or _CSVContents.c == "?DNC?"):
            if not _CSVContents.c == self.c:
                result1 = False
        return result1


    def __str__(self) -> str:
        return "{CSVContents} {" + \
         " a = " + str(self.a) + " "  " b = " + str(self.b) + " "  " c = " + str(self.c) + " "  "} " + "\n"

    def to_json(self) -> str:
        return "{" + \
            '"a": "' + str(self.a) + '"' +  \
            "," + '"b": "' + str(self.b) + '"' +  \
            "," + '"c": "' + str(self.c) + '"' +  \
            "}"

    @staticmethod
    def from_json(json: str):
        instance = CSVContents()
        json = re.sub(r"\s+", "", json) 
        json = json.replace("{","").replace("}","") 
        key_value_pairs = json.split(",")
        for pair in key_value_pairs:
            entry = pair.split(":")
            key = entry[0].replace('\"', "").strip()
            value = entry[1].replace('\"', "").strip()
            switch = {
                   "a": lambda: setattr(instance, "a", value),
                "b": lambda: setattr(instance, "b", value),
                "c": lambda: setattr(instance, "c", value),

                }
            switch.get(key, lambda: print(f"Invalid JSON element {key}", file=sys.stderr))()
        return instance
        

    @staticmethod
    def list_to_json(list: List["CSVContents"]) -> str:
        json_builder = []
        json_builder.append("[")
        for i in range(len(list)):
            json_builder.append(list[i].to_json())
            if i < len(list) - 1:
                json_builder.append(",")
        json_builder.append("]")
        return "".join(json_builder)
        

    @staticmethod
    def list_from_json(json: str) -> List["CSVContents"]:
        result_list = []
        json = re.sub(r"\s+", "", json) 
        json = json.replace("[", "").replace("]", "")
        json_objects = re.split(r"(?<=}),\s*(?={)", json)
        for json_object in json_objects:
            result_list.append(CSVContents.from_json(json_object))
        return result_list
    

    class Builder:
        def __init__(self) -> None:
            self.a = ""
            self.b = ""
            self.c = ""

        def setA(self, a: str) -> 'Builder':
            self.a = a
            return self

        def setB(self, b: str) -> 'Builder':
            self.b = b
            return self

        def setC(self, c: str) -> 'Builder':
            self.c = c
            return self

        def set_compare(self) -> 'Builder':
            self.a = "?DNC?"
            self.b = "?DNC?"
            self.c = "?DNC?"
            return self

        def build(self):
            return CSVContents(
                self.a
                ,self.b
                ,self.c
            )
