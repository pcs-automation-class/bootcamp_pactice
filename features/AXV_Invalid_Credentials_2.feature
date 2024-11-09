# Created by Anna at 11/8/24
Feature: Login Page Tests
  # Login with invalid credentials
  Background:
    Given Open "dev" environment

  Scenario Outline: Login with Invalid Credentials
    Then Type "<username>" into "//input[@name='username']"
    Then Type "<password>" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"
    Examples:
      | username                  | password         |
      | test.axv.2000@gmail.cot   | KgkbAz7RHCoVD7RA |
      | test.axv.2001@gmail.com   | W2kxy6tZf9oXzwC  |