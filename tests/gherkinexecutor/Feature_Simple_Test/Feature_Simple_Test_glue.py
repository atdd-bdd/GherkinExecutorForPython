from tests.gherkinexecutor.Feature_Simple_Test.ATest import ATest
from tests.gherkinexecutor.Feature_Simple_Test.ATestInternal import ATestInternal

from typing import List


class Feature_Simple_Test_glue:
    DNCString = "?DNC?"

    def Given_table_is(self, values: List[ATest]) -> None:
        print("---  " + "Given_table_is")
        for value in values:
            print(value)
            # Add calls to production code and asserts
            i = value.to_ATestInternal()
            print(i)
