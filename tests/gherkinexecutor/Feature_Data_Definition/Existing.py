from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
class Existing:

    @staticmethod
    def to_data_type_string() -> str:
        return "Existing {"
        + "int " 
        + "str " 
        + "float " 
        + "} "

    def to_TestIn(self) :
        from tests.gherkinexecutor.Feature_Data_Definition.TestIn import TestIn
        return TestIn(
         str(self.aValue)
        , str(self.bValue)
        , str(self.cValue)
        )

    def __init__(self,
         aValue: int
        , bValue: str
        , cValue: float
        ) -> None:
        self.aValue = aValue
        self.bValue = bValue
        self.cValue = cValue

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _Existing = other
        return  ( _Existing.aValue == self.aValue)  and ( _Existing.bValue == self.bValue)  and ( _Existing.cValue == self.cValue)

    def __str__(self) -> str:
        return "{Existing} {{" + \
         " aValue = " + str(self.aValue) + " "  " bValue = " + str(self.bValue) + " "  " cValue = " + str(self.cValue) + " "  "} " + "\n" + "}"
