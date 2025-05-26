import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Data_Definition_Error import *
from tests.gherkinexecutor.Feature_Data_Definition_Error.Feature_Data_Definition_Error_glue import Feature_Data_Definition_Error_glue


class Feature_Data_Definition_Error(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def test_Scenario_Simple_Table_with_int_bad(self):
        feature_Data_Definition_Error_glue_object = Feature_Data_Definition_Error_glue()
        self.log("Scenario_Simple_Table_with_int_bad")

        object_list1 : List[ATest] = [
            ATest.Builder()
                .setAnint("q")
                .setAstring("something")
                .setAdouble("1.1")
                .build()
            ]
        feature_Data_Definition_Error_glue_object.Given_table_is(object_list1)

    def test_Scenario_Simple_Table_with_double_bad(self):
        feature_Data_Definition_Error_glue_object = Feature_Data_Definition_Error_glue()
        self.log("Scenario_Simple_Table_with_double_bad")

        object_list2 : List[ATest] = [
            ATest.Builder()
                .setAnint("1")
                .setAstring("something")
                .setAdouble("r")
                .build()
            ]
        feature_Data_Definition_Error_glue_object.Given_table_is(object_list2)

    def test_Scenario_Simple_Table_with_initializer_bad(self):
        feature_Data_Definition_Error_glue_object = Feature_Data_Definition_Error_glue()
        self.log("Scenario_Simple_Table_with_initializer_bad")

        object_list3 : List[ATestBad] = [
            ATestBad.Builder()
                .setAnint("1")
                .build()
            ]
        feature_Data_Definition_Error_glue_object.Given_table_is_bad_initializer(object_list3)

