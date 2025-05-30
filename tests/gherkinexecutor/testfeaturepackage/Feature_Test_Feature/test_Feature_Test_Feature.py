import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Test_Feature import *
from tests.gherkinexecutor.Feature_Test_Feature.Feature_Test_Feature_glue import Feature_Test_Feature_glue


class Feature_Test_Feature(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def test_Scenario_Include_something(self):
        feature_Test_Feature_glue_object = Feature_Test_Feature_glue()
        self.log("Scenario_Include_something")

        string1 ="""
This is an include string from the local directory
""".strip()
        feature_Test_Feature_glue_object.Given_local_include(string1)

        string2 ="""
This is an include string from the local directory
""".strip()
        feature_Test_Feature_glue_object.Then_string_equals(string2)

        string3 ="""
This is an include string from the main directory
""".strip()
        feature_Test_Feature_glue_object.Given_global_include(string3)

        string4 ="""
This is an include string from the main directory
""".strip()
        feature_Test_Feature_glue_object.Then_string_equals(string4)

