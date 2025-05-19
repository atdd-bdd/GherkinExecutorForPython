import unittest
from typing import List
from tests.gherkinexecutor.Feature_Starting.FandC import FandC
from tests.gherkinexecutor.Feature_Starting.FandCInternal import FandCInternal

from tests.gherkinexecutor.Feature_Starting.Feature_Starting_glue import Feature_Starting_glue


class Feature_Starting(unittest.TestCase):

    def log(value):
       try:
           with open("log.txt", "a") as my_log:
               my_log.write(value + "\n")
       except IOError:
           print("*** Cannot write to log", file=sys.stderr)
    
    @staticmethod
    def test_Scenario_Temperature_Conversion():
        feature_Starting_glue_object = Feature_Starting_glue()
        log("Scenario_Temperature_Conversion");

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

