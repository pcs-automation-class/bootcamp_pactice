# Before running this test case, delete one device from your account
Feature: Devices_Test Automation
  Background:
     Given OM Open "dev" environment
     Then OM Verify presents of element "//h5[text()='Login to Your Account']"

  Scenario: Add a New Device
     Then OM Type "k38177348@gmail.com" into "//input[@name='username']"
     Then OM Type "k38ofe" into "//input[@name='password']"
     Then OM Click button "Login"
     And OM Verify presents of element "//h3[text()=' Your device ']"
     And OM Wait 2 seconds
     Then OM Click element "//a[@href='#/device-settings']/i"
     And OM Wait 2 seconds
     And OM Click button "Add new device"
     And OM Wait 3 seconds
     Then OM Pop-up window "//span[contains(text(), 'Add new device')]" should appear
     And OM Type "Test Device" into "//input[@class='el-input__inner']"
     And OM Wait 2 seconds
     Then I choose "333333333333337" from the "//div[@class='el-select__wrapper el-tooltip__trigger el-tooltip__trigger'][1]"
     And OM Wait 2 seconds
     Then OM Click button "+ Add new device"
     And OM Wait 2 seconds
#     Then OM Verify the pop-up message "New device has been added" is displayed
