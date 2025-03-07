class ResultValueInternal:
    def __init__(self, sum):
        self.sum = sum

    @staticmethod
    def to_data_type_string():
        return "ResultValueInternal { Integer }"

    def to_result_value(self):
        return ResultValue(str(self.sum))

    def __eq__(self, other):
        if self is other:
            return True
        if other is None or not isinstance(other, ResultValueInternal):
            return False
        return self.sum == other.sum

    def __str__(self):
        return f"ResultValueInternal {{ sum = {self.sum} }}\n"

# Assuming ResultValue class is defined elsewhere
