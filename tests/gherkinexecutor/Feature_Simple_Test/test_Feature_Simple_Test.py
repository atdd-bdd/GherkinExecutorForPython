import unittest
from typing import List
from tests.gherkinexecutor.Feature_Simple_Test import *
from tests.gherkinexecutor.Feature_Simple_Test.Feature_Simple_Test_glue import Feature_Simple_Test_glue


class Feature_Simple_Test(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    
    def test_Scenario_Simple(self):
        feature_Simple_Test_glue_object = Feature_Simple_Test_glue()
        self.log("Scenario_Simple");

        object_list1 : List[ATest] = [
            ATest.Builder()
                .setAnint("1")
                .setAstring("something")
                .setAdouble("1.2")
                .build()
            ]
        feature_Simple_Test_glue_object.Given_table_is(object_list1)

