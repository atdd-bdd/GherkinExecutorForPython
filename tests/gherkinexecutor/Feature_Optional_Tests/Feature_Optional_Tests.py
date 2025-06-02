import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Optional_Tests import *
from tests.gherkinexecutor.Feature_Optional_Tests.Feature_Optional_Tests_glue import Feature_Optional_Tests_glue


class TestFeature_Optional_Tests(unittest.TestCase): 


    def test_Scenario_This_will_always_be_run(self): 
        feature_Optional_Tests_glue_object = Feature_Optional_Tests_glue()

        feature_Optional_Tests_glue_object.Given_This_will_always_be_run()

    def test_Scenario_This_may_be_run(self): 
        feature_Optional_Tests_glue_object = Feature_Optional_Tests_glue()

        feature_Optional_Tests_glue_object.Given_This_may_be_run()

    @unittest.skip("Skipping this test")

    def test_Scenario_This_will_be_run_if_tag(self): 
        feature_Optional_Tests_glue_object = Feature_Optional_Tests_glue()

        feature_Optional_Tests_glue_object.Given_This_will_be_run_if_tag()

