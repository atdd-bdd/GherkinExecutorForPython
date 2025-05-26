import re

from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from tests.gherkinexecutor.Feature_Json import *
from typing import List
import sys

class Feature_Json_glue :
    DNCString = "?DNC?"

    def __init__(self):
        self.original_table = ""
        self.original_string = ""
    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def Given_one_object_is(self, values: List[SimpleClass]) -> None:
        print("---  " + "Given_one_object_is")
        self.log("---  " + "Given_one_object_is")
        self.log(str(values))
        for value in values:
            print(value)
        self.original_table = values

    def Then_Json_should_be(self, value: str) -> None:
        print("---  " + "Then_Json_should_be")
        self.log("---  " + "Then_Json_should_be")
        self.log(str(value))
        print(value)
        result = self.original_table[0].to_json()
        assert value == result
    def Given_Json_is(self, value: str) -> None:
        print("---  " + "Given_Json_is")
        self.log("---  " + "Given_Json_is")
        self.log(str(value))
        print(value)
        self.original_string = value

    def Then_the_converted_object_is(self, values: List[SimpleClass]) -> None:
        print("---  " + "Then_the_converted_object_is")
        self.log("---  " + "Then_the_converted_object_is")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_SimpleClassInternal()
        result = SimpleClass.from_json(self.original_string)

        assert result == values[0]
    def Given_a_table_is(self, values: List[SimpleClass]) -> None:
        print("---  " + "Given_a_table_is")
        self.log("---  " + "Given_a_table_is")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_SimpleClassInternal()
        self.original_table = values
    def Then_Json_for_table_should_be(self, value: str) -> None:
        print("---  " + "Then_Json_for_table_should_be")
        self.log("---  " + "Then_Json_for_table_should_be")
        self.log(str(value))
        print(value)
        result = SimpleClass.list_to_json(self.original_table)
        print("Here in list to jason")
        print(result)
        print(value)
        result = re.sub(r"\s+","",result)
        value1 = re.sub(r"\s+", "", value)
        print(result)
        print(value1)
        assert result == value1
    def Given_Json_for_table_is(self, value: str) -> None:
        print("---  " + "Given_Json_for_table_is")
        self.log("---  " + "Given_Json_for_table_is")
        self.log(str(value))
        print(value)
        self.original_string = value

    def Then_the_converted_table_should_be(self, values: List[SimpleClass]) -> None:
        print("---  " + "Then_the_converted_table_should_be")
        self.log("---  " + "Then_the_converted_table_should_be")
        self.log(str(values))
        for value in values:
            print(value)
        result = SimpleClass.list_from_json(self.original_string)
        assert result == values

