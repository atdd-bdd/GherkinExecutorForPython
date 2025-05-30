import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Include import *
from tests.gherkinexecutor.Feature_Include.Feature_Include_glue import Feature_Include_glue


class Feature_Include(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def test_Scenario_An_include(self):
        feature_Include_glue_object = Feature_Include_glue()
        self.log("Scenario_An_include")

        string1 ="""
This is an include string from the main directory
""".strip()
        feature_Include_glue_object.Given_a_string_include(string1)

        string2 ="""
This is an include string from the main directory
""".strip()
        feature_Include_glue_object.Then_should_be_equal_to(string2)

    def test_Scenario_An_include_from_base_directory(self):
        feature_Include_glue_object = Feature_Include_glue()
        self.log("Scenario_An_include_from_base_directory")

        string3 ="""
This is an include string from the main directory
""".strip()
        feature_Include_glue_object.Given_a_string_include(string3)

        string4 ="""
This is an include string from the main directory
""".strip()
        feature_Include_glue_object.Then_should_be_equal_to(string4)

    def test_Scenario_An_include_of_CSV_file(self):
        feature_Include_glue_object = Feature_Include_glue()
        self.log("Scenario_An_include_of_CSV_file")

        object_list5 : List[CSVContents] = [
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
        feature_Include_glue_object.Given_a_table(object_list5)

        object_list6 : List[CSVContents] = [
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
        feature_Include_glue_object.Then_Should_be_equal_to_table(object_list6)

