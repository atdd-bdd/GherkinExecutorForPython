
class FilterValueInternal:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    @staticmethod
    def to_data_type_string():
        return "FilterValueInternal { String ID }"

    def to_filter_value(self):
        return FilterValue(self.name, str(self.value))

    def __eq__(self, other):
        if self is other:
            return True
        if other is None or not isinstance(other, FilterValueInternal):
            return False
        return self.name == other.name and self.value == other.value

    def __str__(self):
        return f"FilterValueInternal {{ name = {self.name} value = {self.value} }}\n"

# Assuming FilterValue and ID classes are defined elsewhere
