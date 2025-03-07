
class LabelValueInternal:
    def __init__(self, iD, value):
        self.iD = iD
        self.value = value

    @staticmethod
    def to_data_type_string():
        return "LabelValueInternal { ID Integer }"

    def to_label_value(self):
        return LabelValue(self.iD.__str__(), str(self.value))

    def __eq__(self, other):
        if self is other:
            return True
        if other is None or not isinstance(other, LabelValueInternal):
            return False
        return self.iD == other.iD and self.value == other.value

    def __str__(self):
        return f"LabelValueInternal {{ iD = {self.iD} value = {self.value} }}\n"

# Assuming LabelValue and ID classes are defined elsewhere
