Feature: Add a new jump in LogBook
  Background:
     Given OM Open "dev" environment
     Then OM Verify presents of element "//h5[text()='Login to Your Account']"

  Scenario: Add a New Jump
     Then OM Type "k38177348@gmail.com" into "//input[@name='username']"
     Then OM Type "k38ofe" into "//input[@name='password']"
     Then OM Click button "Login"
     And OM Wait 2 seconds
     Then OM Click menu "LogBook"
     And OM Wait 2 seconds
     Then OM Click button "Add new jump"
     And OM Wait 2 seconds
     Then I choose "New device" from the "dropdown"
     And OM Wait 2 seconds
     Then OM Click element "//span[contains(text(),'New device 333333333333337')]"
     Then OM Enter "2024-12-01" in "Date field"
     And OM Wait 2 seconds
     Then OM Click button "Finish"
     And OM Wait 2 seconds
     Then OM Verify the pop-up message "LogBook has been updated!" is displayed





