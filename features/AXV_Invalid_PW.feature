# Created by Anna at 11/9/24
Feature: Login Page Tests
Background:
  Given Open "dev" environment

  Scenario: Login with invalid email
#    Given Open "dev" environment
    Then Wait 2 seconds
    Then Verify presents of element "//h5[text()='Login to Your Account']"
    Then Wait 1 seconds
    Then Type "test.axv.2000@gmail.com" into "//input[@name='username']"
    Then Wait 1 seconds
    Then Type "KgkbAz7RHCoVD7R" into "//input[@name='password']"
    Then Wait 1 seconds
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"

 Scenario Outline: Login with invalid email
    Then Type "<username>" into "//input[@name='username']"
    Then Type "<password>" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"
    Examples:
      | username                  | password        |
      | test.axv.2000@gmail.com   | KgkbAz7RHCoVD7R |
      | test.axv.2000+1@gmail.com | W2kxy6tZf9oXzwC |