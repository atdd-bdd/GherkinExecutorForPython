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


# will create an internal class name 
Data ATest 
| Name     | Default  | Datatype  | Note  |
| anInt    | 0        | Int       |       |
| aString  | ~        | String    |       |
| aDouble  | 4.0      | Double    |       |

# will create a .tmpl file for Existing 

Data TestIn Existing 
| Name    | Default  | Datatype  | Note  |
| aValue  | 0        | int       |       |
| bValue  | ~        | String    |       |
| cValue  | 4.0      | double    |       |

Data AllTypes
| Name            | Default  | DataType  | Note       |
| anInt           | 0        | int       | primitive  |
| aByte           | 0        | byte      | primitive  |
| aSByte          | 0        | sbyte     | primitive  |
| AShort          | 0        | short     | primitive  |
| AUshort         | 0        | ushort    | primitive  |
| AUint           | 0        | uint      | primitive  |
| aLong           | 0        | long      | primitive  |
| aUlong          | 0        | ulong     | primitive  |
| aFloat          | 0.0      | float     | primitive  |
| aDouble         | 0.0      | double    | primitive  |
| aDecimal        | 0.0      | decimal   | primitive  |
| aBool           | false    | bool      | primitive  |
| aString         |          | string    | primitive  |
| aChar           | 0        | char      | primitive  |
| anIntObject     | 0        | Int32     |            |
| aByteObject     | 0        | Byte      |            |
| aSByteObject    | 0        | SByte     |            |
| aShortObject    | 0        | Int16     |            |
| AUshortObject   | 0        | UInt16    |            |
| AUintObject     | 0        | UInt32    |            |
| aLongObject     | 0        | Int64     |            |
| aUlongObject    | 0        | UInt64    |            |
| aFloatObject    | 0.0      | Single    |            |
| aDoubleObject   | 0.0      | Double    |            |
| aDecimalObject  | 0.0      | Decimal   |            |
| aBoolObject     | false    | Boolean   |            |
| aStringObjet    |          | String    |            |
| aCharObject     | 0        | Char      |            |


