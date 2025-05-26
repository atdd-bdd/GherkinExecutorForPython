Feature: Json

Scenario: Convert to Json 
Given one object is # ListOfObject SimpleClass
| anInt  | aString  |
| 1      | B        |
Then Json should be 
"""
{"anInt": "1","aString": "B"}
"""

Scenario: Convert from Json
Given Json is
"""
{anInt:  "1"   ,   aString:"B"  }
"""
Then the converted object is # ListOfObject SimpleClass
| anInt  | aString  |
| 1      | B        |

Scenario: Convert to Json Array
Given a table is # ListOfObject SimpleClass
| anInt  | aString  |
| 1      | B        |
| 2      | C        |
Then Json for table should be 
"""
[ {"anInt": "1","aString": "B"} 
, {"anInt": "2","aString": "C"} 
]
"""

Scenario: Convert from Json Array
Given Json for table is
"""
[    {anInt:  "1"   ,   aString:"B"  },
{anInt:  "2"   ,   aString:"C"  }
]

"""
Then the converted table should be # ListOfObject SimpleClass
| anInt  | aString  |
| 1      | B        |
| 2      | C        |



Data SimpleClass
| Name     | Default  | Datatype  |
| anInt    | 0        | Integer   |
| aString  | Q        | String    |

