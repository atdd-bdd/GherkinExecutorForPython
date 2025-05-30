import sys
import re
from typing import List
from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime


class ResultValue:
    def __init__(self,
                 sum: str = ""
                ) -> None:
        self.sum = sum

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _ResultValue = other
        result1 = True
        if not (self.sum == "?DNC?" or _ResultValue.sum == "?DNC?"):
            if not _ResultValue.sum == self.sum:
                result1 = False
        return result1


    def __str__(self) -> str:
        return "{ResultValue} {" + \
         " sum = " + str(self.sum) + " "  "} " + "\n"

    def to_json(self) -> str:
        return "{" + \
            '"sum": "' + str(self.sum) + '"' +  \
            "}"

    @staticmethod
    def from_json(json: str):
        instance = ResultValue()
        json = re.sub(r"\s+", "", json) 
        json = json.replace("{","").replace("}","") 
        key_value_pairs = json.split(",")
        for pair in key_value_pairs:
            entry = pair.split(":")
            key = entry[0].replace('\"', "").strip()
            value = entry[1].replace('\"', "").strip()
            switch = {
                   "sum": lambda: setattr(instance, "sum", value),

                }
            switch.get(key, lambda: print(f"Invalid JSON element {key}", file=sys.stderr))()
        return instance
        

    @staticmethod
    def list_to_json(list: List["ResultValue"]) -> str:
        json_builder = []
        json_builder.append("[")
        for i in range(len(list)):
            json_builder.append(list[i].to_json())
            if i < len(list) - 1:
                json_builder.append(",")
        json_builder.append("]")
        return "".join(json_builder)
        

    @staticmethod
    def list_from_json(json: str) -> List["ResultValue"]:
        result_list = []
        json = re.sub(r"\s+", "", json) 
        json = json.replace("[", "").replace("]", "")
        json_objects = re.split(r"(?<=}),\s*(?={)", json)
        for json_object in json_objects:
            result_list.append(ResultValue.from_json(json_object))
        return result_list
    

    def to_ResultValueInternal(self): 
        from tests.gherkinexecutor.Feature_Full_Test.ResultValueInternal import ResultValueInternal
        return ResultValueInternal(
            int(self.sum)
        )

    class Builder:
        def __init__(self) -> None:
            self.sum = ""

        def setSum(self, sum: str) -> 'Builder':
            self.sum = sum
            return self

        def set_compare(self) -> 'Builder':
            self.sum = "?DNC?"
            return self

        def build(self):
            return ResultValue(
                self.sum
            )
