from datetime import datetime
from tests.gherkinexecutor.Feature_Import.Color import Color


class ImportDataInternal:

    @staticmethod
    def to_data_type_string() -> str:
        return "ImportDataInternal {"
        + "datetime " 
        + "Color " 
        + "} "

    def to_ImportData(self):
        from tests.gherkinexecutor.Feature_Import.ImportData import ImportData
        return ImportData(
         str(self.myDate)
        , str(self.color)
        )

    def __init__(self,
                myDate: datetime
               , color: Color
                ) -> None:
        self.myDate = myDate
        self.color = color

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _ImportDataInternal = other
        return  ( _ImportDataInternal.myDate == self.myDate)  and ( _ImportDataInternal.color == self.color)


    def __str__(self) -> str:
        return "{ImportDataInternal} {" + \
         " myDate = " + str(self.myDate) + " "  " color = " + str(self.color) + " "  "} " + "\n"
