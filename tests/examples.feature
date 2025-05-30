
Feature: Examples

Scenario: Temperature Conversion
# Could use * or Rule instead of Calculation
Calculation Convert F to C # ListOfObject FandC
| F    | C    | Notes       |
| 32   | 0    | Freezing    |
| 212  | 100  | Boiling     |
| -40  | -40  | Below zero  |

Data FandC
| Name   | Default  | DataType  | Notes  |
| F      | 0        | Integer   |        |
| C      | 0        | Integer   |        |
| Notes  |          | String    |        |

Scenario: Domain Term ID 
Rule ID must have exactly 5 letters and begin with Q # ListOfObject ValueValid
| Value   | Valid  | Notes              |
| Q1234   | true   |                    |
| Q123    | false  | Too short          |
| Q12345  | false  | Too long           |
| A1234   | false  | Must begin with Q  |

Data ValueValid
| Name   | Default  | DataType  |
| Value  | 0        | String    |
| Valid  | false    | Boolean   |
| Notes  |          | String    |

Scenario: Filter Data 
# filters data 
Given list of numbers # ListOfObject LabelValue 
| ID     | Value  |
| Q1234  | 1      |
| Q9999  | 2      |
| Q1234  | 3      |
When filtered by ID with value
| Q1234  |
Then sum is 
| 4 | 

Scenario: Filter Data Another Way  
# filters data 
Given list of numbers # ListOfObject LabelValue
| ID     | Value  |
| Q1234  | 1      |
| Q9999  | 2      |
| Q1234  | 3      |
When filtered by # ListOfObject FilterValue transpose
| Value  | Q1234  |
Then result # ListOfObject ResultValue 
| Sum  |
| 4    |

* Data FilterValue
| Name   | Default  | DataType  | Notes  |
| Value  | Q0000    | ID        |        |

* Data ResultValue
| Name  | Default  | DataType  | Notes  |
| Sum   |          | Integer   |        |

* Data LabelValue
| Name   | Default  | DataType  | Notes  |
| ID     |          | ID        |        |
| Value  | 0        | Integer   |        |



