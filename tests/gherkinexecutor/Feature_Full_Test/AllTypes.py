import sys
import re
from typing import List
from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime
class AllTypes:
    def __init__(self,
                 anInt: str = "0"
                , aFloat: str = "0.0"
                , aBool: str = "false"
                , aString: str = ""
                , aComplex: str = "0+0j"
                ) -> None:
        self.anInt = anInt
        self.aFloat = aFloat
        self.aBool = aBool
        self.aString = aString
        self.aComplex = aComplex

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _AllTypes = other
        result1 = True
        if not (self.anInt == "?DNC?" or _AllTypes.anInt == "?DNC?"):
            if not _AllTypes.anInt == self.anInt:
                result1 = False
        if not (self.aFloat == "?DNC?" or _AllTypes.aFloat == "?DNC?"):
            if not _AllTypes.aFloat == self.aFloat:
                result1 = False
        if not (self.aBool == "?DNC?" or _AllTypes.aBool == "?DNC?"):
            if not _AllTypes.aBool == self.aBool:
                result1 = False
        if not (self.aString == "?DNC?" or _AllTypes.aString == "?DNC?"):
            if not _AllTypes.aString == self.aString:
                result1 = False
        if not (self.aComplex == "?DNC?" or _AllTypes.aComplex == "?DNC?"):
            if not _AllTypes.aComplex == self.aComplex:
                result1 = False
        return result1


    def __str__(self) -> str:
        return "{AllTypes} {" + \
         " anInt = " + str(self.anInt) + " "  " aFloat = " + str(self.aFloat) + " "  " aBool = " + str(self.aBool) + " "  " aString = " + str(self.aString) + " "  " aComplex = " + str(self.aComplex) + " "  "} " + "\n"

    def to_json(self) -> str:
        return "{" + \
            '"anInt": "' + str(self.anInt) + '"' +  \
            "," + '"aFloat": "' + str(self.aFloat) + '"' +  \
            "," + '"aBool": "' + str(self.aBool) + '"' +  \
            "," + '"aString": "' + str(self.aString) + '"' +  \
            "," + '"aComplex": "' + str(self.aComplex) + '"' +  \
            "}"

    @staticmethod
    def from_json(json: str):
        instance = AllTypes()
        json = re.sub(r"\s+", "", json) 
        json = json.replace("{","").replace("}","") 
        key_value_pairs = json.split(",")
        for pair in key_value_pairs:
            entry = pair.split(":")
            key = entry[0].replace('\"', "").strip()
            value = entry[1].replace('\"', "").strip()
            switch = {
                   "anInt": lambda: setattr(instance, "anInt", value),
                "aFloat": lambda: setattr(instance, "aFloat", value),
                "aBool": lambda: setattr(instance, "aBool", value),
                "aString": lambda: setattr(instance, "aString", value),
                "aComplex": lambda: setattr(instance, "aComplex", value),

                }
            switch.get(key, lambda: print(f"Invalid JSON element {key}", file=sys.stderr))()
        return instance
        

    @staticmethod
    def list_to_json(list: List["AllTypes"]) -> str:
        json_builder = []
        json_builder.append("[")
        for i in range(len(list)):
            json_builder.append(list[i].to_json())
            if i < len(list) - 1:
                json_builder.append(",")
        json_builder.append("]")
        return "".join(json_builder)
        

    @staticmethod
    def list_from_json(json: str) -> List["AllTypes"]:
        result_list = []
        json = re.sub(r"\s+", "", json) 
        json = json.replace("[", "").replace("]", "")
        json_objects = re.split(r"(?<=}),\s*(?={)", json)
        for json_object in json_objects:
            result_list.append(AllTypes.from_json(json_object))
        return result_list
    

    def to_AllTypesInternal(self): 
        from tests.gherkinexecutor.Feature_Full_Test.AllTypesInternal import AllTypesInternal
        return AllTypesInternal(
            int(self.anInt)
            ,float(self.aFloat)
            ,bool(self.aBool)
            ,self.aString
            ,complex(self.aComplex)
        )

    class Builder:
        def __init__(self) -> None:
            self.anInt = "0"
            self.aFloat = "0.0"
            self.aBool = "false"
            self.aString = ""
            self.aComplex = "0+0j"

        def setAnint(self, anInt: str) -> 'Builder':
            self.anInt = anInt
            return self

        def setAfloat(self, aFloat: str) -> 'Builder':
            self.aFloat = aFloat
            return self

        def setAbool(self, aBool: str) -> 'Builder':
            self.aBool = aBool
            return self

        def setAstring(self, aString: str) -> 'Builder':
            self.aString = aString
            return self

        def setAcomplex(self, aComplex: str) -> 'Builder':
            self.aComplex = aComplex
            return self

        def set_compare(self) -> 'Builder':
            self.anInt = "?DNC?"
            self.aFloat = "?DNC?"
            self.aBool = "?DNC?"
            self.aString = "?DNC?"
            self.aComplex = "?DNC?"
            return self

        def build(self):
            return AllTypes(
                self.anInt
                ,self.aFloat
                ,self.aBool
                ,self.aString
                ,self.aComplex
            )
