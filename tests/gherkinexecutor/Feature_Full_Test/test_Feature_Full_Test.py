import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Full_Test import *
from tests.gherkinexecutor.Feature_Full_Test.Feature_Full_Test_glue import Feature_Full_Test_glue


class Feature_Full_Test(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    
import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Full_Test import *
from tests.gherkinexecutor.Feature_Full_Test.Feature_Full_Test_glue import Feature_Full_Test_glue


class Feature_Data_Definition(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    
import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Full_Test import *
from tests.gherkinexecutor.Feature_Full_Test.Feature_Full_Test_glue import Feature_Full_Test_glue


class Feature_Data_Types(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    
import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Full_Test import *
from tests.gherkinexecutor.Feature_Full_Test.Feature_Full_Test_glue import Feature_Full_Test_glue


class Feature_Data_Definition_Error(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    
import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Full_Test import *
from tests.gherkinexecutor.Feature_Full_Test.Feature_Full_Test_glue import Feature_Full_Test_glue


class Feature_Define(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    
import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Full_Test import *
from tests.gherkinexecutor.Feature_Full_Test.Feature_Full_Test_glue import Feature_Full_Test_glue


class Feature_Examples(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    
import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Full_Test import *
from tests.gherkinexecutor.Feature_Full_Test.Feature_Full_Test_glue import Feature_Full_Test_glue


class Feature_Import(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    
import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Full_Test import *
from tests.gherkinexecutor.Feature_Full_Test.Feature_Full_Test_glue import Feature_Full_Test_glue


class Feature_Include(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    
import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Full_Test import *
from tests.gherkinexecutor.Feature_Full_Test.Feature_Full_Test_glue import Feature_Full_Test_glue


class Feature_Simple_Test(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    
import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Full_Test import *
from tests.gherkinexecutor.Feature_Full_Test.Feature_Full_Test_glue import Feature_Full_Test_glue


class Feature_Tables_and_Strings(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    
import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Full_Test import *
from tests.gherkinexecutor.Feature_Full_Test.Feature_Full_Test_glue import Feature_Full_Test_glue


class Feature_Tic_Tac_Toe_Game(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    
import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Full_Test import *
from tests.gherkinexecutor.Feature_Full_Test.Feature_Full_Test_glue import Feature_Full_Test_glue


class Feature_Json(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def test_Scenario_Simple_Comparison(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Simple_Comparison")

        object_list1 : List[ATest] = [
            ATest.Builder()
                .setAnint("1")
                .setAstring("something")
                .setAdouble("1.2")
                .build()
            ]
        feature_Full_Test_glue_object.Given_table_is(object_list1)

        object_list2 : List[ATest] = [
            ATest.Builder()
             .set_compare()
                .setAstring("something")
                .build()
            ]
        feature_Full_Test_glue_object.When_compared_to(object_list2)

        string_list_list3 = [
            [
            "true"
            ]
            ]
        feature_Full_Test_glue_object.Then_result_is(string_list_list3)

        object_list4 : List[ATest] = [
            ATest.Builder()
             .set_compare()
                .setAstring("something else")
                .build()
            ]
        feature_Full_Test_glue_object.When_compared_to(object_list4)

        string_list_list5 = [
            [
            "false"
            ]
            ]
        feature_Full_Test_glue_object.Then_result_is(string_list_list5)

    def test_Scenario_Check_All_Types(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Check_All_Types")

        object_list6 : List[AllTypes] = [
            AllTypes.Builder()
                .setAnint("0")
                .setAfloat("0.0")
                .setAbool("false")
                .setAstring("")
                .setAcomplex("0+0j")
                .build()
            ]
        feature_Full_Test_glue_object.Given_these_are_all_the_types(object_list6)

    def test_Scenario_Use_the_data_types(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Use_the_data_types")

        object_list7 : List[SomeTypes] = [
            SomeTypes.Builder()
                .setAnint("0")
                .setAdouble("0.0")
                .setAchar("x")
                .setAnchar("y")
                .build()
            ,SomeTypes.Builder()
                .setAnint("111")
                .setAdouble("222.2")
                .setAchar("q")
                .setAnchar("")
                .build()
            ]
        feature_Full_Test_glue_object.Given_type_values_are(object_list7)

        object_list8 : List[SomeTypes] = [
            SomeTypes.Builder()
                .setAnchar("y")
                .setAnint("0")
                .setAdouble("0.0")
                .setAchar("x")
                .build()
            ,SomeTypes.Builder()
                .setAnchar("")
                .setAnint("111")
                .setAdouble("222.2")
                .setAchar("q")
                .build()
            ]
        feature_Full_Test_glue_object.Then_this_should_be_equal(object_list8)

    def test_Scenario_Simple_Table_with_int_bad(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Simple_Table_with_int_bad")

        object_list9 : List[ATest] = [
            ATest.Builder()
                .setAnint("q")
                .setAstring("something")
                .setAdouble("1.1")
                .build()
            ]
        feature_Full_Test_glue_object.Given_table_is(object_list9)

    def test_Scenario_Simple_Table_with_double_bad(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Simple_Table_with_double_bad")

        object_list10 : List[ATest] = [
            ATest.Builder()
                .setAnint("1")
                .setAstring("something")
                .setAdouble("r")
                .build()
            ]
        feature_Full_Test_glue_object.Given_table_is(object_list10)

    def test_Scenario_Simple_Table_with_initializer_bad(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Simple_Table_with_initializer_bad")

        object_list11 : List[ATestBad] = [
            ATestBad.Builder()
                .setAnint("1")
                .build()
            ]
        feature_Full_Test_glue_object.Given_table_is_bad_initializer(object_list11)

    def test_Scenario_Simple_Replacement(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Simple_Replacement")

        object_list12 : List[IDValue] = [
            IDValue.Builder()
                .setId("A")
                .setValue("100")
                .build()
            ,IDValue.Builder()
                .setId("B")
                .setValue("1")
                .build()
            ]
        feature_Full_Test_glue_object.Given_this_data(object_list12)

        object_list13 : List[IDValue] = [
            IDValue.Builder()
                .setId("A")
                .setValue("100")
                .build()
            ,IDValue.Builder()
                .setId("B")
                .setValue("1")
                .build()
            ]
        feature_Full_Test_glue_object.Then_should_be_equal_to_data(object_list13)

    def test_Scenario_Try_out_replacements_with_a_calculation(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Try_out_replacements_with_a_calculation")

        object_list14 : List[IDValue] = [
            IDValue.Builder()
                .setId("A")
                .setValue("100")
                .build()
            ,IDValue.Builder()
                .setId("B")
                .setValue("1")
                .build()
            ,IDValue.Builder()
                .setId("C")
                .setValue("(1 + 100)/2")
                .build()
            ]
        feature_Full_Test_glue_object.Given_this_data(object_list14)

        object_list15 : List[IDValue] = [
            IDValue.Builder()
                .setId("A")
                .setValue("100")
                .build()
            ,IDValue.Builder()
                .setId("B")
                .setValue("1")
                .build()
            ,IDValue.Builder()
                .setId("C")
                .setValue("(1 + 100)/2")
                .build()
            ]
        feature_Full_Test_glue_object.Then_should_be_equal_to_data(object_list15)

    def test_Scenario_Temperature_Conversion(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Temperature_Conversion")

        object_list16 : List[FandC] = [
            FandC.Builder()
                .setF("32")
                .setC("0")
                .setNotes("Freezing")
                .build()
            ,FandC.Builder()
                .setF("212")
                .setC("100")
                .setNotes("Boiling")
                .build()
            ,FandC.Builder()
                .setF("-40")
                .setC("-40")
                .setNotes("Below zero")
                .build()
            ]
        feature_Full_Test_glue_object.Calculation_Convert_F_to_C(object_list16)

    def test_Scenario_Domain_Term_ID(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Domain_Term_ID")

        object_list17 : List[ValueValid] = [
            ValueValid.Builder()
                .setValue("Q1234")
                .setValid("true")
                .setNotes("")
                .build()
            ,ValueValid.Builder()
                .setValue("Q123")
                .setValid("false")
                .setNotes("Too short")
                .build()
            ,ValueValid.Builder()
                .setValue("Q12345")
                .setValid("false")
                .setNotes("Too long")
                .build()
            ,ValueValid.Builder()
                .setValue("A1234")
                .setValid("false")
                .setNotes("Must begin with Q")
                .build()
            ]
        feature_Full_Test_glue_object.Rule_ID_must_have_exactly_5_letters_and_begin_with_Q(object_list17)

    def test_Scenario_Filter_Data(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Filter_Data")

        object_list18 : List[LabelValue] = [
            LabelValue.Builder()
                .setId("Q1234")
                .setValue("1")
                .build()
            ,LabelValue.Builder()
                .setId("Q9999")
                .setValue("2")
                .build()
            ,LabelValue.Builder()
                .setId("Q1234")
                .setValue("3")
                .build()
            ]
        feature_Full_Test_glue_object.Given_list_of_numbers(object_list18)

        string_list_list19 = [
            [
            "Q1234"
            ]
            ]
        feature_Full_Test_glue_object.When_filtered_by_ID_with_value(string_list_list19)

        string_list_list20 = [
            [
            "4"
            ]
            ]
        feature_Full_Test_glue_object.Then_sum_is(string_list_list20)

    def test_Scenario_Filter_Data_Another_Way(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Filter_Data_Another_Way")

        object_list21 : List[LabelValue] = [
            LabelValue.Builder()
                .setId("Q1234")
                .setValue("1")
                .build()
            ,LabelValue.Builder()
                .setId("Q9999")
                .setValue("2")
                .build()
            ,LabelValue.Builder()
                .setId("Q1234")
                .setValue("3")
                .build()
            ]
        feature_Full_Test_glue_object.Given_list_of_numbers(object_list21)

        object_list22 : List[FilterValue] = [
            FilterValue.Builder()
                .setValue("Q1234")
                .build()
            ]
        feature_Full_Test_glue_object.When_filtered_by(object_list22)

        object_list23 : List[ResultValue] = [
            ResultValue.Builder()
                .setSum("4")
                .build()
            ]
        feature_Full_Test_glue_object.Then_result(object_list23)

    def test_Scenario_Use_an_import(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Use_an_import")

        object_list24 : List[ImportData] = [
            ImportData.Builder()
                .setMydate("2025-05-26")
                .build()
            ,ImportData.Builder()
                .setMydate("2025-05-27")
                .build()
            ]
        feature_Full_Test_glue_object.Given_this_data_should_be_okay(object_list24)

    def test_Scenario_Should_fail(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Should_fail")

        object_list25 : List[ImportData] = [
            ImportData.Builder()
                .setMydate("2025-02-30")
                .build()
            ]
        feature_Full_Test_glue_object.Given_this_data_should_fail(object_list25)

    def test_Scenario_An_include(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_An_include")

        string26 ="""
This is an include string from the main directory
""".strip()
        feature_Full_Test_glue_object.Given_a_string_include(string26)

        string27 ="""
This is an include string from the main directory
""".strip()
        feature_Full_Test_glue_object.Then_should_be_equal_to(string27)

    def test_Scenario_An_include_from_base_directory(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_An_include_from_base_directory")

        string28 ="""
This is an include string from the main directory
""".strip()
        feature_Full_Test_glue_object.Given_a_string_include(string28)

        string29 ="""
This is an include string from the main directory
""".strip()
        feature_Full_Test_glue_object.Then_should_be_equal_to(string29)

    def test_Scenario_An_include_of_CSV_file(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_An_include_of_CSV_file")

        object_list30 : List[CSVContents] = [
            CSVContents.Builder()
                .setA("a")
                .setB("b,c")
                .setC("d,")
                .build()
            ,CSVContents.Builder()
                .setA("1")
                .setB("2")
                .setC("3")
                .build()
            ]
        feature_Full_Test_glue_object.Given_a_table(object_list30)

        object_list31 : List[CSVContents] = [
            CSVContents.Builder()
                .setA("a")
                .setB("b,c")
                .setC("d,")
                .build()
            ,CSVContents.Builder()
                .setA("1")
                .setB("2")
                .setC("3")
                .build()
            ]
        feature_Full_Test_glue_object.Then_Should_be_equal_to_table(object_list31)

    def test_Scenario_Simple(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Simple")

        object_list32 : List[ATest] = [
            ATest.Builder()
                .setAnint("1")
                .setAstring("something")
                .setAdouble("1.2")
                .build()
            ]
        feature_Full_Test_glue_object.Given_table_is(object_list32)

    def test_Scenario_Here_are_string_options(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Here_are_string_options")

        string33 ="""
One line
Two line
""".strip()
        feature_Full_Test_glue_object.Star_A_multiline_string_to_a_string(string33)

        string_list34 = [
            "Three line"
            ,"Four line"
            ]
        feature_Full_Test_glue_object.Star_A_multiline_string_to_a_List_of_String(string_list34)

    def test_Scenario_Check_String_Variations(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Check_String_Variations")

        string35 ="""
One line
Two line
""".strip()
        feature_Full_Test_glue_object.Given_multiline_string(string35)

        string_list36 = [
            "One line"
            ,"Two line"
            ]
        feature_Full_Test_glue_object.Then_should_be_equal_to_this_list(string_list36)

    def test_Scenario_Here_are_table_options(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Here_are_table_options")

        string_list_list37 = [
            [
            "aa"
            ,"bb"
            ]
            ,[
            "cc"
            ,"dd"
            ]
            ]
        feature_Full_Test_glue_object.Star_A_table_to_List_of_List_of_String(string_list_list37)

        string_list_list38 :  List[List[str]]  = [
            [
            "1"
            ,"2"
            ]
            ,[
            "3"
            ,"4"
            ]
            ,[
            "5"
            ,"6"
            ]
            ]
        feature_Full_Test_glue_object.Star_A_Table_to_List_Of_List_Of_Object(string_list_list38)

        object_list39 : List[ExampleClass] = [
            ExampleClass.Builder()
                .setFielda("a")
                .setFieldb("b")
                .build()
            ,ExampleClass.Builder()
                .setFielda("c")
                .setFieldb("d")
                .build()
            ]
        feature_Full_Test_glue_object.Star_A_table_to_List_of_Object(object_list39)

        object_list40 : List[ExampleClass] = [
            ExampleClass.Builder()
                .setFielda("a")
                .setFieldb("b")
                .build()
            ,ExampleClass.Builder()
                .setFielda("c")
                .setFieldb("d")
                .build()
            ]
        feature_Full_Test_glue_object.Star_A_table_to_List_of_Object(object_list40)

        object_list41 : List[ExampleClass] = [
            ExampleClass.Builder()
                .setFielda("a")
                .build()
            ,ExampleClass.Builder()
                .setFielda("c")
                .build()
            ]
        feature_Full_Test_glue_object.Star_A_table_to_List_of_Object_with_Defaults(object_list41)

        object_list42 : List[ExampleClassWithBlanks] = [
            ExampleClassWithBlanks.Builder()
                .setField_1(" ")
                .setField_2("b")
                .build()
            ,ExampleClassWithBlanks.Builder()
                .setField_1("c")
                .setField_2(" ")
                .build()
            ]
        feature_Full_Test_glue_object.Star_A_table_to_List_of_Object_with_Blanks_in_Values(object_list42)

        object_list43 : List[ExampleClassWithBlanks] = [
            ExampleClassWithBlanks.Builder()
                .setField_1(" ")
                .build()
            ,ExampleClassWithBlanks.Builder()
                .setField_1("c")
                .build()
            ]
        feature_Full_Test_glue_object.Star_A_table_to_List_of_Object_with_Blanks_in_Defaults(object_list43)

        table44 = """
| aa  | bb  |
| cc  | dd  |
""".strip()
        feature_Full_Test_glue_object.Star_A_table_to_String(table44)

    def test_Scenario_Table_to_String(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Table_to_String")

        table45 = """
| aa  | bb  |
| cc  | dd  |
""".strip()
        feature_Full_Test_glue_object.Given_A_table_to_String(table45)

        string46 ="""
| aa  | bb  |
| cc  | dd  |
""".strip()
        feature_Full_Test_glue_object.Then_string_should_be_same_as(string46)

    def test_Scenario_Table_without_all_fields_uses_defaults(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Table_without_all_fields_uses_defaults")

        object_list47 : List[ExampleClass] = [
            ExampleClass.Builder()
                .setFielda("a")
                .build()
            ,ExampleClass.Builder()
                .setFielda("c")
                .build()
            ]
        feature_Full_Test_glue_object.Given_A_table_to_List_of_Object_with_Defaults(object_list47)

        object_list48 : List[ExampleClass] = [
            ExampleClass.Builder()
                .setFielda("a")
                .setFieldb("x")
                .build()
            ,ExampleClass.Builder()
                .setFielda("c")
                .setFieldb("x")
                .build()
            ]
        feature_Full_Test_glue_object.Then_table_should_be_same_as(object_list48)

    def test_Scenario_Transpose_Table(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Transpose_Table")

        object_list49 : List[ExampleClass] = [
            ExampleClass.Builder()
                .setFielda("a")
                .setFieldb("b")
                .build()
            ,ExampleClass.Builder()
                .setFielda("c")
                .setFieldb("d")
                .build()
            ]
        feature_Full_Test_glue_object.Given_A_table_to_List_of_Object(object_list49)

        object_list50 : List[ExampleClass] = [
            ExampleClass.Builder()
                .setFielda("a")
                .setFieldb("b")
                .build()
            ,ExampleClass.Builder()
                .setFielda("c")
                .setFieldb("d")
                .build()
            ]
        feature_Full_Test_glue_object.Then_transposed_table_to_List_of_Object_should_be_the_same(object_list50)

    def test_Scenario_Make_a_move(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Make_a_move")

        string_list_list51 = [
            [
            ""
            ,""
            ,""
            ]
            ,[
            ""
            ,""
            ,""
            ]
            ,[
            ""
            ,""
            ,""
            ]
            ]
        feature_Full_Test_glue_object.Given_board_is(string_list_list51)

        object_list52 : List[Move] = [
            Move.Builder()
                .setRow("1")
                .setColumn("2")
                .setMark("X")
                .build()
            ]
        feature_Full_Test_glue_object.When_move_is(object_list52)

        table53 = """
|   | X  |   |
|   |    |   |
|   |    |   |
""".strip()
        feature_Full_Test_glue_object.Then_board_is_now(table53)

    def test_Scenario_Make_a_move_using_single_element(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Make_a_move_using_single_element")

        string_list_list54 = [
            [
            ""
            ,""
            ,""
            ]
            ,[
            ""
            ,""
            ,""
            ]
            ,[
            ""
            ,""
            ,""
            ]
            ]
        feature_Full_Test_glue_object.Given_board_is(string_list_list54)

        string_list_list55 = [
            [
            "1,2,X"
            ]
            ]
        feature_Full_Test_glue_object.When_one_move_is(string_list_list55)

        table56 = """
|   | X  |   |
|   |    |   |
|   |    |   |
""".strip()
        feature_Full_Test_glue_object.Then_board_is_now(table56)

    def test_Scenario_Make_multiple_moves(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Make_multiple_moves")

        string_list_list57 = [
            [
            ""
            ,""
            ,""
            ]
            ,[
            ""
            ,""
            ,""
            ]
            ,[
            ""
            ,""
            ,""
            ]
            ]
        feature_Full_Test_glue_object.Given_board_is(string_list_list57)

        object_list58 : List[Move] = [
            Move.Builder()
                .setRow("1")
                .setColumn("2")
                .setMark("X")
                .build()
            ,Move.Builder()
                .setRow("2")
                .setColumn("3")
                .setMark("O")
                .build()
            ]
        feature_Full_Test_glue_object.When_moves_are(object_list58)

        table59 = """
|   | X  |    |
|   |    | O  |
|   |    |    |
""".strip()
        feature_Full_Test_glue_object.Then_board_is_now(table59)

    def test_Scenario_check_the_prints_to_see_how_it_works(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_check_the_prints_to_see_how_it_works")

        string_list_list60 = [
            [
            "0"
            ,"x"
            ,"0"
            ]
            ,[
            "x"
            ,"0"
            ,"x"
            ]
            ,[
            "0"
            ,"x"
            ,"0"
            ]
            ]
        feature_Full_Test_glue_object.Given_board_is(string_list_list60)

        table61 = """
| 0  | x  | 0  |
| x  | 0  | x  |
| 0  | x  | 0  |
""".strip()
        feature_Full_Test_glue_object.Then_board_is_now(table61)

    def test_Scenario_Convert_to_Json(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Convert_to_Json")

        object_list62 : List[SimpleClass] = [
            SimpleClass.Builder()
                .setAnint("1")
                .setAstring("B")
                .build()
            ]
        feature_Full_Test_glue_object.Given_one_object_is(object_list62)

        string63 ="""
{"anInt": "1","aString": "B"}
""".strip()
        feature_Full_Test_glue_object.Then_Json_should_be(string63)

    def test_Scenario_Convert_from_Json(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Convert_from_Json")

        string64 ="""
{anInt:  "1"   ,   aString:"B"  }
""".strip()
        feature_Full_Test_glue_object.Given_Json_is(string64)

        object_list65 : List[SimpleClass] = [
            SimpleClass.Builder()
                .setAnint("1")
                .setAstring("B")
                .build()
            ]
        feature_Full_Test_glue_object.Then_the_converted_object_is(object_list65)

    def test_Scenario_Convert_to_Json_Array(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Convert_to_Json_Array")

        object_list66 : List[SimpleClass] = [
            SimpleClass.Builder()
                .setAnint("1")
                .setAstring("B")
                .build()
            ,SimpleClass.Builder()
                .setAnint("2")
                .setAstring("C")
                .build()
            ]
        feature_Full_Test_glue_object.Given_a_table_is(object_list66)

        string67 ="""
[ {"anInt": "1","aString": "B"}
, {"anInt": "2","aString": "C"}
]
""".strip()
        feature_Full_Test_glue_object.Then_Json_for_table_should_be(string67)

    def test_Scenario_Convert_from_Json_Array(self):
        feature_Full_Test_glue_object = Feature_Full_Test_glue()
        self.log("Scenario_Convert_from_Json_Array")

        string68 ="""
[    {anInt:  "1"   ,   aString:"B"  },
{anInt:  "2"   ,   aString:"C"  }
]
""".strip()
        feature_Full_Test_glue_object.Given_Json_for_table_is(string68)

        object_list69 : List[SimpleClass] = [
            SimpleClass.Builder()
                .setAnint("1")
                .setAstring("B")
                .build()
            ,SimpleClass.Builder()
                .setAnint("2")
                .setAstring("C")
                .build()
            ]
        feature_Full_Test_glue_object.Then_the_converted_table_should_be(object_list69)

