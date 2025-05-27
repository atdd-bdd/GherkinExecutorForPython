class TicTacToeGame:
    def __init__(self):
        self.game_board = [[]]

    def set_board(self, value):
        self.game_board.clear()
        for row in value:
            self.game_board.append(list(row))

    def make_a_move(self, row, column, mark):
        print(f"Row {row} Col {column} Mark {mark}")
        self.game_board[row - 1][column - 1] = str(mark)

    def __str__(self):
        return self.list_of_list_to_string(self.game_board)

    @staticmethod
    def list_of_list_to_string(value):
        max_sizes = []
        for row in value:
            for column, cell in enumerate(row):
                if len(max_sizes) <= column:
                    max_sizes.append(0)
                if len(cell) > max_sizes[column]:
                    max_sizes[column] = len(cell)

        result = []
        for row in value:
            row_str = "|"
            for column, cell in enumerate(row):
                spaces = max_sizes[column] - len(cell) + 2
                row_str += f" {cell}{' ' * spaces}|"
            result.append(row_str)
        return "\n".join(result).strip()
