import sys
import re
from typing import List
from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime


class FilterValue:
    def __init__(self,
                 value: str = "Q0000"
                ) -> None:
        self.value = value

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _FilterValue = other
        result1 = True
        if not (self.value == "?DNC?" or _FilterValue.value == "?DNC?"):
            if not _FilterValue.value == self.value:
                result1 = False
        return result1


    def __str__(self) -> str:
        return "{FilterValue} {" + \
         " value = " + str(self.value) + " "  "} " + "\n"

    def to_json(self) -> str:
        return "{" + \
            '"value": "' + str(self.value) + '"' +  \
            "}"

    @staticmethod
    def from_json(json: str):
        instance = FilterValue()
        json = re.sub(r"\s+", "", json) 
        json = json.replace("{","").replace("}","") 
        key_value_pairs = json.split(",")
        for pair in key_value_pairs:
            entry = pair.split(":")
            key = entry[0].replace('\"', "").strip()
            value = entry[1].replace('\"', "").strip()
            switch = {
                   "value": lambda: setattr(instance, "value", value),

                }
            switch.get(key, lambda: print(f"Invalid JSON element {key}", file=sys.stderr))()
        return instance
        

    @staticmethod
    def list_to_json(list: List["FilterValue"]) -> str:
        json_builder = []
        json_builder.append("[")
        for i in range(len(list)):
            json_builder.append(list[i].to_json())
            if i < len(list) - 1:
                json_builder.append(",")
        json_builder.append("]")
        return "".join(json_builder)
        

    @staticmethod
    def list_from_json(json: str) -> List["FilterValue"]:
        result_list = []
        json = re.sub(r"\s+", "", json) 
        json = json.replace("[", "").replace("]", "")
        json_objects = re.split(r"(?<=}),\s*(?={)", json)
        for json_object in json_objects:
            result_list.append(FilterValue.from_json(json_object))
        return result_list
    

    def to_FilterValueInternal(self): 
        from tests.gherkinexecutor.Feature_Full_Test.FilterValueInternal import FilterValueInternal
        return FilterValueInternal(
            ID(self.value)
        )

    class Builder:
        def __init__(self) -> None:
            self.value = "Q0000"

        def setValue(self, value: str) -> 'Builder':
            self.value = value
            return self

        def set_compare(self) -> 'Builder':
            self.value = "?DNC?"
            return self

        def build(self):
            return FilterValue(
                self.value
            )
