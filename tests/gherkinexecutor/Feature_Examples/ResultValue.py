from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
class ResultValue:
    def __init__(self,
                  sum: str = ""
        ) -> None:
        self.sum = sum
    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _ResultValue = other
        _ResultValue:ResultValue=  o
        result1 = True;
        if (
             not self.sum == "?DNC?"
                and not _ResultValue.sum == "?DNC?"):
                if (not  _ResultValue.sum== self.sum):
                    result1 = False
                result1 = False
        return result1

    def __str__(self) -> str:
        return "{ResultValue} {{" + \
         " sum = " + str(self.sum) + " "  "} " + "\n" + "}"
    def to_ResultValueInternal(self): 
        from tests.gherkinexecutor.Feature_Examples.ResultValueInternal import ResultValueInternal
        return ResultValueInternal(
            int(self.sum)
        )

    class Builder:
        def __init__(self) -> None:
            self.sum = ""

        def setSum(self, sum: str) -> 'Builder':
            self.sum = sum
            return self

        def set_compare(self) -> 'Builder':
            self.sum = "?DNC?"
            return self

        def build(self):
            return ResultValue(
                self.sum
            )
