import unittest
from typing import List
from tests.gherkinexecutor.Feature_Starting import *
from tests.gherkinexecutor.Feature_Starting.Feature_Starting_glue import Feature_Starting_glue


class Feature_Starting(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    
    def test_Scenario_Temperature_Conversion(self):
        feature_Starting_glue_object = Feature_Starting_glue()
        self.log("Scenario_Temperature_Conversion");

        object_list1 : List[FandC] = [
            FandC.Builder()
                .setF("32")
                .setC("0")
                .setNotes("Freezing")
                .build()
            ,FandC.Builder()
                .setF("212")
                .setC("100")
                .setNotes("Boiling")
                .build()
            ,FandC.Builder()
                .setF("-40")
                .setC("-40")
                .setNotes("Below zero")
                .build()
            ]
        feature_Starting_glue_object.Calculation_Convert_F_to_C(object_list1)

