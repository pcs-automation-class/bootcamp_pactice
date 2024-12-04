# Created by alisawinston at 11/6/24
Feature: # Login page tests
  # Examples of login page tests
  Background:
    Given Open "dev" environment
    Then Verify presence of element "//h5[text()='Login to Your Account']"
Feature: # Login page tests
  # Examples of login page tests

  Scenario: Login w correct credentials
    Then Type "alisawins7+gear@gmail.com" into "//input[@name='username']"
    Then wait 1 seconds
    Then Type "aVhTpLSLF2TSKi4Y" into "//input [@name='password' ]"
    Then Wait 1 seconds
    Then Click element "//button[text()=' Login ']"
    Then Verify presence of element "//h3[text()=' Your device ']"

  Scenario Outline: Login w incorrect credentials
    Then Type "<username>" into "//input[@name='username']"
    Then wait 1 seconds
    Then Type "<password>" into "//input [@name='password' ]"
    Then Wait 1 seconds
    Then Click element "//button[text()=' Login ']"
    Then Verify presence of element "//p[text()='Invalid username or password']"
    Examples:
      | username | password |
      | notgooduser@gmail.com | aVhTpLSLF2TSKi4Y |
      | user3invalid@gmail.com | aVhTpLSLF2TSKi4Y|
      | user4invalid@gmail.com | aVhTpLSLF2TSKi4Y |
  Scenario: Login w correct credentials
    Given Open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.Linkmygear.com"
    Then Wait 3 seconds
    Then Verify presence of element "//h5[text()='Login to Your Account']"
    Then Wait 3 seconds

