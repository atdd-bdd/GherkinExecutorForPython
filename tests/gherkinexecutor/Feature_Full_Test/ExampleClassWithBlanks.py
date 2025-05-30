import sys
import re
from typing import List
from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime


class ExampleClassWithBlanks:
    def __init__(self,
                 field_1: str = " "
                , field_2: str = " "
                ) -> None:
        self.field_1 = field_1
        self.field_2 = field_2

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _ExampleClassWithBlanks = other
        result1 = True
        if not (self.field_1 == "?DNC?" or _ExampleClassWithBlanks.field_1 == "?DNC?"):
            if not _ExampleClassWithBlanks.field_1 == self.field_1:
                result1 = False
        if not (self.field_2 == "?DNC?" or _ExampleClassWithBlanks.field_2 == "?DNC?"):
            if not _ExampleClassWithBlanks.field_2 == self.field_2:
                result1 = False
        return result1


    def __str__(self) -> str:
        return "{ExampleClassWithBlanks} {" + \
         " field_1 = " + str(self.field_1) + " "  " field_2 = " + str(self.field_2) + " "  "} " + "\n"

    def to_json(self) -> str:
        return "{" + \
            '"field_1": "' + str(self.field_1) + '"' +  \
            "," + '"field_2": "' + str(self.field_2) + '"' +  \
            "}"

    @staticmethod
    def from_json(json: str):
        instance = ExampleClassWithBlanks()
        json = re.sub(r"\s+", "", json) 
        json = json.replace("{","").replace("}","") 
        key_value_pairs = json.split(",")
        for pair in key_value_pairs:
            entry = pair.split(":")
            key = entry[0].replace('\"', "").strip()
            value = entry[1].replace('\"', "").strip()
            switch = {
                   "field_1": lambda: setattr(instance, "field_1", value),
                "field_2": lambda: setattr(instance, "field_2", value),

                }
            switch.get(key, lambda: print(f"Invalid JSON element {key}", file=sys.stderr))()
        return instance
        

    @staticmethod
    def list_to_json(list: List["ExampleClassWithBlanks"]) -> str:
        json_builder = []
        json_builder.append("[")
        for i in range(len(list)):
            json_builder.append(list[i].to_json())
            if i < len(list) - 1:
                json_builder.append(",")
        json_builder.append("]")
        return "".join(json_builder)
        

    @staticmethod
    def list_from_json(json: str) -> List["ExampleClassWithBlanks"]:
        result_list = []
        json = re.sub(r"\s+", "", json) 
        json = json.replace("[", "").replace("]", "")
        json_objects = re.split(r"(?<=}),\s*(?={)", json)
        for json_object in json_objects:
            result_list.append(ExampleClassWithBlanks.from_json(json_object))
        return result_list
    

    class Builder:
        def __init__(self) -> None:
            self.field_1 = " "
            self.field_2 = " "

        def setField_1(self, field_1: str) -> 'Builder':
            self.field_1 = field_1
            return self

        def setField_2(self, field_2: str) -> 'Builder':
            self.field_2 = field_2
            return self

        def set_compare(self) -> 'Builder':
            self.field_1 = "?DNC?"
            self.field_2 = "?DNC?"
            return self

        def build(self):
            return ExampleClassWithBlanks(
                self.field_1
                ,self.field_2
            )
