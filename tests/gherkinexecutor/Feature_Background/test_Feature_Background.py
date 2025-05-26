import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Background import *
from tests.gherkinexecutor.Feature_Background.Feature_Background_glue import Feature_Background_glue


class Feature_Background(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def background(self, feature_Background_glue_object):
        self.log("background")

        string_list_list1 = [
            [
            "Background Here"
            ]
            ]
        feature_Background_glue_object.Given_Background_function_sets_a_value(string_list_list1)

    def cleanup(self, feature_Background_glue_object):
        self.log("cleanup")

        string_list_list2 = [
            [
            "Cleanup Here"
            ]
            ]
        feature_Background_glue_object.Given_value_for_cleanup_should_be_set_to(string_list_list2)

    def test_Scenario_Should_have_Background_and_Cleanup(self):
        feature_Background_glue_object = Feature_Background_glue()
        self.log("Scenario_Should_have_Background_and_Cleanup")
        self.background(feature_Background_glue_object)

        feature_Background_glue_object.Given_a_regular_function()

        string_list_list4 = [
            [
            "Background Here"
            ]
            ]
        feature_Background_glue_object.Then_background_should_set_value_to(string_list_list4)

        string_list_list5 = [
            [
            "Cleanup Here"
            ]
            ]
        feature_Background_glue_object.And_set_a_value_for_cleanup(string_list_list5)
        self.cleanup(feature_Background_glue_object) # from previous

    def test_Scenario_Should_also_have_Background_and_Cleanup(self):
        feature_Background_glue_object = Feature_Background_glue()
        self.log("Scenario_Should_also_have_Background_and_Cleanup")
        self.background(feature_Background_glue_object)

        feature_Background_glue_object.Given_a_regular_function()

        string_list_list7 = [
            [
            "Background Here"
            ]
            ]
        feature_Background_glue_object.Then_background_should_set_value_to(string_list_list7)

        string_list_list8 = [
            [
            "Cleanup Here"
            ]
            ]
        feature_Background_glue_object.And_set_a_value_for_cleanup(string_list_list8)
        self.cleanup(feature_Background_glue_object) # at the end

