class ATestInternal:

    @staticmethod
    def to_data_type_string() -> str:
        return "ATestInternal {"
        + "int " 
        + "str " 
        + "float " 
        + "} "

    def to_ATest(self) -> ATest:
        return ATest(
         str(anInt)
        , str(aString)
        , str(aDouble)
        )

    def __init__(self,
         anInt: int
        , aString: str
        , aDouble: float
        ) -> None:
        self.anInt = anInt
        self.aString = aString
        self.aDouble = aDouble

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _ATestInternal = other
        return 
                ( _ATestInternal.anInt  ==  self.anInt)
                 and ( _ATestInternal.aString  ==  self.aString)
                 and ( _ATestInternal.aDouble  ==  self.aDouble)


            def __str__(self) -> str:
                return "{class_name} {{" + \
                    " anInt = " + str(self.anInt) + " " + \
            " aString = " + str(self.aString) + " " + \
            " aDouble = " + str(self.aDouble) + " " + \
            "} " + "\n" + "}"
