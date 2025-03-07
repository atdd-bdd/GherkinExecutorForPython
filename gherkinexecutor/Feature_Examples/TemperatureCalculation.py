from gherkinexecutor.Feature_Examples.TemperatureCalculationInternal import TemperatureCalculationInternal
import json

class TemperatureCalculation:
    def __init__(self, f="0", c="0", notes=""):
        self.f = f
        self.c = c
        self.notes = notes

    def __eq__(self, other):
        if self is other:
            return True
        if other is None or not isinstance(other, TemperatureCalculation):
            return False
        if self.f != "?DNC?" and other.f != "?DNC?" and self.f != other.f:
            return False
        if self.c != "?DNC?" and other.c != "?DNC?" and self.c != other.c:
            return False
        if self.notes != "?DNC?" and other.notes != "?DNC?" and self.notes != other.notes:
            return False
        return True

    def __str__(self):
        return f"TemperatureCalculation {{f = {self.f} c = {self.c} notes = {self.notes} }}\n"

    def to_json(self):
        return json.dumps({"f": self.f, "c": self.c, "notes": self.notes})

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        instance = TemperatureCalculation()
        instance.f = data.get("f", "0")
        instance.c = data.get("c", "0")
        instance.notes = data.get("notes", "")
        return instance

    @staticmethod
    def list_to_json(list_of_temperature_calculations):
        return json.dumps([temperature_calculation.to_json() for temperature_calculation in list_of_temperature_calculations])

    @staticmethod
    def list_from_json(json_str):
        list_of_temperature_calculations = json.loads(json_str)
        return [TemperatureCalculation.from_json(json.dumps(item)) for item in list_of_temperature_calculations]

    class Builder:
        def __init__(self):
            self.f = "0"
            self.c = "0"
            self.notes = ""

        def setf(self, f):
            self.f = f
            return self

        def setc(self, c):
            self.c = c
            return self

        def setnotes(self, notes):
            self.notes = notes
            return self

        def set_compare(self):
            self.f = "?DNC?"
            self.c = "?DNC?"
            self.notes = "?DNC?"
            return self

        def build(self):
            return TemperatureCalculation(self.f, self.c, self.notes)

    def to_temperature_calculation_internal(self):
        return TemperatureCalculationInternal(int(self.f), int(self.c), self.notes)

# Assuming TemperatureCalculationInternal class is defined elsewhere
