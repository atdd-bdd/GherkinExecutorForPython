import sys
import re
from typing import List
from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
class ATestBad:
    def __init__(self,
                 anInt: str = "a"
                , aString: str = " "
                , aDouble: str = "b"
                ) -> None:
        self.anInt = anInt
        self.aString = aString
        self.aDouble = aDouble

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _ATestBad = other
        result1 = True
        if not (self.anInt == "?DNC?" or _ATestBad.anInt == "?DNC?"):
            if not _ATestBad.anInt == self.anInt:
                result1 = False
        if not (self.aString == "?DNC?" or _ATestBad.aString == "?DNC?"):
            if not _ATestBad.aString == self.aString:
                result1 = False
        if not (self.aDouble == "?DNC?" or _ATestBad.aDouble == "?DNC?"):
            if not _ATestBad.aDouble == self.aDouble:
                result1 = False
        return result1


    def __str__(self) -> str:
        return "{ATestBad} {" + \
         " anInt = " + str(self.anInt) + " "  " aString = " + str(self.aString) + " "  " aDouble = " + str(self.aDouble) + " "  "} " + "\n"

    def to_json(self) -> str:
        return "{" + \
            '"anInt": "' + str(self.anInt) + '"' +  \
            "," + '"aString": "' + str(self.aString) + '"' +  \
            "," + '"aDouble": "' + str(self.aDouble) + '"' +  \
            "}"

    @staticmethod
    def from_json(json: str):
        instance = ATestBad()
        json = re.sub(r"\s+", "", json) 
        json = json.replace("{","").replace("}","") 
        key_value_pairs = json.split(",")
        for pair in key_value_pairs:
            entry = pair.split(":")
            key = entry[0].replace('\"', "").strip()
            value = entry[1].replace('\"', "").strip()
            switch = {
                   "anInt": lambda: setattr(instance, "anInt", value),
                "aString": lambda: setattr(instance, "aString", value),
                "aDouble": lambda: setattr(instance, "aDouble", value),

                }
            switch.get(key, lambda: print(f"Invalid JSON element {key}", file=sys.stderr))()
        return instance
        

    @staticmethod
    def list_to_json(list: List["ATestBad"]) -> str:
        json_builder = []
        json_builder.append("[")
        for i in range(len(list)):
            json_builder.append(list[i].to_json())
            if i < len(list) - 1:
                json_builder.append(",")
        json_builder.append("]")
        return "".join(json_builder)
        

    @staticmethod
    def list_from_json(json: str) -> List["ATestBad"]:
        result_list = []
        json = re.sub(r"\s+", "", json) 
        json = json.replace("[", "").replace("]", "")
        json_objects = re.split(r"(?<=}),\s*(?={)", json)
        for json_object in json_objects:
            result_list.append(ATestBad.from_json(json_object))
        return result_list
    

    def to_ATestBadInternal(self): 
        from tests.gherkinexecutor.Feature_Data_Definition_Error.ATestBadInternal import ATestBadInternal
        return ATestBadInternal(
            int(self.anInt)
            ,self.aString
            ,float(self.aDouble)
        )

    class Builder:
        def __init__(self) -> None:
            self.anInt = "a"
            self.aString = " "
            self.aDouble = "b"

        def setAnint(self, anInt: str) -> 'Builder':
            self.anInt = anInt
            return self

        def setAstring(self, aString: str) -> 'Builder':
            self.aString = aString
            return self

        def setAdouble(self, aDouble: str) -> 'Builder':
            self.aDouble = aDouble
            return self

        def set_compare(self) -> 'Builder':
            self.anInt = "?DNC?"
            self.aString = "?DNC?"
            self.aDouble = "?DNC?"
            return self

        def build(self):
            return ATestBad(
                self.anInt
                ,self.aString
                ,self.aDouble
            )
