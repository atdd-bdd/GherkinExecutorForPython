import sys
import re
from typing import List
from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime


class ValueValid:
    def __init__(self,
                 value: str = "0"
                , valid: str = "false"
                , notes: str = ""
                ) -> None:
        self.value = value
        self.valid = valid
        self.notes = notes

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _ValueValid = other
        result1 = True
        if not (self.value == "?DNC?" or _ValueValid.value == "?DNC?"):
            if not _ValueValid.value == self.value:
                result1 = False
        if not (self.valid == "?DNC?" or _ValueValid.valid == "?DNC?"):
            if not _ValueValid.valid == self.valid:
                result1 = False
        if not (self.notes == "?DNC?" or _ValueValid.notes == "?DNC?"):
            if not _ValueValid.notes == self.notes:
                result1 = False
        return result1


    def __str__(self) -> str:
        return "{ValueValid} {" + \
         " value = " + str(self.value) + " "  " valid = " + str(self.valid) + " "  " notes = " + str(self.notes) + " "  "} " + "\n"

    def to_json(self) -> str:
        return "{" + \
            '"value": "' + str(self.value) + '"' +  \
            "," + '"valid": "' + str(self.valid) + '"' +  \
            "," + '"notes": "' + str(self.notes) + '"' +  \
            "}"

    @staticmethod
    def from_json(json: str):
        instance = ValueValid()
        json = re.sub(r"\s+", "", json) 
        json = json.replace("{","").replace("}","") 
        key_value_pairs = json.split(",")
        for pair in key_value_pairs:
            entry = pair.split(":")
            key = entry[0].replace('\"', "").strip()
            value = entry[1].replace('\"', "").strip()
            switch = {
                   "value": lambda: setattr(instance, "value", value),
                "valid": lambda: setattr(instance, "valid", value),
                "notes": lambda: setattr(instance, "notes", value),

                }
            switch.get(key, lambda: print(f"Invalid JSON element {key}", file=sys.stderr))()
        return instance
        

    @staticmethod
    def list_to_json(list: List["ValueValid"]) -> str:
        json_builder = []
        json_builder.append("[")
        for i in range(len(list)):
            json_builder.append(list[i].to_json())
            if i < len(list) - 1:
                json_builder.append(",")
        json_builder.append("]")
        return "".join(json_builder)
        

    @staticmethod
    def list_from_json(json: str) -> List["ValueValid"]:
        result_list = []
        json = re.sub(r"\s+", "", json) 
        json = json.replace("[", "").replace("]", "")
        json_objects = re.split(r"(?<=}),\s*(?={)", json)
        for json_object in json_objects:
            result_list.append(ValueValid.from_json(json_object))
        return result_list
    

    def to_ValueValidInternal(self): 
        from tests.gherkinexecutor.Feature_Full_Test.ValueValidInternal import ValueValidInternal
        return ValueValidInternal(
            self.value
            ,bool(self.valid)
            ,self.notes
        )

    class Builder:
        def __init__(self) -> None:
            self.value = "0"
            self.valid = "false"
            self.notes = ""

        def setValue(self, value: str) -> 'Builder':
            self.value = value
            return self

        def setValid(self, valid: str) -> 'Builder':
            self.valid = valid
            return self

        def setNotes(self, notes: str) -> 'Builder':
            self.notes = notes
            return self

        def set_compare(self) -> 'Builder':
            self.value = "?DNC?"
            self.valid = "?DNC?"
            self.notes = "?DNC?"
            return self

        def build(self):
            return ValueValid(
                self.value
                ,self.valid
                ,self.notes
            )
