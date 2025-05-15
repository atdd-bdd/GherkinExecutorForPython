import unittest

from tests.gherkinexecutor.Feature_Simple_Test.Feature_Simple_Test_glue import FeatureSimpleTestGlue
from tests.gherkinexecutor.Feature_Simple_Test.ATest import ATest


class FeatureSimpleTest(unittest.TestCase):


    def test_scenario_simple(self):

        feature_simple_test_glue_object = FeatureSimpleTestGlue()

        object_list1 = [
            ATest(
                an_int="1",
                a_string="something",
                a_double="1.2"
            )
        ]
        feature_simple_test_glue_object.given_table_is(object_list1)


if __name__ == '__main__':
    unittest.main()
