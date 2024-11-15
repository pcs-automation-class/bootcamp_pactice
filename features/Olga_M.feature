Feature: Login page tests

  Background:
     Given Open "dev" environment
#     Then Verify presents of element "//h5[text()='Login to Your Account']"

    @regression
  Scenario: Login with correct credentials
     Then OM Type "k38177348@gmail.com" into "//input[@name='username']"
     Then OM Type "k38ofe" into "//input[@name='password']"
     Then OM Click element "//button[text()=' Login ']"
     Then Verify presents of element "//h3[text()=' Your device ']"

  Scenario Outline: Login with invalid username (email)
     Then OM Type "<username>" into "//input[@name='username']"
     Then OM Type "<password>" into "//input[@name='password']"
     Then OM Click element "//button[text()=' Login ']"
     And OM Wait 2 seconds
     Then Verify presents of element "//p[text()='Invalid username or password']"

    Examples:
     | username               | password |
     | christmas0@gmail.com   | k38ofe   |
     | christmas1@gmail.com   | k38ofe   |
     | christmas2@gmail.com   | k38ofe   |


  Scenario Outline: Login with invalid password
     Then OM Type "<username>" into "//input[@name='username']"
     Then OM Type "<password>" into "//input[@name='password']"
     Then OM Click element "//button[text()=' Login ']"
     And OM Wait 2 seconds
     Then Verify presents of element "//p[text()='Invalid username or password']"

    Examples:
     | username              | password |
     | k38177348@gmail.com   | k10ofe   |
     | k38177348@gmail.com   | k20ofe   |
     | k38177348@gmail.com   | k50ofe   |

  Scenario Outline: Login to the page with empty username and/or password
    Then OM Type "<username>" into "//input[@name='username']"
    Then OM Type "<password>" into "//input[@name='password']"
    Then OM Click element "//button[@type = 'submit']"
    Then Verify presents of element "<xpath_username>"
    Then Verify presents of element "<xpath_password>"
    Examples:
      |    username         |  password |        xpath_username              |           xpath_password             |
      | k38177348@gmail.com |  Skip     | Skip                               | //div[text()='Password is required'] |
      | Skip                |  k38ofe   | //div[text()='Email is required']  | Skip                                 |
      | Skip                |  Skip     | //div[text()='Email is required']  | //div[text()='Password is required'] |

