import sys
import re
from typing import List
from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime


class Move:
    def __init__(self,
                 row: str = "0"
                , column: str = "0"
                , mark: str = "^"
                ) -> None:
        self.row = row
        self.column = column
        self.mark = mark

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _Move = other
        result1 = True
        if not (self.row == "?DNC?" or _Move.row == "?DNC?"):
            if not _Move.row == self.row:
                result1 = False
        if not (self.column == "?DNC?" or _Move.column == "?DNC?"):
            if not _Move.column == self.column:
                result1 = False
        if not (self.mark == "?DNC?" or _Move.mark == "?DNC?"):
            if not _Move.mark == self.mark:
                result1 = False
        return result1


    def __str__(self) -> str:
        return "{Move} {" + \
         " row = " + str(self.row) + " "  " column = " + str(self.column) + " "  " mark = " + str(self.mark) + " "  "} " + "\n"

    def to_json(self) -> str:
        return "{" + \
            '"row": "' + str(self.row) + '"' +  \
            "," + '"column": "' + str(self.column) + '"' +  \
            "," + '"mark": "' + str(self.mark) + '"' +  \
            "}"

    @staticmethod
    def from_json(json: str):
        instance = Move()
        json = re.sub(r"\s+", "", json) 
        json = json.replace("{","").replace("}","") 
        key_value_pairs = json.split(",")
        for pair in key_value_pairs:
            entry = pair.split(":")
            key = entry[0].replace('\"', "").strip()
            value = entry[1].replace('\"', "").strip()
            switch = {
                   "row": lambda: setattr(instance, "row", value),
                "column": lambda: setattr(instance, "column", value),
                "mark": lambda: setattr(instance, "mark", value),

                }
            switch.get(key, lambda: print(f"Invalid JSON element {key}", file=sys.stderr))()
        return instance
        

    @staticmethod
    def list_to_json(list: List["Move"]) -> str:
        json_builder = []
        json_builder.append("[")
        for i in range(len(list)):
            json_builder.append(list[i].to_json())
            if i < len(list) - 1:
                json_builder.append(",")
        json_builder.append("]")
        return "".join(json_builder)
        

    @staticmethod
    def list_from_json(json: str) -> List["Move"]:
        result_list = []
        json = re.sub(r"\s+", "", json) 
        json = json.replace("[", "").replace("]", "")
        json_objects = re.split(r"(?<=}),\s*(?={)", json)
        for json_object in json_objects:
            result_list.append(Move.from_json(json_object))
        return result_list
    

    def to_MoveInternal(self): 
        from tests.gherkinexecutor.Feature_Full_Test.MoveInternal import MoveInternal
        return MoveInternal(
            int(self.row)
            ,int(self.column)
            ,self.mark
        )

    class Builder:
        def __init__(self) -> None:
            self.row = "0"
            self.column = "0"
            self.mark = "^"

        def setRow(self, row: str) -> 'Builder':
            self.row = row
            return self

        def setColumn(self, column: str) -> 'Builder':
            self.column = column
            return self

        def setMark(self, mark: str) -> 'Builder':
            self.mark = mark
            return self

        def set_compare(self) -> 'Builder':
            self.row = "?DNC?"
            self.column = "?DNC?"
            self.mark = "?DNC?"
            return self

        def build(self):
            return Move(
                self.row
                ,self.column
                ,self.mark
            )
