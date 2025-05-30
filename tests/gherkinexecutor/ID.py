
class ID:
    def __init__(self, value):
        if len(value) < 5:
            raise ValueError("Too short")
        if len(value) > 5:
            raise ValueError("Too long")
        if value[0] != 'Q':
            raise ValueError("Must begin with Q")
        self.value = value

    # Alternative validation method
    # def is_valid(self):
    #     if len(self.value) < 5:
    #         return False
    #     if len(self.value) > 5:
    #         return False
    #     if self.value[0] != 'Q':
    #         return False
    #     return True

    def __eq__(self, other):
        if self is other:
            return True
        if other is None or not isinstance(other, ID):
            return False
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return f"ID{{value='{self.value}'}}"
