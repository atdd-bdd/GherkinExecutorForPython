import unittest
from typing import List
from tests.gherkinexecutor.Feature_Simple_Test.ATest import ATest
from tests.gherkinexecutor.Feature_Simple_Test.ATestInternal import ATestInternal

from tests.gherkinexecutor.Feature_Simple_Test.Feature_Simple_Test_glue import Feature_Simple_Test_glue


class Feature_Simple_Test(unittest.TestCase):

    @staticmethod
    def test_Scenario_Simple():
        feature_Simple_Test_glue_object = Feature_Simple_Test_glue()

        object_list1 : List[ATest] = [
            ATest.Builder()
                .setAnint("1")
                .setAstring("something")
                .setAdouble("1.2")
                .build()
            ]
        feature_Simple_Test_glue_object.Given_table_is(object_list1)

