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







#    //span[contains(text(),'New device 333333333333339')]
#     And OM Verify presents of element "//h3[text()=' Your device ']"
#     And OM Wait 2 seconds
#     Then OM Click element "//a[@href='#/device-settings']/i"
#     And OM Wait 2 seconds
#     And OM Click button "Add new device"
#     And OM Wait 3 seconds
#     Then OM Pop-up window "//span[contains(text(), 'Add new device')]" should appear
#     And OM Type "Test Device" into "//input[@class='el-input__inner']"
#     And OM Wait 2 seconds
#     Then I choose "333333333333337" from the "//div[@class='el-select__wrapper el-tooltip__trigger el-tooltip__trigger'][1]"
#     And OM Wait 2 seconds
#     Then OM Click button "+ Add new device"
#     And OM Wait 2 seconds
#     Then OM Verify the pop-up message "N++++++++++++++++++++++++++++++++++++++++++++++++ew device has been added" is displayed