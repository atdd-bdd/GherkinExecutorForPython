Feature: Import

# creates the import statements for all the files (including the data files) 

Import 
| Datatype  | ConversionMethod           | Import                                   | Notes                          |
| datetime  | datetime.fromisoformat($)  | from datetime import datetime            |                                |
| Color     | Color[$]                   | from tests.gherkinexecutor.Feature_Import.Color import Color | Should import from production  |

Data ImportData 
| Name    | Default     | Datatype  | Notes  |
| myDate  | 1900-01-21  | datetime  |        |
| color   | RED         | Color     |        |


Scenario: Use an import
Given this data should be okay # ListOfObject ImportData 
| myDate      | color  |
| 2025-05-26  | BLUE   |
| 2025-05-27  | GREEN  |


Scenario: Should fail 
Given this data should fail # ListOfObject ImportData 
| myDate     |
| 2025-02-30 |



