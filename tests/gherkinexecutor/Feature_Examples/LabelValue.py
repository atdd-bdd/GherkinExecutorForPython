from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
class LabelValue:
    def __init__(self,
                  iD: str = ""
                 , value: str = "0"
        ) -> None:
        self.iD = iD
        self.value = value
    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _LabelValue = other
        _LabelValue:LabelValue=  o
        result1 = True;
        if (
             not self.iD == "?DNC?"
                and not _LabelValue.iD == "?DNC?"):
                if (not  _LabelValue.iD== self.iD):
                    result1 = False
                result1 = False
        if (
             not self.value == "?DNC?"
                and not _LabelValue.value == "?DNC?"):
                if (not  _LabelValue.value== self.value):
                    result1 = False
                result1 = False
        return result1

    def __str__(self) -> str:
        return "{LabelValue} {{" + \
         " iD = " + str(self.iD) + " "  " value = " + str(self.value) + " "  "} " + "\n" + "}"
    def to_LabelValueInternal(self): 
        from tests.gherkinexecutor.Feature_Examples.LabelValueInternal import LabelValueInternal
        return LabelValueInternal(
            ID(self.iD)
            ,int(self.value)
        )

    class Builder:
        def __init__(self) -> None:
            self.iD = ""
            self.value = "0"

        def setId(self, iD: str) -> 'Builder':
            self.iD = iD
            return self

        def setValue(self, value: str) -> 'Builder':
            self.value = value
            return self

        def set_compare(self) -> 'Builder':
            self.iD = "?DNC?"
            self.value = "?DNC?"
            return self

        def build(self):
            return LabelValue(
                self.iD
                ,self.value
            )
