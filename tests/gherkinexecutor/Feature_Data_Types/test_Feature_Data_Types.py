import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Data_Types import *
from tests.gherkinexecutor.Feature_Data_Types.Feature_Data_Types_glue import Feature_Data_Types_glue


class Feature_Data_Types(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def test_Scenario_Use_the_data_types(self):
        feature_Data_Types_glue_object = Feature_Data_Types_glue()
        self.log("Scenario_Use_the_data_types")

        object_list1 : List[SomeTypes] = [
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
        feature_Data_Types_glue_object.Given_type_values_are(object_list1)

        object_list2 : List[SomeTypes] = [
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
        feature_Data_Types_glue_object.Then_this_should_be_equal(object_list2)

