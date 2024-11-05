Feature: Login Page Tests
  # Examples of login page tests

  Scenario: Login with correct credentials
    Given Open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"
    Then Wait 1 seconds
    Then Verify presents of element "//h5[contains(text(), 'Login to Your Account')]"
    Then Wait 1 seconds
    Then Type "houseattheocean@gmail.com" into "//input[@type = 'text']"
    Then Wait 1 seconds
    Then Type "mCtwAtjpizSTWEz7" into "//input[@type = 'password']"
    Then Wait 1 seconds
    Then Click element "//button[@type = 'submit']"
    Then Verify presents of element "//h3[text()=' Your device ']"