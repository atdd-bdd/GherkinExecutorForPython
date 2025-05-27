import sys
import re
from typing import List
from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations


class TestIn:
    def __init__(self,
                 aValue: str = "0"
                , bValue: str = " "
                , cValue: str = "4.0"
                ) -> None:
        self.aValue = aValue
        self.bValue = bValue
        self.cValue = cValue

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _TestIn = other
        result1 = True
        if not (self.aValue == "?DNC?" or _TestIn.aValue == "?DNC?"):
            if not _TestIn.aValue == self.aValue:
                result1 = False
        if not (self.bValue == "?DNC?" or _TestIn.bValue == "?DNC?"):
            if not _TestIn.bValue == self.bValue:
                result1 = False
        if not (self.cValue == "?DNC?" or _TestIn.cValue == "?DNC?"):
            if not _TestIn.cValue == self.cValue:
                result1 = False
        return result1


    def __str__(self) -> str:
        return "{TestIn} {" + \
         " aValue = " + str(self.aValue) + " "  " bValue = " + str(self.bValue) + " "  " cValue = " + str(self.cValue) + " "  "} " + "\n"

    def to_json(self) -> str:
        return "{" + \
            '"aValue": "' + str(self.aValue) + '"' +  \
            "," + '"bValue": "' + str(self.bValue) + '"' +  \
            "," + '"cValue": "' + str(self.cValue) + '"' +  \
            "}"

    @staticmethod
    def from_json(json: str):
        instance = TestIn()
        json = re.sub(r"\s+", "", json) 
        json = json.replace("{","").replace("}","") 
        key_value_pairs = json.split(",")
        for pair in key_value_pairs:
            entry = pair.split(":")
            key = entry[0].replace('\"', "").strip()
            value = entry[1].replace('\"', "").strip()
            switch = {
                   "aValue": lambda: setattr(instance, "aValue", value),
                "bValue": lambda: setattr(instance, "bValue", value),
                "cValue": lambda: setattr(instance, "cValue", value),

                }
            switch.get(key, lambda: print(f"Invalid JSON element {key}", file=sys.stderr))()
        return instance
        

    @staticmethod
    def list_to_json(list: List["TestIn"]) -> str:
        json_builder = []
        json_builder.append("[")
        for i in range(len(list)):
            json_builder.append(list[i].to_json())
            if i < len(list) - 1:
                json_builder.append(",")
        json_builder.append("]")
        return "".join(json_builder)
        

    @staticmethod
    def list_from_json(json: str) -> List["TestIn"]:
        result_list = []
        json = re.sub(r"\s+", "", json) 
        json = json.replace("[", "").replace("]", "")
        json_objects = re.split(r"(?<=}),\s*(?={)", json)
        for json_object in json_objects:
            result_list.append(TestIn.from_json(json_object))
        return result_list
    

    def to_Existing(self): 
        from tests.gherkinexecutor.Feature_Data_Definition.Existing import Existing
        return Existing(
            int(self.aValue)
            ,self.bValue
            ,float(self.cValue)
        )

    class Builder:
        def __init__(self) -> None:
            self.aValue = "0"
            self.bValue = " "
            self.cValue = "4.0"

        def setAvalue(self, aValue: str) -> 'Builder':
            self.aValue = aValue
            return self

        def setBvalue(self, bValue: str) -> 'Builder':
            self.bValue = bValue
            return self

        def setCvalue(self, cValue: str) -> 'Builder':
            self.cValue = cValue
            return self

        def set_compare(self) -> 'Builder':
            self.aValue = "?DNC?"
            self.bValue = "?DNC?"
            self.cValue = "?DNC?"
            return self

        def build(self):
            return TestIn(
                self.aValue
                ,self.bValue
                ,self.cValue
            )
