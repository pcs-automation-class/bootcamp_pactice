Feature: Devices List Tests
  # Examples of login page tests

  Scenario: Devices List - rename device successfully

    Then Open "dev" environment
    Then Wait 1 seconds
    Then Verify presents of element "//h5[text()='Login to Your Account']"
    Then Type "kiwi2024+2@mailinator.com" into "//input[@name='username']"
    Then Wait 1 seconds
    Then Type "kiwipass02" into "//input[@name='password']"
    Then Wait 1 seconds
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//h3[text()=' Your device ']"
    Then click element "//a[contains(@href, 'device-settings')]"
    Then Wait 2 seconds
    Then click element "//button[contains(@class, 'lmg-btn')]"
    Then Wait 2 seconds
    Then click element "//div[contains(@class, 'label-top')]"
    Then Wait 2 seconds
    Then Type "kiwis device1 here" into "//input[contains(@class, 'el-input__inner')]"
    Then Wait 2 seconds
    Then Click element "//span[text()='Update']"
    Then Wait 2 seconds