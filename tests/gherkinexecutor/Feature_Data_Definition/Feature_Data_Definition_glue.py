from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from tests.gherkinexecutor.Feature_Data_Definition import *
from typing import List
import sys
class Feature_Data_Definition_glue :
    DNCString = "?DNC?"

    def __init__(self):
        self.original = ""
        self.comparison = ""
    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def Given_table_is(self, values: List[ATest]) -> None:
        print("---  " + "Given_table_is")
        self.log("---  " + "Given_table_is")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
        self.original = values

    def When_compared_to(self, values: List[ATest]) -> None:
        print("---  " + "When_compared_to")
        self.log("---  " + "When_compared_to")
        self.log(str(values))
        for value in values:
            print(value)
        self.comparison = values
    def Then_result_is(self, values: List[List[str]]) -> None:
        print("---  " + "Then_result_is")
        self.log("---  " + "Then_result_is")
        self.log(str(values))
        expected = bool(values[0][0])
        result = self.original == self.comparison
        count = 0
        print (len(self.comparison))
        for value in self.original:
            print(value)
            compare = self.comparison[count]
            print(compare)
            result = value == compare
            print(result)

    def Given_these_are_all_the_types(self, values: List[AllTypes]) -> None:
        print("---  " + "Given_these_are_all_the_types")
        self.log("---  " + "Given_these_are_all_the_types")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_AllTypesInternal()



