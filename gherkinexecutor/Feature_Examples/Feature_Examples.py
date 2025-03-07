
import unittest

class TemperatureCalculation:
    def __init__(self, f, c, notes):
        self.f = f
        self.c = c
        self.notes = notes

    class Builder:
        def __init__(self):
            self.f = None
            self.c = None
            self.notes = None

        def f(self, f):
            self.f = f
            return self

        def c(self, c):
            self.c = c
            return self

        def notes(self, notes):
            self.notes = notes
            return self

        def build(self):
            return TemperatureCalculation(self.f, self.c, self.notes)

class ValueValid:
    def __init__(self, value, valid, notes):
        self.value = value
        self.valid = valid
        self.notes = notes

    class Builder:
        def __init__(self):
            self.value = None
            self.valid = None
            self.notes = None

        def value(self, value):
            self.value = value
            return self

        def valid(self, valid):
            self.valid = valid
            return self

        def notes(self, notes):
            self.notes = notes
            return self

        def build(self):
            return ValueValid(self.value, self.valid, self.notes)

class LabelValue:
    def __init__(self, iD, value):
        self.iD = iD
        self.value = value

    class Builder:
        def __init__(self):
            self.iD = None
            self.value = None

        def iD(self, iD):
            self.iD = iD
            return self

        def value(self, value):
            self.value = value
            return self

        def build(self):
            return LabelValue(self.iD, self.value)

class FilterValue:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    class Builder:
        def __init__(self):
            self.name = None
            self.value = None

        def name(self, name):
            self.name = name
            return self

        def value(self, value):
            self.value = value
            return self

        def build(self):
            return FilterValue(self.name, self.value)

class ResultValue:
    def __init__(self, sum):
        self.sum = sum

    class Builder:
        def __init__(self):
            self.sum = None

        def sum(self, sum):
            self.sum = sum
            return self

        def build(self):
            return ResultValue(self.sum)

class FeatureExamplesGlue:
    def Calculation_Convert_F_to_C(self, objectList1):
        pass

    def Rule_ID_must_have_exactly_5_letters_and_begin_with_Q(self, objectList1):
        pass

    def Given_list_of_numbers(self, objectList1):
        pass

    def When_filtered_by_ID_with_value(self, stringListList2):
        pass

    def Then_sum_is(self, stringListList3):
        pass

    def When_filtered_by(self, objectList2):
        pass

    def Then_result(self, objectList3):
        pass

class FeatureExamples(unittest.TestCase):

    def test_Scenario_Temperature(self):
        feature_examples_glue_object = FeatureExamplesGlue()

        objectList1 = [
            TemperatureCalculation.Builder().f("32").c("0").notes("Freezing").build(),
            TemperatureCalculation.Builder().f("212").c("100").notes("Boiling").build(),
            TemperatureCalculation.Builder().f("-40").c("-40").notes("Below zero").build()
        ]
        feature_examples_glue_object.Calculation_Convert_F_to_C(objectList1)

    def test_Scenario_Domain_Term_ID(self):
        feature_examples_glue_object = FeatureExamplesGlue()

        objectList1 = [
            ValueValid.Builder().value("Q1234").valid("true").notes("").build(),
            ValueValid.Builder().value("Q123").valid("false").notes("Too short").build(),
            ValueValid.Builder().value("Q12345").valid("false").notes("Too long").build(),
            ValueValid.Builder().value("A1234").valid("false").notes("Must begin with Q").build()
        ]
        feature_examples_glue_object.Rule_ID_must_have_exactly_5_letters_and_begin_with_Q(objectList1)

    def test_Scenario_Filter_Data(self):
        feature_examples_glue_object = FeatureExamplesGlue()

        objectList1 = [
            LabelValue.Builder().iD("Q1234").value("1").build(),
            LabelValue.Builder().iD("Q9999").value("2").build(),
            LabelValue.Builder().iD("Q1234").value("3").build()
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
            LabelValue.Builder().iD("Q1234").value("1").build(),
            LabelValue.Builder().iD("Q9999").value("2").build(),
            LabelValue.Builder().iD("Q1234").value("3").build()
        ]
        feature_examples_glue_object.Given_list_of_numbers(objectList1)

        objectList2 = [
            FilterValue.Builder().name("ID").value("Q1234").build()
        ]
        feature_examples_glue_object.When_filtered_by(objectList2)

        objectList3 = [
            ResultValue.Builder().sum("4").build()
        ]
        feature_examples_glue_object.Then_result(objectList3)
