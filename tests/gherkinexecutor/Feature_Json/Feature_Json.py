import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Json import *
from tests.gherkinexecutor.Feature_Json.Feature_Json_glue import Feature_Json_glue


class TestFeature_Json(unittest.TestCase): 


    def test_Scenario_Convert_to_Json(self): 
        feature_Json_glue_object = Feature_Json_glue()

        object_list1: List[SimpleClass] = [
            SimpleClass.Builder()
                .setAnint("1")
                .setAstring("B")
                .build()
            ]
        feature_Json_glue_object.Given_one_object_is(object_list1)

        string2 ="""
{"anInt": "1","aString": "B"}
""".strip()
        feature_Json_glue_object.Then_Json_should_be(string2)

    def test_Scenario_Convert_from_Json(self): 
        feature_Json_glue_object = Feature_Json_glue()

        string3 ="""
{anInt:  "1"   ,   aString:"B"  }
""".strip()
        feature_Json_glue_object.Given_Json_is(string3)

        object_list4: List[SimpleClass] = [
            SimpleClass.Builder()
                .setAnint("1")
                .setAstring("B")
                .build()
            ]
        feature_Json_glue_object.Then_the_converted_object_is(object_list4)

    def test_Scenario_Convert_to_Json_Array(self): 
        feature_Json_glue_object = Feature_Json_glue()

        object_list5: List[SimpleClass] = [
            SimpleClass.Builder()
                .setAnint("1")
                .setAstring("B")
                .build()
            ,SimpleClass.Builder()
                .setAnint("2")
                .setAstring("C")
                .build()
            ]
        feature_Json_glue_object.Given_a_table_is(object_list5)

        string6 ="""
[ {"anInt": "1","aString": "B"}
, {"anInt": "2","aString": "C"}
]
""".strip()
        feature_Json_glue_object.Then_Json_for_table_should_be(string6)

    def test_Scenario_Convert_from_Json_Array(self): 
        feature_Json_glue_object = Feature_Json_glue()

        string7 ="""
[    {anInt:  "1"   ,   aString:"B"  },
{anInt:  "2"   ,   aString:"C"  }
]
""".strip()
        feature_Json_glue_object.Given_Json_for_table_is(string7)

        object_list8: List[SimpleClass] = [
            SimpleClass.Builder()
                .setAnint("1")
                .setAstring("B")
                .build()
            ,SimpleClass.Builder()
                .setAnint("2")
                .setAstring("C")
                .build()
            ]
        feature_Json_glue_object.Then_the_converted_table_should_be(object_list8)

