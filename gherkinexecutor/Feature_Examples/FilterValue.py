
import json

class FilterValue:
    def __init__(self, name="", value="Q0000"):
        self.name = name
        self.value = value

    def __eq__(self, other):
        if self is other:
            return True
        if other is None or not isinstance(other, FilterValue):
            return False
        if self.name != "?DNC?" and other.name != "?DNC?" and self.name != other.name:
            return False
        if self.value != "?DNC?" and other.value != "?DNC?" and self.value != other.value:
            return False
        return True

    def __str__(self):
        return f"FilterValue {{name = {self.name} value = {self.value} }}\n"

    def to_json(self):
        return json.dumps({"name": self.name, "value": self.value})

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        instance = FilterValue()
        instance.name = data.get("name", "")
        instance.value = data.get("value", "Q0000")
        return instance

    @staticmethod
    def list_to_json(list_of_filter_values):
        return json.dumps([filter_value.to_json() for filter_value in list_of_filter_values])

    @staticmethod
    def list_from_json(json_str):
        list_of_filter_values = json.loads(json_str)
        return [FilterValue.from_json(json.dumps(item)) for item in list_of_filter_values]

    class Builder:
        def __init__(self):
            self.name = ""
            self.value = "Q0000"

        def name(self, name):
            self.name = name
            return self

        def value(self, value):
            self.value = value
            return self

        def set_compare(self):
            self.name = "?DNC?"
            self.value = "?DNC?"
            return self

        def build(self):
            return FilterValue(self.name, self.value)

    def to_filter_value_internal(self):
        return FilterValueInternal(self.name, ID(self.value))

# Assuming FilterValueInternal and ID classes are defined elsewhere
