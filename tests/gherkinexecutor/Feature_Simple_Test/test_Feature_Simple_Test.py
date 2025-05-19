import unittest
from typing import List
from tests.gherkinexecutor.Feature_Simple_Test.ATest import ATest
from tests.gherkinexecutor.Feature_Simple_Test.ATestInternal import ATestInternal

from tests.gherkinexecutor.Feature_Simple_Test.Feature_Simple_Test_glue import Feature_Simple_Test_glue


class Feature_Simple_Test(unittest.TestCase):

    @staticmethod
    def log(value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)

    @staticmethod
    def test_Scenario_Simple():
        feature_Simple_Test_glue_object = Feature_Simple_Test_glue()
        Feature_Simple_Test.log("Scenario_Simple");

        object_list1: List[ATest] = [
            ATest.Builder()
            .setAnint("1")
            .setAstring("something")
            .setAdouble("1.2")
            .build()
        ]
        feature_Simple_Test_glue_object.Given_table_is(object_list1)
