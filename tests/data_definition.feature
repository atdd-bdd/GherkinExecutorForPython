Feature: Data Definition


Scenario Simple Comparison 
Given table is # ListOfObject ATest 
| anInt  | aString    | aDouble  |
| 1      | something  | 1.2      |
When compared to # ListOfObject ATest Compare 
| aString    | 
| something  | 
Then result is 
| true | 
When compared to # ListOfObject ATest Compare 
| aString         | 
| something else  | 
Then result is 
| false| 


# Will create an internal class name
# This uses generic names for the data types
Data ATest 
| Name     | Default  | Datatype  | Note  |
| anInt    | 0        | Integer   |       |
| aString  | ~        | String    |       |
| aDouble  | 4.0      | Double    |       |

# will create a .tmpl file for Existing 

Data TestIn Existing 
| Name    | Default  | Datatype  | Note  |
| aValue  | 0        | int       |       |
| bValue  | ~        | str       |       |
| cValue  | 4.0      | float     |       |

Scenario: Check All Types
Given these are all the types  # ListOfObject AllTypes  
| anInt  | aFloat  | aBool  | aString  | aComplex  |
| 0      | 0.0     | false  |          | 0+0j      |


Data AllTypes
| Name            | Default  | DataType  | Note       |
| anInt           | 0        | int       | primitive  |
| aFloat          | 0.0      | float     | primitive  |
| aBool           | false    | bool      | primitive  |
| aString         |          | str       | primitive  |
| aComplex        | 0+0j     | complex   | primitive  |


