from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from tests.gherkinexecutor.Feature_Tables_and_Strings import *
from typing import List
import sys

class Feature_Tables_and_Strings_glue :
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
    

    def Star_A_multiline_string_to_a_string(self, value: str) -> None:
        print("---  " + "Star_A_multiline_string_to_a_string")
        self.log("---  " + "Star_A_multiline_string_to_a_string")
        self.log(str(value))
        print(value)

    def Star_A_multiline_string_to_a_List_of_String(self, values: List[str]) -> None:
        print("---  " + "Star_A_multiline_string_to_a_List_of_String")
        self.log("---  " + "Star_A_multiline_string_to_a_List_of_String")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def Given_multiline_string(self, value: str) -> None:
        print("---  " + "Given_multiline_string")
        self.log("---  " + "Given_multiline_string")
        self.log(str(value))
        self.original_string = value;
        print(value)

    def Then_should_be_equal_to_this_list(self, values: List[str]) -> None:
        print("---  " + "Then_should_be_equal_to_this_list")
        self.log("---  " + "Then_should_be_equal_to_this_list")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def Star_A_table_to_List_of_List_of_String(self, values: List[List[str]]) -> None:
        print("---  " + "Star_A_table_to_List_of_List_of_String")
        self.log("---  " + "Star_A_table_to_List_of_List_of_String")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def Star_A_Table_to_List_Of_List_Of_Object(self, values: List[List[str]]) -> None:
        its = self.convert_list(values)
        print(its)
        self.log("---  " + "Star_A_Table_to_List_Of_List_Of_Object")

    def Star_A_table_to_List_of_Object(self, values: List[ExampleClass]) -> None:
        print("---  " + "Star_A_table_to_List_of_Object")
        self.log("---  " + "Star_A_table_to_List_of_Object")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def Star_A_table_to_List_of_Object_with_Defaults(self, values: List[ExampleClass]) -> None:
        print("---  " + "Star_A_table_to_List_of_Object_with_Defaults")
        self.log("---  " + "Star_A_table_to_List_of_Object_with_Defaults")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def Star_A_table_to_List_of_Object_with_Blanks_in_Values(self, values: List[ExampleClassWithBlanks]) -> None:
        print("---  " + "Star_A_table_to_List_of_Object_with_Blanks_in_Values")
        self.log("---  " + "Star_A_table_to_List_of_Object_with_Blanks_in_Values")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def Star_A_table_to_List_of_Object_with_Blanks_in_Defaults(self, values: List[ExampleClassWithBlanks]) -> None:
        print("---  " + "Star_A_table_to_List_of_Object_with_Blanks_in_Defaults")
        self.log("---  " + "Star_A_table_to_List_of_Object_with_Blanks_in_Defaults")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def Star_A_table_to_String(self, value: str) -> None:
        print("---  " + "Star_A_table_to_String")
        self.log("---  " + "Star_A_table_to_String")
        self.log(str(value))
        print(value)

    def Given_A_table_to_String(self, value: str) -> None:
        print("---  " + "Given_A_table_to_String")
        self.log("---  " + "Given_A_table_to_String")
        self.log(str(value))
        self.original_string = value
        print(value)

    def Then_string_should_be_same_as(self, value: str) -> None:
        print("---  " + "Then_string_should_be_same_as")
        self.log("---  " + "Then_string_should_be_same_as")
        self.log(str(value))
        print(value)
        assert self.original_string == value

    def Given_A_table_to_List_of_Object_with_Defaults(self, values: List[ExampleClass]) -> None:
        print("---  " + "Given_A_table_to_List_of_Object_with_Defaults")
        self.log("---  " + "Given_A_table_to_List_of_Object_with_Defaults")
        self.log(str(values))
        for value in values:
            print(value)
        self.original_table = values

    def Then_table_should_be_same_as(self, values: List[ExampleClass]) -> None:
        print("---  " + "Then_table_should_be_same_as")
        self.log("---  " + "Then_table_should_be_same_as")
        self.log(str(values))
        for value in values:
            print(value)
        assert self.original_table == values

    def Given_A_table_to_List_of_Object(self, values: List[ExampleClass]) -> None:
        print("---  " + "Given_A_table_to_List_of_Object")
        self.log("---  " + "Given_A_table_to_List_of_Object")
        self.log(str(values))
        for value in values:
            print(value)
        self.original_table = values

    def Then_transposed_table_to_List_of_Object_should_be_the_same(self, values: List[ExampleClass]) -> None:
        print("---  " + "Then_transposed_table_to_List_of_Object_should_be_the_same")
        self.log("---  " + "Then_transposed_table_to_List_of_Object_should_be_the_same")
        self.log(str(values))
        for value in values:
            print(value)
        assert self.original_table == values


    def convert_list(self, string_list: List[List[str]]) -> List[List[int]]:
        class_list = []  # Initialize empty list
        for inner_list in string_list:
            inner_class_list = [int(s) for s in inner_list]
        class_list.append(inner_class_list)
        return class_list
       
