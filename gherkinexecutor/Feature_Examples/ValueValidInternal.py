class ValueValidInternal:
    def __init__(self, value, valid, notes):
        self.value = value
        self.valid = valid
        self.notes = notes

    @staticmethod
    def to_data_type_string():
        return "ValueValidInternal { String Boolean String }"

    def to_value_valid(self):
        return ValueValid(self.value, str(self.valid), self.notes)

    def __eq__(self, other):
        if self is other:
            return True
        if other is None or not isinstance(other, ValueValidInternal):
            return False
        return self.value == other.value and self.valid == other.valid and self.notes == other.notes

    def __str__(self):
        return f"ValueValidInternal {{ value = {self.value} valid = {self.valid} notes = {self.notes} }}\n"

# Assuming ValueValid class is defined elsewhere
