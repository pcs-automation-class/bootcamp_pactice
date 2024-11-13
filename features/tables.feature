Feature: Login Page Tests with table
  # Examples of login page tests

#  Scenario: Login with correct credentials2
#    Given Open "dev" environment
#    Then AB Input following credentials
#      | key      | value                         |
#      | username | pcs.automationclass@gmail.com |
#      | password | 1234567 |
#    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
#    Then Type "1234567" into "//input[@name='password']"
#    Then Click element "//button[text()=' Login ']"
#    Then Click button "Subscribe"
#    Then Verify presents of element "//h3[text()=' Your device ']"

  Scenario: Login with correct credentials2
    Given Open "dev" environment
    Then AB Input following credentials
      | key      | value                         |
      | username | pcs.automationclass@gmail.com |
      | password | 1234567                       |
#    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
#    Then Type "1234567" into "//input[@name='password']"
#    Then Click element "//button[text()=' Login ']"
    Then Click button "Login"
#    Then Go to menu logbook
#    Then Click button "Subscribe"
#    Then Go to menu devices

  # Scenario: = Test Case Name
  Scenario: Login with correct credentials2
    Given Open "dev" environment
    Then AB Input following credentials
      | key      | value                         |
      | username | pcs.automationclass@gmail.com |
      | password | 12345678                       |
#    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
#    Then Type "1234567" into "//input[@name='password']"
#    Then Click element "//button[text()=' Login ']"
    Then Click button "Login"
#    Then Go to menu logbook
#    Then Click button "Subscribe"
#    Then Go to menu devices

