import unittest
from typing import List
import sys
from tests.gherkinexecutor.Feature_Tic_Tac_Toe_Game import *
from tests.gherkinexecutor.Feature_Tic_Tac_Toe_Game.Feature_Tic_Tac_Toe_Game_glue import Feature_Tic_Tac_Toe_Game_glue


class Feature_Tic_Tac_Toe_Game(unittest.TestCase):

    def log(self, value):
        try:
            with open("log.txt", "a") as my_log:
                my_log.write(value + "\n")
        except IOError:
            print("*** Cannot write to log", file=sys.stderr)
    

    def test_Scenario_Make_a_move(self):
        feature_Tic_Tac_Toe_Game_glue_object = Feature_Tic_Tac_Toe_Game_glue()
        self.log("Scenario_Make_a_move")

        string_list_list1 = [
            [
            ""
            ,""
            ,""
            ]
            ,[
            ""
            ,""
            ,""
            ]
            ,[
            ""
            ,""
            ,""
            ]
            ]
        feature_Tic_Tac_Toe_Game_glue_object.Given_board_is(string_list_list1)

        object_list2 : List[Move] = [
            Move.Builder()
                .setRow("1")
                .setColumn("2")
                .setMark("X")
                .build()
            ]
        feature_Tic_Tac_Toe_Game_glue_object.When_move_is(object_list2)

        table3 = """
|   | X  |   |
|   |    |   |
|   |    |   |
""".strip()
        feature_Tic_Tac_Toe_Game_glue_object.Then_board_is_now(table3)

    def test_Scenario_Make_a_move_using_single_element(self):
        feature_Tic_Tac_Toe_Game_glue_object = Feature_Tic_Tac_Toe_Game_glue()
        self.log("Scenario_Make_a_move_using_single_element")

        string_list_list4 = [
            [
            ""
            ,""
            ,""
            ]
            ,[
            ""
            ,""
            ,""
            ]
            ,[
            ""
            ,""
            ,""
            ]
            ]
        feature_Tic_Tac_Toe_Game_glue_object.Given_board_is(string_list_list4)

        string_list_list5 = [
            [
            "1,2,X"
            ]
            ]
        feature_Tic_Tac_Toe_Game_glue_object.When_one_move_is(string_list_list5)

        table6 = """
|   | X  |   |
|   |    |   |
|   |    |   |
""".strip()
        feature_Tic_Tac_Toe_Game_glue_object.Then_board_is_now(table6)

    def test_Scenario_Make_multiple_moves(self):
        feature_Tic_Tac_Toe_Game_glue_object = Feature_Tic_Tac_Toe_Game_glue()
        self.log("Scenario_Make_multiple_moves")

        string_list_list7 = [
            [
            ""
            ,""
            ,""
            ]
            ,[
            ""
            ,""
            ,""
            ]
            ,[
            ""
            ,""
            ,""
            ]
            ]
        feature_Tic_Tac_Toe_Game_glue_object.Given_board_is(string_list_list7)

        object_list8 : List[Move] = [
            Move.Builder()
                .setRow("1")
                .setColumn("2")
                .setMark("X")
                .build()
            ,Move.Builder()
                .setRow("2")
                .setColumn("3")
                .setMark("O")
                .build()
            ]
        feature_Tic_Tac_Toe_Game_glue_object.When_moves_are(object_list8)

        table9 = """
|   | X  |    |
|   |    | O  |
|   |    |    |
""".strip()
        feature_Tic_Tac_Toe_Game_glue_object.Then_board_is_now(table9)

    def test_Scenario_check_the_prints_to_see_how_it_works(self):
        feature_Tic_Tac_Toe_Game_glue_object = Feature_Tic_Tac_Toe_Game_glue()
        self.log("Scenario_check_the_prints_to_see_how_it_works")

        string_list_list10 = [
            [
            "0"
            ,"x"
            ,"0"
            ]
            ,[
            "x"
            ,"0"
            ,"x"
            ]
            ,[
            "0"
            ,"x"
            ,"0"
            ]
            ]
        feature_Tic_Tac_Toe_Game_glue_object.Given_board_is(string_list_list10)

        table11 = """
| 0  | x  | 0  |
| x  | 0  | x  |
| 0  | x  | 0  |
""".strip()
        feature_Tic_Tac_Toe_Game_glue_object.Then_board_is_now(table11)

