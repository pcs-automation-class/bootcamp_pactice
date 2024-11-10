# Created by Anna at 11/9/24
Feature: Login Page Tests
  # Examples of login page tests

  Background:
    Given Open "dev" environment

  Scenario Outline: Login with empty user name and or password
    Then Type "<username>" into "//input[@name='username']"
    Then Type "<password>" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//div[text()='Email is required']"
    Then Verify presents of element "//div[text()='Password is required']"
    Examples:
      | username      | password |
      | Skip          | Skip     |