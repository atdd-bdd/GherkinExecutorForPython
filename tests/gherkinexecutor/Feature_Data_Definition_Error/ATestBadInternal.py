from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations


class ATestBadInternal:

    @staticmethod
    def to_data_type_string() -> str:
        return "ATestBadInternal {"
        + "int " 
        + "str " 
        + "float " 
        + "} "

    def to_ATestBad(self) :
        from tests.gherkinexecutor.Feature_Data_Definition_Error.ATestBad import ATestBad
        return ATestBad(
         str(self.anInt)
        , str(self.aString)
        , str(self.aDouble)
        )

    def __init__(self,
                anInt: int
               , aString: str
               , aDouble: float
                ) -> None:
        self.anInt = anInt
        self.aString = aString
        self.aDouble = aDouble

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _ATestBadInternal = other
        return  ( _ATestBadInternal.anInt == self.anInt)  and ( _ATestBadInternal.aString == self.aString)  and ( _ATestBadInternal.aDouble == self.aDouble)

    def __str__(self) -> str:
        return "{ATestBadInternal} {" + \
         " anInt = " + str(self.anInt) + " "  " aString = " + str(self.aString) + " "  " aDouble = " + str(self.aDouble) + " "  "} " + "\n"
