import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Optional_Tests import *
from tests.gherkinexecutor.Feature_Optional_Tests.Feature_Optional_Tests_glue import Feature_Optional_Tests_glue


class Feature_Optional_Tests(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def test_Scenario_This_will_always_be_run(self):
        feature_Optional_Tests_glue_object = Feature_Optional_Tests_glue()
        self.log("Scenario_This_will_always_be_run")

        feature_Optional_Tests_glue_object.Given_This_will_always_be_run()

    def test_Scenario_This_may_be_run(self):
        feature_Optional_Tests_glue_object = Feature_Optional_Tests_glue()
        self.log("Scenario_This_may_be_run")

        feature_Optional_Tests_glue_object.Given_This_may_be_run()

    @unittest.skip("Skipping this test")

    def test_Scenario_This_will_be_run_if_tag(self):
        feature_Optional_Tests_glue_object = Feature_Optional_Tests_glue()
        self.log("Scenario_This_will_be_run_if_tag")

        feature_Optional_Tests_glue_object.Given_This_will_be_run_if_tag()

