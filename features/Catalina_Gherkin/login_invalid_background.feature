# Created by catalinab at 11/6/24
Feature: Login Page Tests
  # Examples of login page tests

  Background:
    Given Open "dev" environment

  Scenario Outline: Login with incorrect user name
    Then Type "<username>" into "//input[@name='username']"
    Then Type "<password>" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presence of element "//p[text()='Invalid username or password']"

    Examples:
      | username                      | password       |
      | catk.tes@gmail.com            | strongpassword |
      | catk.test@gmail.co            | strongpassword |
      | catk.testgmail.com            | strongpassword |

  Scenario Outline: Login with incorrect password
    Then Type "catk.test@gmail.com" into "//input[@name='username']"
    Then Type "<password>" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presence of element "//p[text()='Invalid username or password']"

    Examples:
      | password       |
      | strong         |
      | password       |

# username: catk.test@gmail.com
# password: strongpassword
