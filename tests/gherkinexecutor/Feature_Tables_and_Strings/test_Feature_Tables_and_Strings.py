import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Tables_and_Strings import *
from tests.gherkinexecutor.Feature_Tables_and_Strings.Feature_Tables_and_Strings_glue import Feature_Tables_and_Strings_glue


class Feature_Tables_and_Strings(unittest.TestCase):


    def test_Scenario_Here_are_string_options(self):
        feature_Tables_and_Strings_glue_object = Feature_Tables_and_Strings_glue()

        string1 ="""
One line
Two line
""".strip()
        feature_Tables_and_Strings_glue_object.Star_A_multiline_string_to_a_string(string1)

        string_list2 = [
            "Three line"
            ,"Four line"
            ]
        feature_Tables_and_Strings_glue_object.Star_A_multiline_string_to_a_List_of_String(string_list2)

    def test_Scenario_Check_String_Variations(self):
        feature_Tables_and_Strings_glue_object = Feature_Tables_and_Strings_glue()

        string3 ="""
One line
Two line
""".strip()
        feature_Tables_and_Strings_glue_object.Given_multiline_string(string3)

        string_list4 = [
            "One line"
            ,"Two line"
            ]
        feature_Tables_and_Strings_glue_object.Then_should_be_equal_to_this_list(string_list4)

    def test_Scenario_Here_are_table_options(self):
        feature_Tables_and_Strings_glue_object = Feature_Tables_and_Strings_glue()

        string_list_list5 = [
            [
            "aa"
            ,"bb"
            ]
            ,[
            "cc"
            ,"dd"
            ]
            ]
        feature_Tables_and_Strings_glue_object.Star_A_table_to_List_of_List_of_String(string_list_list5)

        string_list_list6 :  List[List[str]]  = [
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
        feature_Tables_and_Strings_glue_object.Star_A_Table_to_List_Of_List_Of_Object(string_list_list6)

        object_list7 : List[ExampleClass] = [
            ExampleClass.Builder()
                .setFielda("a")
                .setFieldb("b")
                .build()
            ,ExampleClass.Builder()
                .setFielda("c")
                .setFieldb("d")
                .build()
            ]
        feature_Tables_and_Strings_glue_object.Star_A_table_to_List_of_Object(object_list7)

        object_list8 : List[ExampleClass] = [
            ExampleClass.Builder()
                .setFielda("a")
                .setFieldb("b")
                .build()
            ,ExampleClass.Builder()
                .setFielda("c")
                .setFieldb("d")
                .build()
            ]
        feature_Tables_and_Strings_glue_object.Star_A_table_to_List_of_Object(object_list8)

        object_list9 : List[ExampleClass] = [
            ExampleClass.Builder()
                .setFielda("a")
                .build()
            ,ExampleClass.Builder()
                .setFielda("c")
                .build()
            ]
        feature_Tables_and_Strings_glue_object.Star_A_table_to_List_of_Object_with_Defaults(object_list9)

        object_list10 : List[ExampleClassWithBlanks] = [
            ExampleClassWithBlanks.Builder()
                .setField_1(" ")
                .setField_2("b")
                .build()
            ,ExampleClassWithBlanks.Builder()
                .setField_1("c")
                .setField_2(" ")
                .build()
            ]
        feature_Tables_and_Strings_glue_object.Star_A_table_to_List_of_Object_with_Blanks_in_Values(object_list10)

        object_list11 : List[ExampleClassWithBlanks] = [
            ExampleClassWithBlanks.Builder()
                .setField_1(" ")
                .build()
            ,ExampleClassWithBlanks.Builder()
                .setField_1("c")
                .build()
            ]
        feature_Tables_and_Strings_glue_object.Star_A_table_to_List_of_Object_with_Blanks_in_Defaults(object_list11)

        table12 = """
| aa  | bb  |
| cc  | dd  |
""".strip()
        feature_Tables_and_Strings_glue_object.Star_A_table_to_String(table12)

    def test_Scenario_Table_to_String(self):
        feature_Tables_and_Strings_glue_object = Feature_Tables_and_Strings_glue()

        table13 = """
| aa  | bb  |
| cc  | dd  |
""".strip()
        feature_Tables_and_Strings_glue_object.Given_A_table_to_String(table13)

        string14 ="""
| aa  | bb  |
| cc  | dd  |
""".strip()
        feature_Tables_and_Strings_glue_object.Then_string_should_be_same_as(string14)

    def test_Scenario_Table_without_all_fields_uses_defaults(self):
        feature_Tables_and_Strings_glue_object = Feature_Tables_and_Strings_glue()

        object_list15 : List[ExampleClass] = [
            ExampleClass.Builder()
                .setFielda("a")
                .build()
            ,ExampleClass.Builder()
                .setFielda("c")
                .build()
            ]
        feature_Tables_and_Strings_glue_object.Given_A_table_to_List_of_Object_with_Defaults(object_list15)

        object_list16 : List[ExampleClass] = [
            ExampleClass.Builder()
                .setFielda("a")
                .setFieldb("x")
                .build()
            ,ExampleClass.Builder()
                .setFielda("c")
                .setFieldb("x")
                .build()
            ]
        feature_Tables_and_Strings_glue_object.Then_table_should_be_same_as(object_list16)

    def test_Scenario_Transpose_Table(self):
        feature_Tables_and_Strings_glue_object = Feature_Tables_and_Strings_glue()

        object_list17 : List[ExampleClass] = [
            ExampleClass.Builder()
                .setFielda("a")
                .setFieldb("b")
                .build()
            ,ExampleClass.Builder()
                .setFielda("c")
                .setFieldb("d")
                .build()
            ]
        feature_Tables_and_Strings_glue_object.Given_A_table_to_List_of_Object(object_list17)

        object_list18 : List[ExampleClass] = [
            ExampleClass.Builder()
                .setFielda("a")
                .setFieldb("b")
                .build()
            ,ExampleClass.Builder()
                .setFielda("c")
                .setFieldb("d")
                .build()
            ]
        feature_Tables_and_Strings_glue_object.Then_transposed_table_to_List_of_Object_should_be_the_same(object_list18)

