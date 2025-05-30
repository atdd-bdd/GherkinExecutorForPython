from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
class ResultValueInternal:

    @staticmethod
    def to_data_type_string() -> str:
        return "ResultValueInternal {"
        + "int " 
        + "} "

    def to_ResultValue(self) :
        from tests.gherkinexecutor.Feature_Examples.ResultValue import ResultValue
        return ResultValue(
         str(self.sum)
        )

    def __init__(self,
         sum: int
        ) -> None:
        self.sum = sum

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _ResultValueInternal = other
        return  ( _ResultValueInternal.sum == self.sum)

    def __str__(self) -> str:
        return "{ResultValueInternal} {{" + \
         " sum = " + str(self.sum) + " "  "} " + "\n" + "}"
