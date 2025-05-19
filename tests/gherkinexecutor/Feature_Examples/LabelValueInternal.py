from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
class LabelValueInternal:

    @staticmethod
    def to_data_type_string() -> str:
        return "LabelValueInternal {"
        + "ID " 
        + "int " 
        + "} "

    def to_LabelValue(self) :
        from tests.gherkinexecutor.Feature_Examples.LabelValue import LabelValue
        return LabelValue(
         str(self.iD)
        , str(self.value)
        )

    def __init__(self,
         iD: ID
        , value: int
        ) -> None:
        self.iD = iD
        self.value = value

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _LabelValueInternal = other
        return  ( _LabelValueInternal.iD == self.iD)  and ( _LabelValueInternal.value  ==  self.value)


    def __str__(self) -> str:
        return "{LabelValueInternal} {{" + \
         " iD = " + str(self.iD) + " "  " value = " + str(self.value) + " "  "} " + "\n" + "}"
