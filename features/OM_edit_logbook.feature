Feature: Edit a logbook entry in LogBook
  Background:
     Given OM Open "dev" environment
     Then OM Verify presents of element "//h5[text()='Login to Your Account']"

  Scenario: Add a New Jump
     Then OM Type "k38177348@gmail.com" into "//input[@name='username']"
     Then OM Type "k38ofe" into "//input[@name='password']"
     Then OM Click button "Login"
     And OM Wait 2 seconds
     Then OM Click menu "Logbook"
     And OM Wait 2 seconds
     Then OM Click button "View"
     Then OM Verify presents of element "//h4[contains(text(), 'Jump info')]"
     And OM Wait 2 seconds
     Then OM Click element "//button[@class='action-btn-3dot__trigger']"
     And OM Wait 2 seconds
     Then OM Click button "Edit log"
     And OM Wait 2 seconds
     Then OM Enter "2024-11-30" in "Date field"
     And OM Wait 2 seconds
     Then OM Click button "Finish"
     Then OM Verify the pop-up message "LogBook has been updated!" is displayed
