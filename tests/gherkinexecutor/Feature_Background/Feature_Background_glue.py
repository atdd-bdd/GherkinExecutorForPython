from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from tests.gherkinexecutor.Feature_Background import *
from typing import List

class Feature_Background_glue :
    DNCString = "?DNC?"

    def __init__(self):
        self.background_value = ""
        self.cleanup_value = ""


    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def Given_Background_function_sets_a_value(self, values: List[List[str]]) -> None:
        print("---  " + "Given_Background_function_sets_a_value")
        self.log("---  " + "Given_Background_function_sets_a_value")
        self.log(str(values))
        print("input is " + values[0][0])
        self.background_value = values[0][0]

    def Given_value_for_cleanup_should_be_set_to(self, values: List[List[str]]) -> None:
        print("---  " + "Given_value_for_cleanup_should_be_set_to")
        self.log("---  " + "Given_value_for_cleanup_should_be_set_to")
        self.log(str(values))
        print("input is " + values[0][0])
        print(" to cleanup " + self.cleanup_value)
        self.cleanup_value = values[0][0]

    def Given_a_regular_function(self) -> None:
        print("---  " + "Given_a_regular_function")
        self.log("---  " + "Given_a_regular_function")

    def Then_background_should_set_value_to(self, values: List[List[str]]) -> None:
        print("---  " + "Then_background_should_set_value_to")
        self.log("---  " + "Then_background_should_set_value_to")
        self.log(str(values))
        print(values[0][0])
        print(" to background is " + self.background_value)

        assert self.background_value == values[0][0]

    def And_set_a_value_for_cleanup(self, values: List[List[str]]) -> None:
        print("---  " + "And_set_a_value_for_cleanup")
        self.log("---  " + "And_set_a_value_for_cleanup")
        self.log(str(values))


