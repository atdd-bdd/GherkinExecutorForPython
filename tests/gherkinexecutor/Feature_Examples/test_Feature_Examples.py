import unittest
from typing import List
from tests.gherkinexecutor.Feature_Examples import *
from tests.gherkinexecutor.Feature_Examples.Feature_Examples_glue import Feature_Examples_glue


class Feature_Examples(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    
    def test_Scenario_Temperature_Conversion(self):
        feature_Examples_glue_object = Feature_Examples_glue()
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
        feature_Examples_glue_object.Calculation_Convert_F_to_C(object_list1)
    def test_Scenario_Domain_Term_ID(self):
        feature_Examples_glue_object = Feature_Examples_glue()
        self.log("Scenario_Domain_Term_ID");

        object_list2 : List[ValueValid] = [
            ValueValid.Builder()
                .setValue("Q1234")
                .setValid("true")
                .setNotes("")
                .build()
            ,ValueValid.Builder()
                .setValue("Q123")
                .setValid("false")
                .setNotes("Too short")
                .build()
            ,ValueValid.Builder()
                .setValue("Q12345")
                .setValid("false")
                .setNotes("Too long")
                .build()
            ,ValueValid.Builder()
                .setValue("A1234")
                .setValid("false")
                .setNotes("Must begin with Q")
                .build()
            ]
        feature_Examples_glue_object.Rule_ID_must_have_exactly_5_letters_and_begin_with_Q(object_list2)
    def test_Scenario_Filter_Data(self):
        feature_Examples_glue_object = Feature_Examples_glue()
        self.log("Scenario_Filter_Data");

        object_list3 : List[LabelValue] = [
            LabelValue.Builder()
                .setId("Q1234")
                .setValue("1")
                .build()
            ,LabelValue.Builder()
                .setId("Q9999")
                .setValue("2")
                .build()
            ,LabelValue.Builder()
                .setId("Q1234")
                .setValue("3")
                .build()
            ]
        feature_Examples_glue_object.Given_list_of_numbers(object_list3)

        string_list_list4 = [
            [
            "Q1234"
            ]
            ]
        feature_Examples_glue_object.When_filtered_by_ID_with_value(string_list_list4)

        string_list_list5 = [
            [
            "4"
            ]
            ]
        feature_Examples_glue_object.Then_sum_is(string_list_list5)
    def test_Scenario_Filter_Data_Another_Way(self):
        feature_Examples_glue_object = Feature_Examples_glue()
        self.log("Scenario_Filter_Data_Another_Way");

        object_list6 : List[LabelValue] = [
            LabelValue.Builder()
                .setId("Q1234")
                .setValue("1")
                .build()
            ,LabelValue.Builder()
                .setId("Q9999")
                .setValue("2")
                .build()
            ,LabelValue.Builder()
                .setId("Q1234")
                .setValue("3")
                .build()
            ]
        feature_Examples_glue_object.Given_list_of_numbers(object_list6)

        object_list7 : List[FilterValue] = [
            FilterValue.Builder()
                .setValue("Q1234")
                .build()
            ]
        feature_Examples_glue_object.When_filtered_by(object_list7)

        object_list8 : List[ResultValue] = [
            ResultValue.Builder()
                .setSum("4")
                .build()
            ]
        feature_Examples_glue_object.Then_result(object_list8)

