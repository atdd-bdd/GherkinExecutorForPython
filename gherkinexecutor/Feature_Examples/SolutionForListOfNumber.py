from gherkinexecutor.Feature_Examples.ID import ID


class SolutionForListOfNumber:
    def __init__(self):
        self.values = []
        self.filter_value = ID("Q0000")

    def add(self, value):
        self.values.append(value)

    def set_filter_value(self, value):
        self.filter_value = value

    def sum(self):
        total = 0
        for element in self.values:
            if element.iD == self.filter_value:
                total += element.value
        return total

# Assuming LabelValueInternal and ID classes are defined elsewhere
