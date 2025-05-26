import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Define import *
from tests.gherkinexecutor.Feature_Define.Feature_Define_glue import Feature_Define_glue


class Feature_Define(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def test_Scenario_Simple_Replacement(self):
        feature_Define_glue_object = Feature_Define_glue()
        self.log("Scenario_Simple_Replacement")

        object_list1 : List[IDValue] = [
            IDValue.Builder()
                .setId("A")
                .setValue("100")
                .build()
            ,IDValue.Builder()
                .setId("B")
                .setValue("1")
                .build()
            ]
        feature_Define_glue_object.Given_this_data(object_list1)

        object_list2 : List[IDValue] = [
            IDValue.Builder()
                .setId("A")
                .setValue("100")
                .build()
            ,IDValue.Builder()
                .setId("B")
                .setValue("1")
                .build()
            ]
        feature_Define_glue_object.Then_should_be_equal_to_data(object_list2)

    def test_Scenario_Try_out_replacements_with_a_calculation(self):
        feature_Define_glue_object = Feature_Define_glue()
        self.log("Scenario_Try_out_replacements_with_a_calculation")

        object_list3 : List[IDValue] = [
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
        feature_Define_glue_object.Given_this_data(object_list3)

        object_list4 : List[IDValue] = [
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
        feature_Define_glue_object.Then_should_be_equal_to_data(object_list4)

