import sys
import re
from typing import List
from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime


class SimpleClass:
    def __init__(self,
                 anInt: str = "0"
                , aString: str = "Q"
                ) -> None:
        self.anInt = anInt
        self.aString = aString

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _SimpleClass = other
        result1 = True
        if not (self.anInt == "?DNC?" or _SimpleClass.anInt == "?DNC?"):
            if not _SimpleClass.anInt == self.anInt:
                result1 = False
        if not (self.aString == "?DNC?" or _SimpleClass.aString == "?DNC?"):
            if not _SimpleClass.aString == self.aString:
                result1 = False
        return result1


    def __str__(self) -> str:
        return "{SimpleClass} {" + \
         " anInt = " + str(self.anInt) + " "  " aString = " + str(self.aString) + " "  "} " + "\n"

    def to_json(self) -> str:
        return "{" + \
            '"anInt": "' + str(self.anInt) + '"' +  \
            "," + '"aString": "' + str(self.aString) + '"' +  \
            "}"

    @staticmethod
    def from_json(json: str):
        instance = SimpleClass()
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

                }
            switch.get(key, lambda: print(f"Invalid JSON element {key}", file=sys.stderr))()
        return instance
        

    @staticmethod
    def list_to_json(list: List["SimpleClass"]) -> str:
        json_builder = []
        json_builder.append("[")
        for i in range(len(list)):
            json_builder.append(list[i].to_json())
            if i < len(list) - 1:
                json_builder.append(",")
        json_builder.append("]")
        return "".join(json_builder)
        

    @staticmethod
    def list_from_json(json: str) -> List["SimpleClass"]:
        result_list = []
        json = re.sub(r"\s+", "", json) 
        json = json.replace("[", "").replace("]", "")
        json_objects = re.split(r"(?<=}),\s*(?={)", json)
        for json_object in json_objects:
            result_list.append(SimpleClass.from_json(json_object))
        return result_list
    

    def to_SimpleClassInternal(self): 
        from tests.gherkinexecutor.Feature_Full_Test.SimpleClassInternal import SimpleClassInternal
        return SimpleClassInternal(
            int(self.anInt)
            ,self.aString
        )

    class Builder:
        def __init__(self) -> None:
            self.anInt = "0"
            self.aString = "Q"

        def setAnint(self, anInt: str) -> 'Builder':
            self.anInt = anInt
            return self

        def setAstring(self, aString: str) -> 'Builder':
            self.aString = aString
            return self

        def set_compare(self) -> 'Builder':
            self.anInt = "?DNC?"
            self.aString = "?DNC?"
            return self

        def build(self):
            return SimpleClass(
                self.anInt
                ,self.aString
            )
