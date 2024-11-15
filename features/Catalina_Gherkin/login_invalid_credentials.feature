# Created by catalinab at 11/5/24

Feature: Login Page Tests
  # Examples of login page tests
    @smoke
Scenario: Login with incorrect credentials
    Given CK Open "dev" environment
#    Then Wait 1 seconds
    Then CK Verify presence of element "//h5[text()='Login to Your Account']"
#    Then Wait 1 seconds
    Then CK Type "catk.test@gmail.com" into "//input[@name='username']"
#    Then Wait 1 seconds
    Then CK Type "hr9r" into "//input[@name='password']"
#    Then Wait 1 seconds
    Then CK Click button "Login"
    Then CK Verify presence of element "//p[text()='Invalid username or password']"