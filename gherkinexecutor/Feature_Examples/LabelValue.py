
import json

from gherkinexecutor.Feature_Examples.LabelValueInternal import LabelValueInternal
from gherkinexecutor.Feature_Examples.ID import ID


class LabelValue:
    def __init__(self, iD="", value="0"):
        self.iD = iD
        self.value = value

    def __eq__(self, other):
        if self is other:
            return True
        if other is None or not isinstance(other, LabelValue):
            return False
        if self.iD != "?DNC?" and other.iD != "?DNC?" and self.iD != other.iD:
            return False
        if self.value != "?DNC?" and other.value != "?DNC?" and self.value != other.value:
            return False
        return True

    def __str__(self):
        return f"LabelValue {{iD = {self.iD} value = {self.value} }}\n"

    def to_json(self):
        return json.dumps({"iD": self.iD, "value": self.value})

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        instance = LabelValue()
        instance.iD = data.get("iD", "")
        instance.value = data.get("value", "0")
        return instance

    @staticmethod
    def list_to_json(list_of_label_values):
        return json.dumps([label_value.to_json() for label_value in list_of_label_values])

    @staticmethod
    def list_from_json(json_str):
        list_of_label_values = json.loads(json_str)
        return [LabelValue.from_json(json.dumps(item)) for item in list_of_label_values]

    class Builder:
        def __init__(self):
            self.iD = ""
            self.value = "0"

        def setiD(self, iD):
            self.iD = iD
            return self

        def setvalue(self, value):
            self.value = value
            return self

        def set_compare(self):
            self.iD = "?DNC?"
            self.value = "?DNC?"
            return self

        def build(self):
            return LabelValue(self.iD, self.value)

    def to_label_value_internal(self):
        return LabelValueInternal(ID(self.iD), int(self.value))

# Assuming LabelValueInternal and ID classes are defined elsewhere
