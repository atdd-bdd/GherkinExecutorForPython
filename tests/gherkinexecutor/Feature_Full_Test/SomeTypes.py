import sys
import re
from typing import List
from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime


class SomeTypes:
    def __init__(self,
                 anInt: str = "0"
                , aDouble: str = "0.0"
                , aChar: str = "x"
                , anchar: str = "y"
                ) -> None:
        self.anInt = anInt
        self.aDouble = aDouble
        self.aChar = aChar
        self.anchar = anchar

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _SomeTypes = other
        result1 = True
        if not (self.anInt == "?DNC?" or _SomeTypes.anInt == "?DNC?"):
            if not _SomeTypes.anInt == self.anInt:
                result1 = False
        if not (self.aDouble == "?DNC?" or _SomeTypes.aDouble == "?DNC?"):
            if not _SomeTypes.aDouble == self.aDouble:
                result1 = False
        if not (self.aChar == "?DNC?" or _SomeTypes.aChar == "?DNC?"):
            if not _SomeTypes.aChar == self.aChar:
                result1 = False
        if not (self.anchar == "?DNC?" or _SomeTypes.anchar == "?DNC?"):
            if not _SomeTypes.anchar == self.anchar:
                result1 = False
        return result1


    def __str__(self) -> str:
        return "{SomeTypes} {" + \
         " anInt = " + str(self.anInt) + " "  " aDouble = " + str(self.aDouble) + " "  " aChar = " + str(self.aChar) + " "  " anchar = " + str(self.anchar) + " "  "} " + "\n"

    def to_json(self) -> str:
        return "{" + \
            '"anInt": "' + str(self.anInt) + '"' +  \
            "," + '"aDouble": "' + str(self.aDouble) + '"' +  \
            "," + '"aChar": "' + str(self.aChar) + '"' +  \
            "," + '"anchar": "' + str(self.anchar) + '"' +  \
            "}"

    @staticmethod
    def from_json(json: str):
        instance = SomeTypes()
        json = re.sub(r"\s+", "", json) 
        json = json.replace("{","").replace("}","") 
        key_value_pairs = json.split(",")
        for pair in key_value_pairs:
            entry = pair.split(":")
            key = entry[0].replace('\"', "").strip()
            value = entry[1].replace('\"', "").strip()
            switch = {
                   "anInt": lambda: setattr(instance, "anInt", value),
                "aDouble": lambda: setattr(instance, "aDouble", value),
                "aChar": lambda: setattr(instance, "aChar", value),
                "anchar": lambda: setattr(instance, "anchar", value),

                }
            switch.get(key, lambda: print(f"Invalid JSON element {key}", file=sys.stderr))()
        return instance
        

    @staticmethod
    def list_to_json(list: List["SomeTypes"]) -> str:
        json_builder = []
        json_builder.append("[")
        for i in range(len(list)):
            json_builder.append(list[i].to_json())
            if i < len(list) - 1:
                json_builder.append(",")
        json_builder.append("]")
        return "".join(json_builder)
        

    @staticmethod
    def list_from_json(json: str) -> List["SomeTypes"]:
        result_list = []
        json = re.sub(r"\s+", "", json) 
        json = json.replace("[", "").replace("]", "")
        json_objects = re.split(r"(?<=}),\s*(?={)", json)
        for json_object in json_objects:
            result_list.append(SomeTypes.from_json(json_object))
        return result_list
    

    def to_SomeTypesInternal(self): 
        from tests.gherkinexecutor.Feature_Full_Test.SomeTypesInternal import SomeTypesInternal
        return SomeTypesInternal(
            int(self.anInt)
            ,float(self.aDouble)
            ,self.aChar
            ,self.anchar
        )

    class Builder:
        def __init__(self) -> None:
            self.anInt = "0"
            self.aDouble = "0.0"
            self.aChar = "x"
            self.anchar = "y"

        def setAnint(self, anInt: str) -> 'Builder':
            self.anInt = anInt
            return self

        def setAdouble(self, aDouble: str) -> 'Builder':
            self.aDouble = aDouble
            return self

        def setAchar(self, aChar: str) -> 'Builder':
            self.aChar = aChar
            return self

        def setAnchar(self, anchar: str) -> 'Builder':
            self.anchar = anchar
            return self

        def set_compare(self) -> 'Builder':
            self.anInt = "?DNC?"
            self.aDouble = "?DNC?"
            self.aChar = "?DNC?"
            self.anchar = "?DNC?"
            return self

        def build(self):
            return SomeTypes(
                self.anInt
                ,self.aDouble
                ,self.aChar
                ,self.anchar
            )
