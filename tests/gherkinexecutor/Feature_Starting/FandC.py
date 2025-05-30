import sys
import re
from typing import List


class FandC:
    def __init__(self,
                 f: str = "0"
                , c: str = "0"
                , notes: str = ""
                ) -> None:
        self.f = f
        self.c = c
        self.notes = notes

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _FandC = other
        result1 = True
        if not (self.f == "?DNC?" or _FandC.f == "?DNC?"):
            if not _FandC.f == self.f:
                result1 = False
        if not (self.c == "?DNC?" or _FandC.c == "?DNC?"):
            if not _FandC.c == self.c:
                result1 = False
        if not (self.notes == "?DNC?" or _FandC.notes == "?DNC?"):
            if not _FandC.notes == self.notes:
                result1 = False
        return result1


    def __str__(self) -> str:
        return "{FandC} {" + \
         " f = " + str(self.f) + " "  " c = " + str(self.c) + " "  " notes = " + str(self.notes) + " "  "} " + "\n"

    def to_json(self) -> str:
        return "{" + \
            '"f": "' + str(self.f) + '"' +  \
            "," + '"c": "' + str(self.c) + '"' +  \
            "," + '"notes": "' + str(self.notes) + '"' +  \
            "}"

    @staticmethod
    def from_json(json: str):
        instance = FandC()
        json = re.sub(r"\s+", "", json) 
        json = json.replace("{","").replace("}","") 
        key_value_pairs = json.split(",")
        for pair in key_value_pairs:
            entry = pair.split(":")
            key = entry[0].replace('\"', "").strip()
            value = entry[1].replace('\"', "").strip()
            switch = {
                   "f": lambda: setattr(instance, "f", value),
                "c": lambda: setattr(instance, "c", value),
                "notes": lambda: setattr(instance, "notes", value),

                }
            switch.get(key, lambda: print(f"Invalid JSON element {key}", file=sys.stderr))()
        return instance
        

    @staticmethod
    def list_to_json(list: List["FandC"]) -> str:
        json_builder = []
        json_builder.append("[")
        for i in range(len(list)):
            json_builder.append(list[i].to_json())
            if i < len(list) - 1:
                json_builder.append(",")
        json_builder.append("]")
        return "".join(json_builder)
        

    @staticmethod
    def list_from_json(json: str) -> List["FandC"]:
        result_list = []
        json = re.sub(r"\s+", "", json) 
        json = json.replace("[", "").replace("]", "")
        json_objects = re.split(r"(?<=}),\s*(?={)", json)
        for json_object in json_objects:
            result_list.append(FandC.from_json(json_object))
        return result_list
    

    def to_FandCInternal(self): 
        from tests.gherkinexecutor.Feature_Starting.FandCInternal import FandCInternal
        return FandCInternal(
            int(self.f)
            ,int(self.c)
            ,self.notes
        )

    class Builder:
        def __init__(self) -> None:
            self.f = "0"
            self.c = "0"
            self.notes = ""

        def setF(self, f: str) -> 'Builder':
            self.f = f
            return self

        def setC(self, c: str) -> 'Builder':
            self.c = c
            return self

        def setNotes(self, notes: str) -> 'Builder':
            self.notes = notes
            return self

        def set_compare(self) -> 'Builder':
            self.f = "?DNC?"
            self.c = "?DNC?"
            self.notes = "?DNC?"
            return self

        def build(self):
            return FandC(
                self.f
                ,self.c
                ,self.notes
            )
