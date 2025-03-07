import json

class ValueValid:
    def __init__(self, value="0", valid="false", notes=""):
        self.value = value
        self.valid = valid
        self.notes = notes

    def __eq__(self, other):
        if self is other:
            return True
        if other is None or not isinstance(other, ValueValid):
            return False
        if self.value != "?DNC?" and other.value != "?DNC?" and self.value != other.value:
            return False
        if self.valid != "?DNC?" and other.valid != "?DNC?" and self.valid != other.valid:
            return False
        if self.notes != "?DNC?" and other.notes != "?DNC?" and self.notes != other.notes:
            return False
        return True

    def __str__(self):
        return f"ValueValid {{value = {self.value} valid = {self.valid} notes = {self.notes} }}\n"

    def to_json(self):
        return json.dumps({"value": self.value, "valid": self.valid, "notes": self.notes})

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        instance = ValueValid()
        instance.value = data.get("value", "0")
        instance.valid = data.get("valid", "false")
        instance.notes = data.get("notes", "")
        return instance

    @staticmethod
    def list_to_json(list_of_value_valids):
        return json.dumps([value_valid.to_json() for value_valid in list_of_value_valids])

    @staticmethod
    def list_from_json(json_str):
        list_of_value_valids = json.loads(json_str)
        return [ValueValid.from_json(json.dumps(item)) for item in list_of_value_valids]

    class Builder:
        def __init__(self):
            self.value = "0"
            self.valid = "false"
            self.notes = ""

        def setvalue(self, value):
            self.value = value
            return self

        def setvalid(self, valid):
            self.valid = valid
            return self

        def setnotes(self, notes):
            self.notes = notes
            return self

        def set_compare(self):
            self.value = "?DNC?"
            self.valid = "?DNC?"
            self.notes = "?DNC?"
            return self

        def build(self):
            return ValueValid(self.value, self.valid, self.notes)

    def to_value_valid_internal(self):
        return ValueValidInternal(self.value, self.valid.lower() == "true", self.notes)

# Assuming ValueValidInternal class is defined elsewhere
