

class MoveInternal:

    @staticmethod
    def to_data_type_string() -> str:
        return "MoveInternal {"
        + "int " 
        + "int " 
        + "str " 
        + "} "

    def to_Move(self) :
        from tests.gherkinexecutor.Feature_Tic_Tac_Toe_Game.Move import Move
        return Move(
         str(self.row)
        , str(self.column)
        , str(self.mark)
        )

    def __init__(self,
                row: int
               , column: int
               , mark: str
                ) -> None:
        self.row = row
        self.column = column
        self.mark = mark

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, self.__class__):
            return False
        _MoveInternal = other
        return  ( _MoveInternal.row == self.row)  and ( _MoveInternal.column == self.column)  and ( _MoveInternal.mark == self.mark)

    def __str__(self) -> str:
        return "{MoveInternal} {" + \
         " row = " + str(self.row) + " "  " column = " + str(self.column) + " "  " mark = " + str(self.mark) + " "  "} " + "\n"
