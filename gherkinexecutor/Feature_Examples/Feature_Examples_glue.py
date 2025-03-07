
import unittest
from typing import List

class TemperatureCalculation:
    def __init__(self, f, c, notes):
        self.f = f
        self.c = c
        self.notes = notes

    def to_temperature_calculation_internal(self):
        return TemperatureCalculationInternal(self.f, self.c, self.notes)

    class Builder:
        def __init__(self):
            self.f = None
            self.c = None
            self.notes = None

        def f(self, f):
            self.f = f
            return self

        def c(self, c):
            self.c = c
            return self

        def notes(self, notes):
            self.notes = notes
            return self

        def build(self):
            return TemperatureCalculation(self.f, self.c, self.notes)

class ValueValid:
    def __init__(self, value, valid, notes):
        self.value = value
        self.valid = valid
        self.notes = notes

    class Builder:
        def __init__(self):
            self.value = None
            self.valid = None
            self.notes = None

        def value(self, value):
            self.value = value
            return self

        def valid(self, valid):
            self.valid = valid
            return self

        def notes(self, notes):
            self.notes = notes
            return self

        def build(self):
            return ValueValid(self.value, self.valid, self.notes)

class LabelValue:
    def __init__(self, iD, value):
        self.iD = iD
        self.value = value

    def to_label_value_internal(self):
        return LabelValueInternal(self.iD, self.value)

    class Builder:
        def __init__(self):
            self.iD = None
            self.value = None

        def iD(self, iD):
            self.iD = iD
            return self

        def value(self, value):
            self.value = value
            return self

        def build(self):
            return LabelValue(self.iD, self.value)

class FilterValue:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def to_filter_value_internal(self):
        return FilterValueInternal(self.name, self.value)

    class Builder:
        def __init__(self):
            self.name = None
            self.value = None

        def name(self, name):
            self.name = name
            return self

        def value(self, value):
            self.value = value
            return self

        def build(self):
            return FilterValue(self.name, self.value)

class ResultValue:
    def __init__(self, sum):
        self.sum = sum

    def to_result_value_internal(self):
        return ResultValueInternal(self.sum)

    class Builder:
        def __init__(self):
            self.sum = None

        def sum(self, sum):
            self.sum = sum
            return self

        def build(self):
            return ResultValue(self.sum)

class FeatureExamplesGlue:
    def __init__(self):
        self.solution = SolutionForListOfNumber()

    def log(self, value):
        try:
            with open("src/test/java/gherkinexecutor/Feature_Examples/log.txt", "a") as myLog:
                myLog.write(value + "\n")
        except IOError:
            print("**** Cannot write to log ")

    def Calculation_Convert_F_to_C(self, values: List[TemperatureCalculation]):
        print("---  Calculation_Convert_F_to_C")
        self.log("---  Calculation_Convert_F_to_C")
        self.log(str(values))
        for value in values:
            print(value)
            try:
                i = value.to_temperature_calculation_internal()
                c = TemperatureCalculations.convert_fahrenheit_to_celsius(i.f)
                assert i.c == c, i.notes
                print(i)
            except Exception as e:
                print(f"Argument Error {value} {TemperatureCalculationInternal.to_data_type_string()}")

    def Rule_ID_must_have_exactly_5_letters_and_begin_with_Q(self, values: List[ValueValid]):
        print("---  Rule_ID_must_have_exactly_5_letters_and_begin_with_Q")
        self.log("---  Rule_ID_must_have_exactly_5_letters_and_begin_with_Q")
        self.log(str(values))
        for value in values:
            print(value)
            expected = value.valid.lower() == "true"
            try:
                ID(value.value)
                if not expected:
                    assert False, f"Invalid value did not throw exception {value.value} {value.notes}"
            except Exception:
                if expected:
                    assert False, f"Valid value threw exception {value.value} {value.notes}"

    def Given_list_of_numbers(self, values: List[LabelValue]):
        print("---  Given_list_of_numbers")
        self.log("---  Given_list_of_numbers")
        self.log(str(values))
        for value in values:
            print(value)
            try:
                i = value.to_label_value_internal()
                print(i)
                self.solution.add(i)
            except Exception as e:
                print(f"Argument Error {value} {LabelValueInternal.to_data_type_string()}")

    def When_filtered_by_ID_with_value(self, values: List[List[str]]):
        print("---  When_filtered_by_ID_with_value")
        self.log("---  When_filtered_by_ID_with_value")
        self.log(str(values))
        id = values[0][0]
        print(f"ID is {id}")
        self.solution.set_filter_value(ID(id))

    def Then_sum_is(self, values: List[List[str]]):
        print("---  Then_sum_is")
        self.log("---  Then_sum_is")
        self.log(str(values))
        expected = int(values[0][0])
        print(f"    expecting {expected}")
        result = self.solution.sum()
        assert expected == result

    def When_filtered_by(self, values: List[FilterValue]):
        print("---  When_filtered_by")
        for value in values:
            print(value)
            try:
                i = value.to_filter_value_internal()
                print(f"Filter is {value.value}")
                self.solution.set_filter_value(ID(value.value))
            except Exception as e:
                print(f"Argument Error {value} {FilterValueInternal.to_data_type_string()}")

    def Then_result(self, values: List[ResultValue]):
        print("---  Then_result")
        for value in values:
            print(value)
            try:
                i = value.to_result_value_internal()
                actual = self.solution.sum()
                assert i.sum == actual
            except Exception as e:
                print(f"Argument Error {value} {ResultValueInternal.to_data_type_string()}")
