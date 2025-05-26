from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
class ValueValidInternal:

    @staticmethod
    def to_data_type_string() -> str:
        return "ValueValidInternal {"
        + "str " 
        + "bool " 
        + "str " 
        + "} "

    def to_ValueValid(self) :
        from tests.gherkinexecutor.Feature_Examples.ValueValid import ValueValid
        return ValueValid(
         str(self.value)
        , str(self.valid)
        , str(self.notes)
        )

    def __init__(self,
         value: str
        , valid: bool
        , notes: str
        ) -> None:
        self.value = value
        self.valid = valid
        self.notes = notes

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _ValueValidInternal = other
        return  ( _ValueValidInternal.value == self.value)  and ( _ValueValidInternal.valid == self.valid)  and ( _ValueValidInternal.notes == self.notes)

    def __str__(self) -> str:
        return "{ValueValidInternal} {{" + \
         " value = " + str(self.value) + " "  " valid = " + str(self.valid) + " "  " notes = " + str(self.notes) + " "  "} " + "\n" + "}"
