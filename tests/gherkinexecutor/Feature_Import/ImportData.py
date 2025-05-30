import sys
import re
from typing import List
from datetime import datetime
from tests.gherkinexecutor.Feature_Import.Color import Color


class ImportData:
    def __init__(self,
                 myDate: str = "1900-01-21"
                , color: str = "RED"
                ) -> None:
        self.myDate = myDate
        self.color = color

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _ImportData = other
        result1 = True
        if not (self.myDate == "?DNC?" or _ImportData.myDate == "?DNC?"):
            if not _ImportData.myDate == self.myDate:
                result1 = False
        if not (self.color == "?DNC?" or _ImportData.color == "?DNC?"):
            if not _ImportData.color == self.color:
                result1 = False
        return result1


    def __str__(self) -> str:
        return "{ImportData} {" + \
         " myDate = " + str(self.myDate) + " "  " color = " + str(self.color) + " "  "} " + "\n"

    def to_json(self) -> str:
        return "{" + \
            '"myDate": "' + str(self.myDate) + '"' +  \
            "," + '"color": "' + str(self.color) + '"' +  \
            "}"

    @staticmethod
    def from_json(json: str):
        instance = ImportData()
        json = re.sub(r"\s+", "", json) 
        json = json.replace("{","").replace("}","") 
        key_value_pairs = json.split(",")
        for pair in key_value_pairs:
            entry = pair.split(":")
            key = entry[0].replace('\"', "").strip()
            value = entry[1].replace('\"', "").strip()
            switch = {
                   "myDate": lambda: setattr(instance, "myDate", value),
                "color": lambda: setattr(instance, "color", value),

                }
            switch.get(key, lambda: print(f"Invalid JSON element {key}", file=sys.stderr))()
        return instance
        

    @staticmethod
    def list_to_json(list: List["ImportData"]) -> str:
        json_builder = []
        json_builder.append("[")
        for i in range(len(list)):
            json_builder.append(list[i].to_json())
            if i < len(list) - 1:
                json_builder.append(",")
        json_builder.append("]")
        return "".join(json_builder)
        

    @staticmethod
    def list_from_json(json: str) -> List["ImportData"]:
        result_list = []
        json = re.sub(r"\s+", "", json) 
        json = json.replace("[", "").replace("]", "")
        json_objects = re.split(r"(?<=}),\s*(?={)", json)
        for json_object in json_objects:
            result_list.append(ImportData.from_json(json_object))
        return result_list
    

    def to_ImportDataInternal(self): 
        from tests.gherkinexecutor.Feature_Import.ImportDataInternal import ImportDataInternal
        return ImportDataInternal(
            datetime.fromisoformat(self.myDate)
            ,Color[self.color]
        )

    class Builder:
        def __init__(self) -> None:
            self.myDate = "1900-01-21"
            self.color = "RED"

        def setMydate(self, myDate: str) -> 'Builder':
            self.myDate = myDate
            return self

        def setColor(self, color: str) -> 'Builder':
            self.color = color
            return self

        def set_compare(self) -> 'Builder':
            self.myDate = "?DNC?"
            self.color = "?DNC?"
            return self

        def build(self):
            return ImportData(
                self.myDate
                ,self.color
            )
