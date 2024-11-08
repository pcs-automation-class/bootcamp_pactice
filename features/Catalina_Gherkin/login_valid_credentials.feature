# Created by catalinak at 11/5/24
Feature: Login Page Tests
  # Examples of login page tests

  Scenario: Login with correct credentials
    Given CK Open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"
#    Then Wait 1 seconds
    Then Verify presents of element "//h5[text()='Login to Your Account']"
#    Then Wait 1 seconds
    Then Type "catk.test@gmail.com" into "//input[@name='username']"
#    Then Wait 1 seconds
    Then Type "strongpassword" into "//input[@name='password']"
#    Then Wait 1 seconds
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//h3[text()=' Your device ']"

# username: catk.test@gmail.com
# password: strongpassword

#   Add credentials to the URL
#   full_url = f"https://{username}:{password}@{url}"