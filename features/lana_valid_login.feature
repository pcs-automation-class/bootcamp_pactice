Feature: Login Page Tests
  # Examples of login page tests

  Scenario: Scenario: Valid login

    Given Open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"
    Then Wait 1 seconds
    Then Verify presents of element "//h5[text()='Login to Your Account']"
    Then Type "kiwi2024+2@mailinator.com" into "//input[@name='username']"
#   Then Wait 1 seconds
    Then Type "kiwipass02" into "//input[@name='password']"
#    Then Wait 1 seconds
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//h3[text()=' Your device ']"

