# Created by Anna at 11/7/24
Feature: Login Page Tests
  # Examples of login page tests
  # Valid Credentials Test

  Scenario: Login with correct credentials
    Given Open "dev" environment
    Then Wait 3 seconds
    Then Verify presents of element "//h5[text()='Login to Your Account']"
    Then Wait 3 seconds
    Then Type "test.axv.2000@gmail.com" into "//input[@name='username']"
    Then Wait 3 seconds
    Then Type "KgkbAz7RHCoVD7RE" into "//input[@name='password']"
    Then Wait 3 seconds
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//h3[text()=' Your device ']"