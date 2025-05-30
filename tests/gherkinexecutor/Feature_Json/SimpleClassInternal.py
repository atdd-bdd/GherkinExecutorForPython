

class SimpleClassInternal:

    @staticmethod
    def to_data_type_string() -> str:
        return "SimpleClassInternal {"
        + "int " 
        + "str " 
        + "} "

    def to_SimpleClass(self) :
        from tests.gherkinexecutor.Feature_Json.SimpleClass import SimpleClass
        return SimpleClass(
         str(self.anInt)
        , str(self.aString)
        )

    def __init__(self,
                anInt: int
               , aString: str
                ) -> None:
        self.anInt = anInt
        self.aString = aString

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _SimpleClassInternal = other
        return  ( _SimpleClassInternal.anInt == self.anInt)  and ( _SimpleClassInternal.aString == self.aString)

    def __str__(self) -> str:
        return "{SimpleClassInternal} {" + \
         " anInt = " + str(self.anInt) + " "  " aString = " + str(self.aString) + " "  "} " + "\n"
