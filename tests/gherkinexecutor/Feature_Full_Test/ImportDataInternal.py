from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime
class ImportDataInternal:

    @staticmethod
    def to_data_type_string() -> str:
        return "ImportDataInternal {"
        + "datetime " 
        + "} "

    def to_ImportData(self) :
        from tests.gherkinexecutor.Feature_Full_Test.ImportData import ImportData
        return ImportData(
         str(self.myDate)
        )

    def __init__(self,
                myDate: datetime
                ) -> None:
        self.myDate = myDate

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _ImportDataInternal = other
        return  ( _ImportDataInternal.myDate == self.myDate)

    def __str__(self) -> str:
        return "{ImportDataInternal} {" + \
         " myDate = " + str(self.myDate) + " "  "} " + "\n"
