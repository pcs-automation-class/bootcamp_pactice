Feature: Test using POM

  Scenario: Login using POM
    Given Open "dev" environment
    Then Enter username for user "test_1"
    Then Enter password for user "test_1"
    Then Click login button
    Then Wait 3 seconds