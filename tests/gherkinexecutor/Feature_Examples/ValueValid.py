from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
class ValueValid:
    def __init__(self,
                  value: str = "0"
                 , valid: str = "false"
                 , notes: str = ""
        ) -> None:
        self.value = value
        self.valid = valid
        self.notes = notes
    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _ValueValid = other
        _ValueValid:ValueValid=  o
        result1 = True;
        if (
             not self.value == "?DNC?"
                and not _ValueValid.value == "?DNC?"):
                if (not  _ValueValid.value== self.value):
                    result1 = False
                result1 = False
        if (
             not self.valid == "?DNC?"
                and not _ValueValid.valid == "?DNC?"):
                if (not  _ValueValid.valid== self.valid):
                    result1 = False
                result1 = False
        if (
             not self.notes == "?DNC?"
                and not _ValueValid.notes == "?DNC?"):
                if (not  _ValueValid.notes== self.notes):
                    result1 = False
                result1 = False
        return result1

    def __str__(self) -> str:
        return "{ValueValid} {{" + \
         " value = " + str(self.value) + " "  " valid = " + str(self.valid) + " "  " notes = " + str(self.notes) + " "  "} " + "\n" + "}"

    def to_ValueValidInternal(self): 
        from tests.gherkinexecutor.Feature_Examples.ValueValidInternal import ValueValidInternal
        return ValueValidInternal(
            self.value
            ,bool(self.valid)
            ,self.notes
        )

    class Builder:
        def __init__(self) -> None:
            self.value = "0"
            self.valid = "false"
            self.notes = ""

        def setValue(self, value: str) -> 'Builder':
            self.value = value
            return self

        def setValid(self, valid: str) -> 'Builder':
            self.valid = valid
            return self

        def setNotes(self, notes: str) -> 'Builder':
            self.notes = notes
            return self

        def set_compare(self) -> 'Builder':
            self.value = "?DNC?"
            self.valid = "?DNC?"
            self.notes = "?DNC?"
            return self

        def build(self):
            return ValueValid(
                self.value
                ,self.valid
                ,self.notes
            )
