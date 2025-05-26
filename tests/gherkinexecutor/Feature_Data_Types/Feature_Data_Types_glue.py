from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from tests.gherkinexecutor.Feature_Data_Types import *
from typing import List


class Feature_Data_Types_glue:
    DNCString = "?DNC?"

    def __init__(self):
        self.original = []
        self.expected = []

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)

    def Given_type_values_are(self, values: List[SomeTypes]) -> None:
        print("---  " + "Given_type_values_are")
        self.log("---  " + "Given_type_values_are")
        self.log(str(values))
        for value in values:
            print(value)
            # Add calls to production code and asserts
            i = value.to_SomeTypesInternal()
            self.original.append(i)
            print(i)

    def Then_this_should_be_equal(self, values: List[SomeTypes]) -> None:
        print("---  " + "Then_this_should_be_equal")
        self.log("---  " + "Then_this_should_be_equal")
        self.log(str(values))
        for value in values:
            print(value)
            # Add calls to production code and asserts
            i = value.to_SomeTypesInternal()
            self.expected.append(i)
            print(i)
        assert self.original == self.expected

