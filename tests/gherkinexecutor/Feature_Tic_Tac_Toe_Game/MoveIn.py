
class MoveIn:
    def __init__(self, row="0", column="0", mark="^"):
        self.row = row
        self.column = column
        self.mark = mark

    @classmethod
    def from_string(cls, move_string):
        parts = move_string.split(",")
        if len(parts) == 3:
            return cls(parts[0], parts[1], parts[2])
        else:
            raise ValueError("Invalid move string format")

