# Created by catalinab at 11/6/24
Feature: Login Page Tests
  # Examples of login page tests
  Background:
    Given CK Open "dev" environment
#    Then Verify presents of element "//h5[text()='Login to Your Account']"

  Scenario: Login with correct credentials
    Then CK Type "catk.test@gmail.com" into "//input[@name='username']"
    Then CK Type "strongpassword" into "//input[@name='password']"
    Then CK Click button "Login"
    Then CK Verify presence of element "//h3[text()=' Your device ']"


  Scenario Outline: Login with incorrect user name
    Then CK Type "<username>" into "//input[@name='username']"
    Then CK Type "<password>" into "//input[@name='password']"
    Then CK Click button "Login"

    Examples:
      | username                      | password         |
      | catk.test@gmail.com           | strongpassword   |

