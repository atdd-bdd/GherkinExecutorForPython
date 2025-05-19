Feature: Import

# creates the import statements for all the files (including the data files) 

Import 
| Datatype    | ConversionMethod                               | Import                 | Notes                 |
| DayOfWeek   |  (DayOfWeek)Enum.Parse(typeof(DayOfWeek), $)   |                        | Enum that is created  |
| BigInteger  | BigInteger.Parse($)                            | System.Numerics        |                       |

Data ImportData 
| Name       | Default             | Datatype      | Notes           |
| myWeekday  | Monday              | DayOfWeek     | Uses an enum    |
| myBigInt   | 1                   | BigInteger    | Uses import     |


Scenario: Use an import
Given this data should be okay # ListOfObject ImportData 
| myWeekday  | myBigInt     |
| Monday     | 1            |
| Sunday     | 10000000000  |


Scenario: Should fail 
Given this data should fail # ListOfObject ImportData 
| myWeekday  | myBigInt  |
| Humpday    | 1         |
| Sunday     | 2         |

Scenario: Should also fail
Given this data should fail # ListOfObject ImportData 
| myWeekday  | myBigInt  |
| Monday     | 1         |
| Sunday     | A.2       |


