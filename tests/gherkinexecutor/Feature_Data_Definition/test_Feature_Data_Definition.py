import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Data_Definition import *
from tests.gherkinexecutor.Feature_Data_Definition.Feature_Data_Definition_glue import Feature_Data_Definition_glue


class Feature_Data_Definition(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def test_Scenario_Simple_Comparison(self):
        feature_Data_Definition_glue_object = Feature_Data_Definition_glue()
        self.log("Scenario_Simple_Comparison")

        object_list1 : List[ATest] = [
            ATest.Builder()
                .setAnint("1")
                .setAstring("something")
                .setAdouble("1.2")
                .build()
            ]
        feature_Data_Definition_glue_object.Given_table_is(object_list1)

        object_list2 : List[ATest] = [
            ATest.Builder()
             .set_compare()
                .setAstring("something")
                .build()
            ]
        feature_Data_Definition_glue_object.When_compared_to(object_list2)

        string_list_list3 = [
            [
            "true"
            ]
            ]
        feature_Data_Definition_glue_object.Then_result_is(string_list_list3)

        object_list4 : List[ATest] = [
            ATest.Builder()
             .set_compare()
                .setAstring("something else")
                .build()
            ]
        feature_Data_Definition_glue_object.When_compared_to(object_list4)

        string_list_list5 = [
            [
            "false"
            ]
            ]
        feature_Data_Definition_glue_object.Then_result_is(string_list_list5)

    def test_Scenario_Check_All_Types(self):
        feature_Data_Definition_glue_object = Feature_Data_Definition_glue()
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
        feature_Data_Definition_glue_object.Given_these_are_all_the_types(object_list6)

