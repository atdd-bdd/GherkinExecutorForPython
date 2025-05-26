from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from tests.gherkinexecutor.Feature_Data_Definition_Error import *
from typing import List
import sys

class Feature_Data_Definition_Error_glue :
    DNCString = "?DNC?"

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
            i = value.to_ATestInternal()

    def Given_table_is_bad_initializer(self, values: List[ATestBad]) -> None:
        print("---  " + "Given_table_is_bad_initializer")
        self.log("---  " + "Given_table_is_bad_initializer")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_ATestBadInternal()

