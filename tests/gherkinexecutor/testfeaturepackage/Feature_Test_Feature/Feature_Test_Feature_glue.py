from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from tests.gherkinexecutor.Feature_Test_Feature import *
from typing import List
import sys

class Feature_Test_Feature_glue :
    DNCString = "?DNC?"

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def Given_local_include(self, value: str) -> None:
        print("---  " + "Given_local_include")
        self.log("---  " + "Given_local_include")
        self.log(str(value))
        print(value)

    def Then_string_equals(self, value: str) -> None:
        print("---  " + "Then_string_equals")
        self.log("---  " + "Then_string_equals")
        self.log(str(value))
        print(value)

    def Given_global_include(self, value: str) -> None:
        print("---  " + "Given_global_include")
        self.log("---  " + "Given_global_include")
        self.log(str(value))
        print(value)

