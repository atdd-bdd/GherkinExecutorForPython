Feature: Optional Tests

Scenario: This will always be run 
Given This will always be run

Scenario: This may be run  # InDev OnlyThis 
Given This may be run

@unittest.skip("Skipping this test")
Scenario: This will be run if tag
Given This will be run if tag 
