Feature: Test Sections
  Background:
     Given OM Open "dev" environment
    Then OM Verify presents of element "//h5[text()='Login to Your Account']"

  Scenario: Verify that the Active Jumps section is present
     Then OM Type "k38177348@gmail.com" into "//input[@name='username']"
     Then OM Type "k38ofe" into "//input[@name='password']"
     Then OM Click button "Login"
     And OM Verify presents of element "//h3[text()=' Your device ']"
     Then OM Click menu "Active Jumps"
     Then OM Verify presents of element "//a[text()='Active Jumps']"
