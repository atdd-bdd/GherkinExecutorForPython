from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations


class AllTypesInternal:

    @staticmethod
    def to_data_type_string() -> str:
        return "AllTypesInternal {"
        + "int " 
        + "float " 
        + "bool " 
        + "str " 
        + "complex " 
        + "} "

    def to_AllTypes(self) :
        from tests.gherkinexecutor.Feature_Data_Definition.AllTypes import AllTypes
        return AllTypes(
         str(self.anInt)
        , str(self.aFloat)
        , str(self.aBool)
        , str(self.aString)
        , str(self.aComplex)
        )

    def __init__(self,
                anInt: int
               , aFloat: float
               , aBool: bool
               , aString: str
               , aComplex: complex
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
        _AllTypesInternal = other
        return  ( _AllTypesInternal.anInt == self.anInt)  and ( _AllTypesInternal.aFloat == self.aFloat)  and ( _AllTypesInternal.aBool == self.aBool)  and ( _AllTypesInternal.aString == self.aString)  and ( _AllTypesInternal.aComplex == self.aComplex)

    def __str__(self) -> str:
        return "{AllTypesInternal} {" + \
         " anInt = " + str(self.anInt) + " "  " aFloat = " + str(self.aFloat) + " "  " aBool = " + str(self.aBool) + " "  " aString = " + str(self.aString) + " "  " aComplex = " + str(self.aComplex) + " "  "} " + "\n"
