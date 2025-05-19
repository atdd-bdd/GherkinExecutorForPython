from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
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
        _FandC:FandC=  o
        result1 = True;
        if (
             not self.f == "?DNC?"
                and not _FandC.f == "?DNC?"):
                if (not  _FandC.f== self.f):
                    result1 = False
                result1 = False
        if (
             not self.c == "?DNC?"
                and not _FandC.c == "?DNC?"):
                if (not  _FandC.c== self.c):
                    result1 = False
                result1 = False
        if (
             not self.notes == "?DNC?"
                and not _FandC.notes == "?DNC?"):
                if (not  _FandC.notes== self.notes):
                    result1 = False
                result1 = False
        return result1

    def __str__(self) -> str:
        return "{FandC} {{" + \
         " f = " + str(self.f) + " "  " c = " + str(self.c) + " "  " notes = " + str(self.notes) + " "  "} " + "\n" + "}"
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
