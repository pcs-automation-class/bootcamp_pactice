# Created by lana-n at 11/6/24
# Created by lana-n at 11/6/24
Feature: Login Page Tests
  # Examples of login page tests
  Background:
    Given Open "dev" environment
    Then Verify presents of element "//h5[text()='Login to Your Account']"

  Scenario Outline: Scenario: Valid login
    Then Type "<username>" into "//input[@name='username']"
    Then Type "<password>" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//h3[text()=' Your device ']"
    Examples:
      | username                  | password   |
      | kiwi2024@mailinator.com   | kiwipass01 |
      | kiwi2024+2@mailinator.com | kiwipass02 |
      | kiwi2024+3@mailinator.com | kiwipass03 |

  Scenario Outline: Scenario: Invalid email
    Then Type "<username>" into "//input[@name='username']"
    Then Type "<password>" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"
    Examples:
      | username                  | password   |
      | kiwi2024AAA@mailinator.com   | kiwipass01 |
      | kiwi2024BBB+2@mailinator.com | kiwipass02 |
      | kiwi2024CCC+3@mailinator.com | kiwipass03 |

   Scenario Outline: Scenario: Invalid password
    Then Type "<username>" into "//input[@name='username']"
    Then Type "<password>" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"
     Examples:
      | username                  | password   |
      | kiwi2024@mailinator.com   | kiwipass01AAA |
      | kiwi2024+2@mailinator.com | kiwipass02BBB |
      | kiwi2024+3@mailinator.com | kiwipass03CCC |

  Scenario Outline: Scenario: Invalid email and invalid password
    Then Type "<username>" into "//input[@name='username']"
    Then Type "<password>" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"
    Examples:
      | username                  | password   |
      | kiwi2024A@mailinator.com   | kiwipass01A |
      | kiwi2024AB+2@mailinator.com | kiwipass02A |
      | kiwi2024C+3@mailinator.com | kiwipass03A |




