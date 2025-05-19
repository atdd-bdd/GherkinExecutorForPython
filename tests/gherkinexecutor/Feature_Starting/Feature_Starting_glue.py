from tests.gherkinexecutor.Feature_Starting.FandC import FandC
from tests.gherkinexecutor.Feature_Starting.FandCInternal import FandCInternal

from typing import List

class Feature_Starting_glue :
    DNCString = "?DNC?"


    def Calculation_Convert_F_to_C(self, values: List[FandC]) -> None:
        print("---  " + "Calculation_Convert_F_to_C")
        for value in values:
            print(value)
             # Add calls to production code and asserts
            i = value.to_FandCInternal()
        raise NotImplementedError("Must implement")

