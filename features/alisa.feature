# Created by alisawinston at 11/6/24
Feature: # Login page tests
  # Examples of login page tests

  Scenario: Login w correct credentials
    Given Open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.Linkmygear.com"
    Then Wait 3 seconds
    Then Verify presence of element "//h5[text()='Login to Your Account']"
    Then Wait 3 seconds
    
