Feature: Login page tests
  # Examples of test cases for login page
   # Branch AB-74-Test-login-page-with-valid-credentials

  Scenario: Login with correct credentials
     Given Open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"
     Then Wait 2 seconds
     Then Verify presents of element "//h5[text()='Login to Your Account']"
     And Wait 2 seconds
     Then Type "k38177348@gmail.com" into "//input[@name='username']"
     And Wait 2 seconds
     Then Type "k38ofe" into "//input[@name='password']"
     And Wait 2 seconds
     Then Click element "//button[text()=' Login ']"
     And Wait 2 seconds
     Then Verify presents of element "//h3[text()=' Your device ']"

# Pseudo code
# username: k38177348@gmail.com
# password: k38ofe
