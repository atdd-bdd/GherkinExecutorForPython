from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
class FandCInternal:

    @staticmethod
    def to_data_type_string() -> str:
        return "FandCInternal {"
        + "int " 
        + "int " 
        + "str " 
        + "} "

    def to_FandC(self) :
        from tests.gherkinexecutor.Feature_Examples.FandC import FandC
        return FandC(
         str(self.f)
        , str(self.c)
        , str(self.notes)
        )

    def __init__(self,
         f: int
        , c: int
        , notes: str
        ) -> None:
        self.f = f
        self.c = c
        self.notes = notes

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _FandCInternal = other
        return  ( _FandCInternal.f  ==  self.f)  and ( _FandCInternal.c  ==  self.c)  and ( _FandCInternal.notes  ==  self.notes)


    def __str__(self) -> str:
        return "{FandCInternal} {{" + \
         " f = " + str(self.f) + " "  " c = " + str(self.c) + " "  " notes = " + str(self.notes) + " "  "} " + "\n" + "}"
