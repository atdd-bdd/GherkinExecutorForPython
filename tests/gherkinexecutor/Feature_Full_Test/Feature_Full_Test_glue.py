from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime
from tests.gherkinexecutor.Feature_Full_Test import *
from typing import List
import sys

class Feature_Full_Test_glue :
    DNCString = "?DNC?"

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime
from tests.gherkinexecutor.Feature_Full_Test import *
from typing import List
import sys

class Feature_Full_Test_glue :
    DNCString = "?DNC?"

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime
from tests.gherkinexecutor.Feature_Full_Test import *
from typing import List
import sys

class Feature_Full_Test_glue :
    DNCString = "?DNC?"

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime
from tests.gherkinexecutor.Feature_Full_Test import *
from typing import List
import sys

class Feature_Full_Test_glue :
    DNCString = "?DNC?"

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime
from tests.gherkinexecutor.Feature_Full_Test import *
from typing import List
import sys

class Feature_Full_Test_glue :
    DNCString = "?DNC?"

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime
from tests.gherkinexecutor.Feature_Full_Test import *
from typing import List
import sys

class Feature_Full_Test_glue :
    DNCString = "?DNC?"

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime
from tests.gherkinexecutor.Feature_Full_Test import *
from typing import List
import sys

class Feature_Full_Test_glue :
    DNCString = "?DNC?"

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime
from tests.gherkinexecutor.Feature_Full_Test import *
from typing import List
import sys

class Feature_Full_Test_glue :
    DNCString = "?DNC?"

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime
from tests.gherkinexecutor.Feature_Full_Test import *
from typing import List
import sys

class Feature_Full_Test_glue :
    DNCString = "?DNC?"

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime
from tests.gherkinexecutor.Feature_Full_Test import *
from typing import List
import sys

class Feature_Full_Test_glue :
    DNCString = "?DNC?"

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime
from tests.gherkinexecutor.Feature_Full_Test import *
from typing import List
import sys

class Feature_Full_Test_glue :
    DNCString = "?DNC?"

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

from tests.gherkinexecutor.ID import ID
from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations
from datetime import datetime
from tests.gherkinexecutor.Feature_Full_Test import *
from typing import List
import sys

class Feature_Full_Test_glue :
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

    def When_compared_to(self, values: List[ATest]) -> None:
        print("---  " + "When_compared_to")
        self.log("---  " + "When_compared_to")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_ATestInternal()

    def Then_result_is(self, values: List[List[str]]) -> None:
        print("---  " + "Then_result_is")
        self.log("---  " + "Then_result_is")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def Given_these_are_all_the_types(self, values: List[AllTypes]) -> None:
        print("---  " + "Given_these_are_all_the_types")
        self.log("---  " + "Given_these_are_all_the_types")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_AllTypesInternal()

    def Given_type_values_are(self, values: List[SomeTypes]) -> None:
        print("---  " + "Given_type_values_are")
        self.log("---  " + "Given_type_values_are")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_SomeTypesInternal()

    def Then_this_should_be_equal(self, values: List[SomeTypes]) -> None:
        print("---  " + "Then_this_should_be_equal")
        self.log("---  " + "Then_this_should_be_equal")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_SomeTypesInternal()

    def Given_table_is_bad_initializer(self, values: List[ATestBad]) -> None:
        print("---  " + "Given_table_is_bad_initializer")
        self.log("---  " + "Given_table_is_bad_initializer")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_ATestBadInternal()

    def Given_this_data(self, values: List[IDValue]) -> None:
        print("---  " + "Given_this_data")
        self.log("---  " + "Given_this_data")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def Then_should_be_equal_to_data(self, values: List[IDValue]) -> None:
        print("---  " + "Then_should_be_equal_to_data")
        self.log("---  " + "Then_should_be_equal_to_data")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def Calculation_Convert_F_to_C(self, values: List[FandC]) -> None:
        print("---  " + "Calculation_Convert_F_to_C")
        self.log("---  " + "Calculation_Convert_F_to_C")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_FandCInternal()

    def Rule_ID_must_have_exactly_5_letters_and_begin_with_Q(self, values: List[ValueValid]) -> None:
        print("---  " + "Rule_ID_must_have_exactly_5_letters_and_begin_with_Q")
        self.log("---  " + "Rule_ID_must_have_exactly_5_letters_and_begin_with_Q")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_ValueValidInternal()

    def Given_list_of_numbers(self, values: List[LabelValue]) -> None:
        print("---  " + "Given_list_of_numbers")
        self.log("---  " + "Given_list_of_numbers")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_LabelValueInternal()

    def When_filtered_by_ID_with_value(self, values: List[List[str]]) -> None:
        print("---  " + "When_filtered_by_ID_with_value")
        self.log("---  " + "When_filtered_by_ID_with_value")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def Then_sum_is(self, values: List[List[str]]) -> None:
        print("---  " + "Then_sum_is")
        self.log("---  " + "Then_sum_is")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def When_filtered_by(self, values: List[FilterValue]) -> None:
        print("---  " + "When_filtered_by")
        self.log("---  " + "When_filtered_by")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_FilterValueInternal()

    def Then_result(self, values: List[ResultValue]) -> None:
        print("---  " + "Then_result")
        self.log("---  " + "Then_result")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_ResultValueInternal()

    def Given_this_data_should_be_okay(self, values: List[ImportData]) -> None:
        print("---  " + "Given_this_data_should_be_okay")
        self.log("---  " + "Given_this_data_should_be_okay")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_ImportDataInternal()

    def Given_this_data_should_fail(self, values: List[ImportData]) -> None:
        print("---  " + "Given_this_data_should_fail")
        self.log("---  " + "Given_this_data_should_fail")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_ImportDataInternal()

    def Given_a_string_include(self, value: str) -> None:
        print("---  " + "Given_a_string_include")
        self.log("---  " + "Given_a_string_include")
        self.log(str(value))
        print(value)

    def Then_should_be_equal_to(self, value: str) -> None:
        print("---  " + "Then_should_be_equal_to")
        self.log("---  " + "Then_should_be_equal_to")
        self.log(str(value))
        print(value)

    def Given_a_table(self, values: List[CSVContents]) -> None:
        print("---  " + "Given_a_table")
        self.log("---  " + "Given_a_table")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def Then_Should_be_equal_to_table(self, values: List[CSVContents]) -> None:
        print("---  " + "Then_Should_be_equal_to_table")
        self.log("---  " + "Then_Should_be_equal_to_table")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

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
        print(value)

    def Then_string_should_be_same_as(self, value: str) -> None:
        print("---  " + "Then_string_should_be_same_as")
        self.log("---  " + "Then_string_should_be_same_as")
        self.log(str(value))
        print(value)

    def Given_A_table_to_List_of_Object_with_Defaults(self, values: List[ExampleClass]) -> None:
        print("---  " + "Given_A_table_to_List_of_Object_with_Defaults")
        self.log("---  " + "Given_A_table_to_List_of_Object_with_Defaults")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def Then_table_should_be_same_as(self, values: List[ExampleClass]) -> None:
        print("---  " + "Then_table_should_be_same_as")
        self.log("---  " + "Then_table_should_be_same_as")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def Given_A_table_to_List_of_Object(self, values: List[ExampleClass]) -> None:
        print("---  " + "Given_A_table_to_List_of_Object")
        self.log("---  " + "Given_A_table_to_List_of_Object")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def Then_transposed_table_to_List_of_Object_should_be_the_same(self, values: List[ExampleClass]) -> None:
        print("---  " + "Then_transposed_table_to_List_of_Object_should_be_the_same")
        self.log("---  " + "Then_transposed_table_to_List_of_Object_should_be_the_same")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def Given_board_is(self, values: List[List[str]]) -> None:
        print("---  " + "Given_board_is")
        self.log("---  " + "Given_board_is")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def When_move_is(self, values: List[Move]) -> None:
        print("---  " + "When_move_is")
        self.log("---  " + "When_move_is")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_MoveInternal()

    def Then_board_is_now(self, value: str) -> None:
        print("---  " + "Then_board_is_now")
        self.log("---  " + "Then_board_is_now")
        self.log(str(value))
        print(value)

    def When_one_move_is(self, values: List[List[str]]) -> None:
        print("---  " + "When_one_move_is")
        self.log("---  " + "When_one_move_is")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts

    def When_moves_are(self, values: List[Move]) -> None:
        print("---  " + "When_moves_are")
        self.log("---  " + "When_moves_are")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_MoveInternal()

    def Given_one_object_is(self, values: List[SimpleClass]) -> None:
        print("---  " + "Given_one_object_is")
        self.log("---  " + "Given_one_object_is")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_SimpleClassInternal()

    def Then_Json_should_be(self, value: str) -> None:
        print("---  " + "Then_Json_should_be")
        self.log("---  " + "Then_Json_should_be")
        self.log(str(value))
        print(value)

    def Given_Json_is(self, value: str) -> None:
        print("---  " + "Given_Json_is")
        self.log("---  " + "Given_Json_is")
        self.log(str(value))
        print(value)

    def Then_the_converted_object_is(self, values: List[SimpleClass]) -> None:
        print("---  " + "Then_the_converted_object_is")
        self.log("---  " + "Then_the_converted_object_is")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_SimpleClassInternal()

    def Given_a_table_is(self, values: List[SimpleClass]) -> None:
        print("---  " + "Given_a_table_is")
        self.log("---  " + "Given_a_table_is")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_SimpleClassInternal()

    def Then_Json_for_table_should_be(self, value: str) -> None:
        print("---  " + "Then_Json_for_table_should_be")
        self.log("---  " + "Then_Json_for_table_should_be")
        self.log(str(value))
        print(value)

    def Given_Json_for_table_is(self, value: str) -> None:
        print("---  " + "Given_Json_for_table_is")
        self.log("---  " + "Given_Json_for_table_is")
        self.log(str(value))
        print(value)

    def Then_the_converted_table_should_be(self, values: List[SimpleClass]) -> None:
        print("---  " + "Then_the_converted_table_should_be")
        self.log("---  " + "Then_the_converted_table_should_be")
        self.log(str(values))
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_SimpleClassInternal()


    def convert_list(self, string_list: List[List[str]]) -> List[List[int]]:
        class_list = []  # Initialize empty list
        for inner_list in string_list:
            inner_class_list = [int(s) for s in inner_list]  
        class_list.append(inner_class_list)  
        return class_list
        
