from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from tests.gherkinexecutor.Feature_Include import *
from typing import List
import sys

class Feature_Include_glue :
    DNCString = "?DNC?"

    def __init__(self):
        self.string_original = ""
        self.table_original = ""
    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def Given_a_string_include(self, value: str) -> None:
        print("---  " + "Given_a_string_include")
        self.log("---  " + "Given_a_string_include")
        self.log(str(value))
        print(value)
        self.string_original = value

    def Then_should_be_equal_to(self, value: str) -> None:
        print("---  " + "Then_should_be_equal_to")
        self.log("---  " + "Then_should_be_equal_to")
        self.log(str(value))
        print(value)
        assert self.string_original == value
    def Given_a_table(self, values: List[CSVContents]) -> None:
        print("---  " + "Given_a_table")
        self.log("---  " + "Given_a_table")
        self.log(str(values))
        for value in values:
            print(value)
        self.table_original = values

    def Then_Should_be_equal_to_table(self, values: List[CSVContents]) -> None:
        print("---  " + "Then_Should_be_equal_to_table")
        self.log("---  " + "Then_Should_be_equal_to_table")
        self.log(str(values))
        for value in values:
            print(value)
        assert self.table_original == values

