Feature:  # Examples of test cases for login page
Scenario: Login with incorrect email
#  AB-96-Test-login-page-with-incorrect-password
     Given Open "dev" environment
     Then Wait 2 seconds
     Then Verify presents of element "//h5[text()='Login to Your Account']"
     And Wait 2 seconds
     Then Type "k38177348@gmail.com" into "//input[@name='username']"
     And Wait 2 seconds
     Then Type "abc8ofe" into "//input[@name='password']"
     And Wait 2 seconds
     Then Click element "//button[text()=' Login ']"
     And Wait 2 seconds
     Then Verify presents of element "//p[text()='Invalid username or password']"

# Pseudo code
# correct username : k38177348@gmail.com
# incorrect password: abc8ofe


