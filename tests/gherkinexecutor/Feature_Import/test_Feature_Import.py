import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Import import *
from tests.gherkinexecutor.Feature_Import.Feature_Import_glue import Feature_Import_glue


class Feature_Import(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def test_Scenario_Use_an_import(self):
        feature_Import_glue_object = Feature_Import_glue()
        self.log("Scenario_Use_an_import")

        object_list1 : List[ImportData] = [
            ImportData.Builder()
                .setMydate("2025-05-26")
                .setColor("BLUE")
                .build()
            ,ImportData.Builder()
                .setMydate("2025-05-27")
                .setColor("GREEN")
                .build()
            ]
        feature_Import_glue_object.Given_this_data_should_be_okay(object_list1)

    def test_Scenario_Should_fail(self):
        feature_Import_glue_object = Feature_Import_glue()
        self.log("Scenario_Should_fail")

        object_list2 : List[ImportData] = [
            ImportData.Builder()
                .setMydate("2025-02-30")
                .build()
            ]
        feature_Import_glue_object.Given_this_data_should_fail(object_list2)

