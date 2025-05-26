from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
class ATest:
    def __init__(self,
                  anInt: str = "0"
                 , aString: str = "^"
                 , aDouble: str = "1.2"
        ) -> None:
        self.anInt = anInt
        self.aString = aString
        self.aDouble = aDouble
    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _ATest = other
        _ATest:ATest=  o
        result1 = True;
        if (
             not self.anInt == "?DNC?"
                and not _ATest.anInt == "?DNC?"):
                if (not  _ATest.anInt== self.anInt):
                    result1 = False
                result1 = False
        if (
             not self.aString == "?DNC?"
                and not _ATest.aString == "?DNC?"):
                if (not  _ATest.aString== self.aString):
                    result1 = False
                result1 = False
        if (
             not self.aDouble == "?DNC?"
                and not _ATest.aDouble == "?DNC?"):
                if (not  _ATest.aDouble== self.aDouble):
                    result1 = False
                result1 = False
        return result1

    def __str__(self) -> str:
        return "{ATest} {{" + \
         " anInt = " + str(self.anInt) + " "  " aString = " + str(self.aString) + " "  " aDouble = " + str(self.aDouble) + " "  "} " + "\n" + "}"

    def to_ATestInternal(self): 
        from tests.gherkinexecutor.Feature_Simple_Test.ATestInternal import ATestInternal
        return ATestInternal(
            int(self.anInt)
            ,self.aString
            ,float(self.aDouble)
        )

    class Builder:
        def __init__(self) -> None:
            self.anInt = "0"
            self.aString = "^"
            self.aDouble = "1.2"

        def setAnint(self, anInt: str) -> 'Builder':
            self.anInt = anInt
            return self

        def setAstring(self, aString: str) -> 'Builder':
            self.aString = aString
            return self

        def setAdouble(self, aDouble: str) -> 'Builder':
            self.aDouble = aDouble
            return self

        def set_compare(self) -> 'Builder':
            self.anInt = "?DNC?"
            self.aString = "?DNC?"
            self.aDouble = "?DNC?"
            return self

        def build(self):
            return ATest(
                self.anInt
                ,self.aString
                ,self.aDouble
            )
