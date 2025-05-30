from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime
class SomeTypesInternal:

    @staticmethod
    def to_data_type_string() -> str:
        return "SomeTypesInternal {"
        + "int " 
        + "float " 
        + "str " 
        + "str " 
        + "} "

    def to_SomeTypes(self) :
        from tests.gherkinexecutor.Feature_Full_Test.SomeTypes import SomeTypes
        return SomeTypes(
         str(self.anInt)
        , str(self.aDouble)
        , str(self.aChar)
        , str(self.anchar)
        )

    def __init__(self,
                anInt: int
               , aDouble: float
               , aChar: str
               , anchar: str
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
        _SomeTypesInternal = other
        return  ( _SomeTypesInternal.anInt == self.anInt)  and ( _SomeTypesInternal.aDouble == self.aDouble)  and ( _SomeTypesInternal.aChar == self.aChar)  and ( _SomeTypesInternal.anchar == self.anchar)

    def __str__(self) -> str:
        return "{SomeTypesInternal} {" + \
         " anInt = " + str(self.anInt) + " "  " aDouble = " + str(self.aDouble) + " "  " aChar = " + str(self.aChar) + " "  " anchar = " + str(self.anchar) + " "  "} " + "\n"
