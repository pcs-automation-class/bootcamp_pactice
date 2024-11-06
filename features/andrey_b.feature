Feature: Login Page Tests
  # Examples of login page tests

  Scenario: Login with correct credentials
    Given Open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"
    Then Wait 1 seconds
    Then Verify presents of element "//h5[text()='Login to Your Account']"
#    Then Wait 1 seconds
    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
#    Then Wait 1 seconds
    Then Type "1234567" into "//input[@name='password']"
#    Then Wait 1 seconds
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//h3[text()=' Your device ']"


  Scenario: Login with incorrect credentials
    Given Open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"
#    Then Wait 1 seconds
    Then Verify presents of element "//h5[text()='Login to Your Account']"
#    Then Wait 1 seconds
    Then Type "pcs@gmail.com" into "//input[@name='username']"
#    Then Wait 1 seconds
    Then Type "hr9rsHU6TnWDYnpy" into "//input[@name='password']"
#    Then Wait 1 seconds
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"


# username: pcs.automationclass+1@gmail.com
# password: jnTVrm3cpLJfdsMk

#   Add credentials to the URL
#   full_url = f"https://{username}:{password}@{url}"
