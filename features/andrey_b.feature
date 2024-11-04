Feature: Login Page Tests
  # Examples of login page tests

  Scenario: Login with correct credentials
    Given Open "https://dev.linkmygear.com"
    Then Wait 3 seconds
    Then Click element "//div"
    Then Type "sgsrgsrg" into "//input"
    Then Create document