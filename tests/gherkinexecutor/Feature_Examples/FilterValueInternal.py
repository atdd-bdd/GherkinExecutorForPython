from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
class FilterValueInternal:

    @staticmethod
    def to_data_type_string() -> str:
        return "FilterValueInternal {"
        + "ID " 
        + "} "

    def to_FilterValue(self) :
        from tests.gherkinexecutor.Feature_Examples.FilterValue import FilterValue
        return FilterValue(
         str(self.value)
        )

    def __init__(self,
         value: ID
        ) -> None:
        self.value = value

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _FilterValueInternal = other
        return  ( _FilterValueInternal.value == self.value)


    def __str__(self) -> str:
        return "{FilterValueInternal} {{" + \
         " value = " + str(self.value) + " "  "} " + "\n" + "}"
