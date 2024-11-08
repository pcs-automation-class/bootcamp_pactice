Feature: Login Page Tests with table
  # Examples of login page tests

  Scenario: Login with correct credentials
    Given Open "dev" environment
    Then AB Input following credentials
      | key      | value                         |
      | username | pcs.automationclass@gmail.com |
#    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
#    Then Type "1234567" into "//input[@name='password']"
#    Then Click element "//button[text()=' Login ']"
#    Then Verify presents of element "//h3[text()=' Your device ']"