Feature: Forth

This is an example of using Gherkin to demonstrate a Forth interpreter 

Scenario: Individual Instructions
Given stack starts as
| 2 5 7 |
When word is input then stack becomes # ListOfObject WordStack
| Word  | Stack    | Notes                                                            |
| DUP   | 2 5 7 7  | Duplicates the top element (.. A -> .. A A)                      |
| SWAP  | 2 7 5    | Swaps the top two elements of the stack.                         |
| OVER  | 2 5 7 5  | Copies the second element from the top of the stack to the top.  |
| ROT   | 5 7 2    | Rotates the third element to the top.                            |
| DROP  | 2 5      | Removes the top element of the stack                             |
| +     | 2 12     | Adds the top two elements of the stack.                          |
| *     | 2 35     | Multiplies the top two elements of the stack.                    |
| -     | 2 -2     | Subtracts the top element from the second top element.           |

Scenario: Sequence of Input 
* Given an input, what the stack becomes # ListOfObject InputStack 
| Input  | Stack      |
| 2 5 7  | 2 5 7      |
| DUP    | 2 5 7 7    |
| SWAP   | 2 5 7 7    |
| OVER   | 2 5 7 7 7  |
| ROT    | 2 5 7 7 7  |  
| DROP   | 2 5 7 7    |
| +      | 2 5 14     |
| *      | 2 78       |

Scenario: Example Program 
# https://www.forth.com/starting-forth/12-forth-code-example/
# 15 FOOT  2 INCH  PILE  as example input 
* Given this input 
"""
\ "No Weighting" from Starting Forth Chapter 12
VARIABLE DENSITY
VARIABLE THETA
VARIABLE ID

: " ( -- addr )   [CHAR] " WORD DUP C@ 1+ ALLOT ;

: MATERIAL ( addr n1 n2 -- )    \ addr=string, n1=density, n2=theta
   CREATE  , , , 
   DOES> ( -- )   DUP @ THETA !
   CELL+ DUP @ DENSITY !  CELL+ @ ID ! ;

: .SUBSTANCE ( -- )   ID @ COUNT TYPE ;
: FOOT ( n1 -- n2 )   10 * ;
: INCH ( n1 -- n2 )   100 12 */  5 +  10 /  + ;
: /TAN ( n1 -- n2 )   1000 THETA @ */ ;

: PILE ( n -- )         \ n=scaled height
   DUP DUP 10 */ 1000 */  355 339 */  /TAN /TAN
   DENSITY @ 200 */  ." = " . ." tons of "  .SUBSTANCE ;

\ table of materials
\   string-address  density  tan[theta] 
   " cement"           131        700  MATERIAL CEMENT
   " loose gravel"      93        649  MATERIAL LOOSE-GRAVEL
   " packed gravel"    100        700  MATERIAL PACKED-GRAVEL
   " dry sand"          90        754  MATERIAL DRY-SAND
   " wet sand"         118        900  MATERIAL WET-SAND
   " clay"             120        727  MATERIAL CLAY
""" 
* Given an input, this is the output # ListOfObject InputOutput
| Input                | Output               |
| CEMENT               |                      |
| 10 FOOT PILE         | 138 tons of cement   |
| 10 FOOT 3 INCH PILE  | 151 tons of cement   |
| DRY-SAND             |                      |
| 10 FOOT PILE         | 81 tons of dry sand  |

Data InputOutput 
| Name    | Default  |
| Input   |          |
| Output  |          |

Data WordStack 
| Name   | Default  |
| Word   |          |
| Stack  |          |
| Notes  |          |

Data InputStack
| Name   | Default  |
| Input  |          |
| Stack  |          |
| Notes |           |

