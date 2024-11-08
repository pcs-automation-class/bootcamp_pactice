Feature: Login Page Tests
  # Examples of login page tests

  Scenario: Empty email login

     Then Open "dev" environment
     Then Wait 1 seconds
     Then Verify presents of element "//h5[text()='Login to Your Account']"
     Then Click element "//input[@name='username']"
     Then Wait 1 seconds
     Then Click element "//input[@name='password']"
     Then Verify presents of element "//div[text()='Email is required']"

  Scenario: Empty password login

    Then Open "dev" environment
    Then Wait 1 seconds
    Then Verify presents of element "//h5[text()='Login to Your Account']"
    Then Type "kiwi2024+2@mailinator.com" into "//input[@name='username']"
    Then Wait 1 seconds
    Then Click element "//input[@name='password']"
    Then Click element "//h5[text()='Login to Your Account']"
    Then Verify presents of element "//div[text()='Password is required']"

    Scenario: Empty both fields login

      Then Open "dev" environment
      Then Wait 1 seconds
      Then Verify presents of element "//h5[text()='Login to Your Account']"
      Then Click element "//input[@name='username']"
      Then Wait 1 seconds
      Then Click element "//input[@name='password']"
      Then Verify presents of element "//div[text()='Email is required']"
      Then Click element "//input[@name='username']"
      Then Verify presents of element "//div[text()='Password is required']"


