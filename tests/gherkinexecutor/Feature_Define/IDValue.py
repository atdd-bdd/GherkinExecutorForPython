import sys
import re
from typing import List


class IDValue:
    def __init__(self,
                 iD: str = ""
                , value: str = ""
                ) -> None:
        self.iD = iD
        self.value = value

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _IDValue = other
        result1 = True
        if not (self.iD == "?DNC?" or _IDValue.iD == "?DNC?"):
            if not _IDValue.iD == self.iD:
                result1 = False
        if not (self.value == "?DNC?" or _IDValue.value == "?DNC?"):
            if not _IDValue.value == self.value:
                result1 = False
        return result1


    def __str__(self) -> str:
        return "{IDValue} {" + \
         " iD = " + str(self.iD) + " "  " value = " + str(self.value) + " "  "} " + "\n"

    def to_json(self) -> str:
        return "{" + \
            '"iD": "' + str(self.iD) + '"' +  \
            "," + '"value": "' + str(self.value) + '"' +  \
            "}"

    @staticmethod
    def from_json(json: str):
        instance = IDValue()
        json = re.sub(r"\s+", "", json) 
        json = json.replace("{","").replace("}","") 
        key_value_pairs = json.split(",")
        for pair in key_value_pairs:
            entry = pair.split(":")
            key = entry[0].replace('\"', "").strip()
            value = entry[1].replace('\"', "").strip()
            switch = {
                   "iD": lambda: setattr(instance, "iD", value),
                "value": lambda: setattr(instance, "value", value),

                }
            switch.get(key, lambda: print(f"Invalid JSON element {key}", file=sys.stderr))()
        return instance
        

    @staticmethod
    def list_to_json(list: List["IDValue"]) -> str:
        json_builder = []
        json_builder.append("[")
        for i in range(len(list)):
            json_builder.append(list[i].to_json())
            if i < len(list) - 1:
                json_builder.append(",")
        json_builder.append("]")
        return "".join(json_builder)
        

    @staticmethod
    def list_from_json(json: str) -> List["IDValue"]:
        result_list = []
        json = re.sub(r"\s+", "", json) 
        json = json.replace("[", "").replace("]", "")
        json_objects = re.split(r"(?<=}),\s*(?={)", json)
        for json_object in json_objects:
            result_list.append(IDValue.from_json(json_object))
        return result_list
    

    class Builder:
        def __init__(self) -> None:
            self.iD = ""
            self.value = ""

        def setId(self, iD: str) -> 'Builder':
            self.iD = iD
            return self

        def setValue(self, value: str) -> 'Builder':
            self.value = value
            return self

        def set_compare(self) -> 'Builder':
            self.iD = "?DNC?"
            self.value = "?DNC?"
            return self

        def build(self):
            return IDValue(
                self.iD
                ,self.value
            )
