Feature: Devices_Test Automation
  Background:
     Given OM Open "dev" environment
     Then OM Verify presents of element "//h5[text()='Login to Your Account']"

  Scenario: Delete Device by IMEI
     Then OM Type "k38177348@gmail.com" into "//input[@name='username']"
     Then OM Type "k38ofe" into "//input[@name='password']"
     Then OM Click button "Login"
     And OM Verify presents of element "//h3[text()=' Your device ']"
     And OM Wait 2 seconds
     Then OM Click element "//a[@href='#/device-settings']/i"
     And OM Wait 2 seconds
     Then OM Click button "Delete"
     And OM Wait 2 seconds
     Then OM Pop-up window "//h3[contains(text(), 'Delete device')]" should appear
     And OM Wait 2 seconds
     Then OM Click button "Delete_1"
     And OM Wait 2 seconds
     Then OM Verify the pop-up message "Device deleted" is displayed


