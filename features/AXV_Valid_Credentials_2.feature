# Created by Anna at 11/8/24
Feature: Login Page Tests

Background:
  Given Open "dev" environment

Scenario Outline: Login with Correct Credentials
    Then Type "<username>" into "//input[@name='username']"
    Then Type "<password>" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//h3[text()=' Your device ']"
    Examples:
      | username                  | password         |
      | test.axv.2000@gmail.com   | KgkbAz7RHCoVD7RE |
      | test.axv.2000+1@gmail.com | W2kxy6tZf9oXzwC4 |