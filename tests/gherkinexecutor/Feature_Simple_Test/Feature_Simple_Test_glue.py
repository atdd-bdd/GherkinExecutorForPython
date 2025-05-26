from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from tests.gherkinexecutor.Feature_Simple_Test import *
from typing import List


class Feature_Simple_Test_glue:
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

