Feature: Linkmygear.com Login Page Tests
  # Examples of login page tests

  @smoke @regression
  Scenario: Login with valid credentials
    Given Open "https://dev.linkmygear.com"
    Then Wait 5 seconds
#    Then