Feature: Login Page Tests
  # Examples of login page tests
  Background:
    Given Open "dev" environment
#    Then Verify presents of element "//h5[text()='Login to Your Account']"

  @smoke
  Scenario: Login with correct credentials
    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
    Then AB Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
    Then Type "1234567" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//h3[text()=' Your device ']"


  Scenario Outline: Login with incorrect user name
    Then Type "<username>" into "//input[@name='username']"
    Then Type "<password>" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"
    Examples:
      | username       | password         |
      | pcs@gmail.com  | hr9rsHU6TnWDYnpy |
      | None           | 1234567          |
      | pcs2@gmail.com | hr9rsHU6TnWDYnpy |

  Scenario Outline: Login with empty user name and or password
    Then Type "<username>" into "//input[@name='username']"
    Then Type "<password>" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "<xpath_username>"
    Then Verify presents of element "<xpath_password>"
    Examples:
      | username      | password | xpath_username                    | xpath_password                       |
      | pcs@gmail.com | Skip     | Skip                              | //div[text()='Password is required'] |
      | Skip          | 1234567  | //div[text()='Email is required'] | Skip                                 |
      | Skip          | Skip     | //div[text()='Email is required'] | //div[text()='Password is required'] |


  Scenario: Login with incorrect password
    Then Type "pcs.automationclass+1@gmail.com" into "//input[@name='username']"
    Then Type "2" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"
