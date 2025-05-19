from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from tests.gherkinexecutor.SolutionForListOfNumber import SolutionForListOfNumber
from tests.gherkinexecutor.Feature_Examples.FandC import FandC
from tests.gherkinexecutor.Feature_Examples.FandCInternal import FandCInternal
from tests.gherkinexecutor.Feature_Examples.ValueValid import ValueValid
from tests.gherkinexecutor.Feature_Examples.ValueValidInternal import ValueValidInternal
from tests.gherkinexecutor.Feature_Examples.FilterValue import FilterValue
from tests.gherkinexecutor.Feature_Examples.FilterValueInternal import FilterValueInternal
from tests.gherkinexecutor.Feature_Examples.ResultValue import ResultValue
from tests.gherkinexecutor.Feature_Examples.ResultValueInternal import ResultValueInternal
from tests.gherkinexecutor.Feature_Examples.LabelValue import LabelValue
from tests.gherkinexecutor.Feature_Examples.LabelValueInternal import LabelValueInternal

from typing import List


class Feature_Examples_glue:
    DNCString = "?DNC?"

    def __init__(self):
        self.solution = SolutionForListOfNumber()

    def Calculation_Convert_F_to_C(self, values: List[FandC]) -> None:
        print("---  " + "Calculation_Convert_F_to_C")
        for value in values:
            print(value)
            try:
                i = value.to_FandCInternal()
                c = TemperatureCalculations.convert_fahrenheit_to_celsius(i.f)
                assert i.c == c, i.notes
                print(i)
            except Exception as e:
                print(e)
                print(f"Argument Error  1 {value} {FandCInternal.to_data_type_string()}")

    def Rule_ID_must_have_exactly_5_letters_and_begin_with_Q(self, values: List[ValueValid]) -> None:
        print("---  " + "Rule_ID_must_have_exactly_5_letters_and_begin_with_Q")
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


    def Given_list_of_numbers(self, values: List[LabelValue]) -> None:
        print("---  " + "Given_list_of_numbers")
        for value in values:
            print(value)
            try:
                i = value.to_LabelValueInternal()
                print(i)
                self.solution.add(i)
            except Exception as e:
                print(e)
                print(f"Argument Error 2 {value} {LabelValueInternal.to_data_type_string()}")

    def When_filtered_by_ID_with_value(self, values: List[List[str]]) -> None:
        print("---  " + "When_filtered_by_ID_with_value")
        id = values[0][0]
        print(f"ID is {id}")
        self.solution.set_filter_value(ID(id))


    def Then_sum_is(self, values: List[List[str]]) -> None:
        print("---  " + "Then_sum_is")
        for value in values:
            print(value)
            # Add calls to production code and asserts
        expected = int(values[0][0])
        print(f"    expecting {expected}")
        result = self.solution.sum()
        assert expected == result


    def When_filtered_by(self, values: List[FilterValue]) -> None:
        print("---  " + "When_filtered_by")
        for value in values:
            print(value)
            try:
                i = value.to_FilterValueInternal()
                print(f"Filter is {value.value}")
                self.solution.set_filter_value(ID(value.value))
            except Exception as e:
                print(e)
                print(f"Argument Error 3 {value} {FilterValueInternal.to_data_type_string()}")

    def Then_result(self, values: List[ResultValue]) -> None:
        print("---  " + "Then_result")
        for value in values:
            print(value)
            try:
                i = value.to_ResultValueInternal()
                actual = self.solution.sum()
                assert i.sum == actual
            except Exception as e:
                print(e)
                print(f"Argument Error 4 {value} {ResultValueInternal.to_data_type_string()}")
