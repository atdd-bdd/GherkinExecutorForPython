class TemperatureCalculationInternal:
    def __init__(self, f, c, notes):
        self.f = f
        self.c = c
        self.notes = notes

    @staticmethod
    def to_data_type_string():
        return "TemperatureCalculationInternal { Integer Integer String }"

    def to_temperature_calculation(self):
        return TemperatureCalculation(str(self.f), str(self.c), self.notes)

    def __eq__(self, other):
        if self is other:
            return True
        if other is None or not isinstance(other, TemperatureCalculationInternal):
            return False
        return self.f == other.f and self.c == other.c and self.notes == other.notes

    def __str__(self):
        return f"TemperatureCalculationInternal {{ f = {self.f} c = {self.c} notes = {self.notes} }}\n"

# Assuming TemperatureCalculation class is defined elsewhere

