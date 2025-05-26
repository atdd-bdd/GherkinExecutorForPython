import sys
import re
from typing import List
from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime
class ExampleClass:
    def __init__(self,
                 fieldA: str = "y"
                , fieldB: str = "x"
                ) -> None:
        self.fieldA = fieldA
        self.fieldB = fieldB

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _ExampleClass = other
        result1 = True
        if not (self.fieldA == "?DNC?" or _ExampleClass.fieldA == "?DNC?"):
            if not _ExampleClass.fieldA == self.fieldA:
                result1 = False
        if not (self.fieldB == "?DNC?" or _ExampleClass.fieldB == "?DNC?"):
            if not _ExampleClass.fieldB == self.fieldB:
                result1 = False
        return result1


    def __str__(self) -> str:
        return "{ExampleClass} {" + \
         " fieldA = " + str(self.fieldA) + " "  " fieldB = " + str(self.fieldB) + " "  "} " + "\n"

    def to_json(self) -> str:
        return "{" + \
            '"fieldA": "' + str(self.fieldA) + '"' +  \
            "," + '"fieldB": "' + str(self.fieldB) + '"' +  \
            "}"

    @staticmethod
    def from_json(json: str):
        instance = ExampleClass()
        json = re.sub(r"\s+", "", json) 
        json = json.replace("{","").replace("}","") 
        key_value_pairs = json.split(",")
        for pair in key_value_pairs:
            entry = pair.split(":")
            key = entry[0].replace('\"', "").strip()
            value = entry[1].replace('\"', "").strip()
            switch = {
                   "fieldA": lambda: setattr(instance, "fieldA", value),
                "fieldB": lambda: setattr(instance, "fieldB", value),

                }
            switch.get(key, lambda: print(f"Invalid JSON element {key}", file=sys.stderr))()
        return instance
        

    @staticmethod
    def list_to_json(list: List["ExampleClass"]) -> str:
        json_builder = []
        json_builder.append("[")
        for i in range(len(list)):
            json_builder.append(list[i].to_json())
            if i < len(list) - 1:
                json_builder.append(",")
        json_builder.append("]")
        return "".join(json_builder)
        

    @staticmethod
    def list_from_json(json: str) -> List["ExampleClass"]:
        result_list = []
        json = re.sub(r"\s+", "", json) 
        json = json.replace("[", "").replace("]", "")
        json_objects = re.split(r"(?<=}),\s*(?={)", json)
        for json_object in json_objects:
            result_list.append(ExampleClass.from_json(json_object))
        return result_list
    

    class Builder:
        def __init__(self) -> None:
            self.fieldA = "y"
            self.fieldB = "x"

        def setFielda(self, fieldA: str) -> 'Builder':
            self.fieldA = fieldA
            return self

        def setFieldb(self, fieldB: str) -> 'Builder':
            self.fieldB = fieldB
            return self

        def set_compare(self) -> 'Builder':
            self.fieldA = "?DNC?"
            self.fieldB = "?DNC?"
            return self

        def build(self):
            return ExampleClass(
                self.fieldA
                ,self.fieldB
            )
