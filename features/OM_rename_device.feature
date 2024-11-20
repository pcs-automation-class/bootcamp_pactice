  Feature: Test Sections
  Background:
     Given OM Open "dev" environment
     Then OM Verify presents of element "//h5[text()='Login to Your Account']"

  Scenario: Rename a device in Device page
     Then OM Type "k38177348@gmail.com" into "//input[@name='username']"
     Then OM Type "k38ofe" into "//input[@name='password']"
     Then OM Click button "Login"
     And OM Verify presents of element "//h3[text()=' Your device ']"
     And OM Wait 2 seconds
     Then OM Click element "//a[@href='#/device-settings']/i"
     And OM Wait 2 seconds
     Then OM Click button "Edit"
     And OM Wait 2 seconds
     Then OM Clear input field "//input[@class='el-input__inner']"
     And OM Wait 2 seconds
     And OM Type "Test Device" into "//input[@class='el-input__inner']"
     And OM Wait 2 seconds
     Then OM Click button "Update"
