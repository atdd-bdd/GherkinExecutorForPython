from gherkinexecutor.Feature_Examples.ResultValueInternal import ResultValueInternal
import json

class ResultValue:
    def __init__(self, sum=""):
        self.sum = sum

    def __eq__(self, other):
        if self is other:
            return True
        if other is None or not isinstance(other, ResultValue):
            return False
        if self.sum != "?DNC?" and other.sum != "?DNC?" and self.sum != other.sum:
            return False
        return True

    def __str__(self):
        return f"ResultValue {{sum = {self.sum} }}\n"

    def to_json(self):
        return json.dumps({"sum": self.sum})

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        instance = ResultValue()
        instance.sum = data.get("sum", "")
        return instance

    @staticmethod
    def list_to_json(list_of_result_values):
        return json.dumps([result_value.to_json() for result_value in list_of_result_values])

    @staticmethod
    def list_from_json(json_str):
        list_of_result_values = json.loads(json_str)
        return [ResultValue.from_json(json.dumps(item)) for item in list_of_result_values]

    class Builder:
        def __init__(self):
            self.sum = ""

        def setsum(self, sum):
            self.sum = sum
            return self

        def set_compare(self):
            self.sum = "?DNC?"
            return self

        def build(self):
            return ResultValue(self.sum)

    def to_result_value_internal(self):
        return ResultValueInternal(int(self.sum))

# Assuming ResultValueInternal class is defined elsewhere
