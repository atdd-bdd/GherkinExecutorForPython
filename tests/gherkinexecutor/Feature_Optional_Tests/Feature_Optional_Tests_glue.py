from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from tests.gherkinexecutor.Feature_Optional_Tests import *
from typing import List
import sys

class Feature_Optional_Tests_glue :
    DNCString = "?DNC?"

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def Given_This_will_always_be_run(self) -> None:
        print("---  " + "Given_This_will_always_be_run")
        self.log("---  " + "Given_This_will_always_be_run")

    def Given_This_may_be_run(self) -> None:
        print("---  " + "Given_This_may_be_run")
        self.log("---  " + "Given_This_may_be_run")

    def Given_This_will_be_run_if_tag(self) -> None:
        print("---  " + "Given_This_will_be_run_if_tag")
        self.log("---  " + "Given_This_will_be_run_if_tag")

