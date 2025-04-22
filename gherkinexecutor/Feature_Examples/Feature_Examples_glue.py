
import unittest
from typing import List

from gherkinexecutor.Feature_Examples.TemperatureCalculation import TemperatureCalculation
from gherkinexecutor.Feature_Examples.FilterValue import FilterValue
from gherkinexecutor.Feature_Examples.ResultValue import ResultValue
from gherkinexecutor.Feature_Examples.LabelValue import LabelValue
from gherkinexecutor.Feature_Examples.ValueValid import ValueValid
from gherkinexecutor.Feature_Examples.TemperatureCalculations import TemperatureCalculations
from gherkinexecutor.Feature_Examples.TemperatureCalculationInternal import TemperatureCalculationInternal
from gherkinexecutor.Feature_Examples.ID import ID
from gherkinexecutor.Feature_Examples.SolutionForListOfNumber import SolutionForListOfNumber
from gherkinexecutor.Feature_Examples.LabelValueInternal import LabelValueInternal
from gherkinexecutor.Feature_Examples.FilterValueInternal import FilterValueInternal
from gherkinexecutor.Feature_Examples.ResultValueInternal import ResultValueInternal


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
                print(e)
                print(f"Argument Error  1 {value} {TemperatureCalculationInternal.to_data_type_string()}")

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
                print(e)
                print(f"Argument Error 2 {value} {LabelValueInternal.to_data_type_string()}")

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
                print(e)
                print(f"Argument Error 3 {value} {FilterValueInternal.to_data_type_string()}")

    def Then_result(self, values: List[ResultValue]):
        print("---  Then_result")
        for value in values:
            print(value)
            try:
                i = value.to_result_value_internal()
                actual = self.solution.sum()
                assert i.sum == actual
            except Exception as e:
                print(e)
                print(f"Argument Error 4 {value} {ResultValueInternal.to_data_type_string()}")
