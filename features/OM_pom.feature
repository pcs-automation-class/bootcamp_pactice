Feature: Test using POM

  Scenario: OM_Loging using POM
   Given Open "dev" environment
    Then OM Enter username "user_1"
    Then OM Enter password "user_1"
    Then OM Click login button
    And OM Wait 2 seconds
#    Then OM Click element "forgot_password"



