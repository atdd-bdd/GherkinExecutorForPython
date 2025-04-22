import unittest

from Feature_Simple_Test_glue import FeatureSimpleTestGlue

class FeatureSimpleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.feature_simple_test_glue_object = FeatureSimpleTestGlue()

    def test_scenario_simple(self):
        object_list1 = [
            ATest(
                an_int="1",
                a_string="something",
                a_double="1.2"
            )
        ]
        self.feature_simple_test_glue_object.given_table_is(object_list1)


if __name__ == '__main__':
    unittest.main()
