Feature: Test Feature

Scenario Include something 
Given local include
"""
Include "string.inc"
"""
Then string equals
"""
This is an include string from the local directory
"""
Given global include
"""
Include 'string.inc' 
"""
Then string equals 
"""
This is an include string from the main directory
"""

