from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
class FilterValue:
    def __init__(self,
                  value: str = "Q0000"
        ) -> None:
        self.value = value
    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _FilterValue = other
        _FilterValue:FilterValue=  o
        result1 = True;
        if (
             not self.value == "?DNC?"
                and not _FilterValue.value == "?DNC?"):
                if (not  _FilterValue.value== self.value):
                    result1 = False
                result1 = False
        return result1

    def __str__(self) -> str:
        return "{FilterValue} {{" + \
         " value = " + str(self.value) + " "  "} " + "\n" + "}"
    def to_FilterValueInternal(self): 
        from tests.gherkinexecutor.Feature_Examples.FilterValueInternal import FilterValueInternal
        return FilterValueInternal(
            ID(self.value)
        )

    class Builder:
        def __init__(self) -> None:
            self.value = "Q0000"

        def setValue(self, value: str) -> 'Builder':
            self.value = value
            return self

        def set_compare(self) -> 'Builder':
            self.value = "?DNC?"
            return self

        def build(self):
            return FilterValue(
                self.value
            )
