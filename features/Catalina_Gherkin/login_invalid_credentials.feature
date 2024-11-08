# Created by catalinab at 11/5/24

Feature: Login Page Tests
  # Examples of login page tests
Scenario: Login with incorrect credentials
    Given Open "dev" environment
#    Then Wait 1 seconds
    Then Verify presents of element "//h5[text()='Login to Your Account']"
#    Then Wait 1 seconds
    Then Type "catk.test@gmail.com" into "//input[@name='username']"
#    Then Wait 1 seconds
    Then Type "hr9r" into "//input[@name='password']"
#    Then Wait 1 seconds
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"