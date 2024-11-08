Feature: Login page tests

 Background:
 Given Open "dev" environment

  Scenario: Login with correct credentials
     Then Verify presents of element "//h5[text()='Login to Your Account']"
     And Wait 2 seconds
     Then Type "k38177348@gmail.com" into "//input[@name='username']"
     And Wait 2 seconds
     Then Type "k38ofe" into "//input[@name='password']"
     And Wait 2 seconds
     Then Click element "//button[text()=' Login ']"
     And Wait 2 seconds
     Then Verify presents of element "//h3[text()=' Your device ']"

    Scenario Outline: Login with invalid username (email)
     Then Type "<username>" into "//input[@name='username']"
     Then Type "<password>" into "//input[@name='password']"
     Then Click element "//button[text()=' Login ']"
#    And Wait 2 seconds
     Then Verify presents of element "//p[text()='Invalid username or password']"

    Examples:
     | username               | password |
     | christmas0@gmail.com   | k38ofe   |
     | christmas1@gmail.com   | k38ofe   |
     | christmas2@gmail.com   | k38ofe   |


  Scenario Outline: Login with invalid password
     Then Type "<username>" into "//input[@name='username']"
     Then Type "<password>" into "//input[@name='password']"
     Then Click element "//button[text()=' Login ']"
#    And Wait 2 seconds
     Then Verify presents of element "//p[text()='Invalid username or password']"


    Examples:
     | username              | password |
     | k38177348@gmail.com   | k10ofe   |
     | k38177348@gmail.com   | k20ofe   |
     | k38177348@gmail.com   | k50ofe   |

# Pseudo code
# username: k38177348@gmail.com
# password: k38ofe
