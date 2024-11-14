Feature: Devices Page Tests
  # Examples of login page tests

  Scenario: Homepage Header - click Devices menu item

    Then Open "dev" environment
    Then Wait 1 seconds
    Then Verify presents of element "//h5[text()='Login to Your Account']"
    Then Type "kiwi2024+2@mailinator.com" into "//input[@name='username']"
    Then Wait 1 seconds
    Then Type "kiwipass02" into "//input[@name='password']"
    Then Wait 1 seconds
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//h3[text()=' Your device ']"
    Then click element "//a[text()='Devices']"
    Then Wait 2 seconds