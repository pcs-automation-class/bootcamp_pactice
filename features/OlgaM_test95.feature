Feature:  # Examples of test cases for login page

  Scenario: Login with incorrect email
#  AB-95-Test-login-page-with-incorrect-email

     Given Open "dev" environment
     Then Wait 2 seconds
     Then Verify presents of element "//h5[text()='Login to Your Account']"
     And Wait 2 seconds
     Then Type "christmas@gmail.com" into "//input[@name='username']"
     And Wait 2 seconds
     Then Type "k38ofe" into "//input[@name='password']"
     And Wait 2 seconds
     Then Click element "//button[text()=' Login ']"
     And Wait 2 seconds
     Then Verify presents of element "//p[text()='Invalid username or password']"

# Pseudo code
# incorrect username : christmas@gmail.com
# password: k38ofe