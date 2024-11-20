Feature: Login Page Tests with table
#  Background:
#    When Use chrome browser

  Scenario: Login with correct credentials
    Given Open "dev" environment
    Then AB Input following credentials
      | key      | value                         |
      | username | pcs.automationclass@gmail.com |
      | password | 1234567                       |
    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
    Then Type "1234567" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
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
      | password | 12345678                      |
#    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
#    Then Type "1234567" into "//input[@name='password']"
#    Then Click element "//button[text()=' Login ']"
    Then Click button "Login"
#    Then Go to menu logbook
#    Then Click button "Subscribe"
#    Then Go to menu devices


  Scenario: Rename device
    Given Login as "test_1" in "dev" environment
    Then Open window Device Settings
#    Then Click element "//tr[./td/div[text()='333333333333324']]//button[text()=' Edit ']"
#    Then Click element "//input[@class='el-input__inner']"
#    Then Clear input field "//input[@class='el-input__inner']"
#    Then Click button "Update"
#    Then Wait 3 seconds

  Scenario: Verify battery in heartbeat message
    Given Create new heartbeat message for device with following data
      | key       | value           |
      | imei      | 333333333333324 |
      | date      | 20241114        |
      | latitude  | 37.770198       |
      | longitude | -121.641856     |
      | battery   | 43              |
      | state     | on              |
    Then Login as "test_1" in "dev" environment
    Then Wait 2 seconds
    Then Verify presents of element "//div[./h4[text()='Device 1']]//span[contains(text(), '34')]"
#    Then ldkhgkdlshglkshglkshg
    Then Verify battery prercentage "10%" for device "Device 1"