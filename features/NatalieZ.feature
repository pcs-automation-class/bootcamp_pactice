# Created by nati- at 11/2/2024
Feature: Login Page Tests
  # Examples of login page tests
  Background:
    Given Open "dev" environment
#    Then Verify presents of element "//h5[text()='Login to Your Account']"

  Scenario: Login with correct credentials
    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
    Then Type "1234567" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//h3[text()=' Your device ']"


  Scenario Outline: Login with incorrect user name
    Then Type "<username>" into "//input[@name='username']"
    Then Type "<password>" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"
    Examples:
      | username                      | password         |
      | pcs@gmail.com                 | hr9rsHU6TnWDYnpy |
      | pcs.automationclass@gmail.com | 1234567          |
      | pcs2@gmail.com                | hr9rsHU6TnWDYnpy |


  Scenario: Login with incorrect password
    Then Type "pcs.automationclass+1@gmail.com" into "//input[@name='username']"
    Then Type "2" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"
