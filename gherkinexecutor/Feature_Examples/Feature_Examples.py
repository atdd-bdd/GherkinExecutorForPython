import unittest


from gherkinexecutor.Feature_Examples.TemperatureCalculation import TemperatureCalculation
from gherkinexecutor.Feature_Examples.FilterValue import FilterValue
from gherkinexecutor.Feature_Examples.ResultValue import ResultValue
from gherkinexecutor.Feature_Examples.LabelValue import LabelValue
from gherkinexecutor.Feature_Examples.ValueValid import ValueValid
from gherkinexecutor.Feature_Examples.Feature_Examples_glue import FeatureExamplesGlue


class FeatureExamples(unittest.TestCase):

    def test_Scenario_Temperature(self):
        feature_examples_glue_object = FeatureExamplesGlue()

        objectList1 = [
            TemperatureCalculation.Builder().setf("32").setc("0").setnotes("Freezing").build(),
            TemperatureCalculation.Builder().setf("212").setc("100").setnotes("Boiling").build(),
            TemperatureCalculation.Builder().setf("-40").setc("-40").setnotes("Below zero").build()
        ]
        feature_examples_glue_object.Calculation_Convert_F_to_C(objectList1)

    def test_Scenario_Domain_Term_ID(self):
        feature_examples_glue_object = FeatureExamplesGlue()

        objectList1 = [
            ValueValid.Builder().setvalue("Q1234").setvalid("true").setnotes("").build(),
            ValueValid.Builder().setvalue("Q123").setvalid("false").setnotes("Too short").build(),
            ValueValid.Builder().setvalue("Q12345").setvalid("false").setnotes("Too long").build(),
            ValueValid.Builder().setvalue("A1234").setvalid("false").setnotes("Must begin with Q").build()
        ]
        feature_examples_glue_object.Rule_ID_must_have_exactly_5_letters_and_begin_with_Q(objectList1)

    def test_Scenario_Filter_Data(self):
        feature_examples_glue_object = FeatureExamplesGlue()

        objectList1 = [
            LabelValue.Builder().setiD("Q1234").setvalue("1").build(),
            LabelValue.Builder().setiD("Q9999").setvalue("2").build(),
            LabelValue.Builder().setiD("Q1234").setvalue("3").build()
        ]
        feature_examples_glue_object.Given_list_of_numbers(objectList1)

        stringListList2 = [
            ["Q1234"]
        ]
        feature_examples_glue_object.When_filtered_by_ID_with_value(stringListList2)

        stringListList3 = [
            ["4"]
        ]
        feature_examples_glue_object.Then_sum_is(stringListList3)

    def test_Scenario_Filter_Data_Another_Way(self):
        feature_examples_glue_object = FeatureExamplesGlue()

        objectList1 = [
            LabelValue.Builder().setiD("Q1234").setvalue("1").build(),
            LabelValue.Builder().setiD("Q9999").setvalue("2").build(),
            LabelValue.Builder().setiD("Q1234").setvalue("3").build()
        ]
        feature_examples_glue_object.Given_list_of_numbers(objectList1)

        # objectList2 = [
        #     FilterValue.Builder().setname("ID").setvalue("Q1234").build()
        # ]
        # feature_examples_glue_object.When_filtered_by(objectList2)

        objectList3 = [
            ResultValue.Builder().setsum("4").build()
        ]
        feature_examples_glue_object.Then_result(objectList3)
