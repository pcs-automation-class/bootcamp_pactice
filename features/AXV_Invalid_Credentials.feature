Feature: Login Page Tests
  # Examples of login page tests
  # invalid Credentials Test

#Run Single Scenario
  Scenario: Login with correct credentials
    Given Open "dev" environment
    Then Wait 2 seconds
    Then Verify presents of element "//h5[text()='Login to Your Account']"
    Then Wait 1 seconds
    Then Type "test.axv.200@gmail.com" into "//input[@name='username']"
    Then Wait 1 seconds
    Then Type "KgkbAz7RHCoVD7RA" into "//input[@name='password']"
    Then Wait 1 seconds
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"

