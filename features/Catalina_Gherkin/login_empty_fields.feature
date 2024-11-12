# Created by catalinab at 11/6/24
Feature: Login Page Tests
  # Examples of login page tests

  Background:
    Given CK Open "dev" environment

  Scenario Outline: Login with empty fields
    Then CK Type "<username>" into "//input[@name='username']"
    Then CK Type "<password>" into "//input[@name='password']"
    Then CK Click element "//button[text()=' Login ']"
    Then CK Verify presence of element "//p[text()='Invalid username or password']"

    Examples:
      | username | password       |
      | none     | strongpassword |
      | catk.test@gmail.com | none |
      | none     | none           |


