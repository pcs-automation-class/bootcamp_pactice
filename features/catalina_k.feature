# Created by catalinak at 11/5/24
Feature: Login Page Tests
  # Examples of login page tests

  Scenario: Login with correct credentials
    Given Open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"
#    Then Wait 1 seconds
    Then Verify presents of element "//h5[text()='Login to Your Account']"
#    Then Wait 1 seconds
    Then Type "catk.test@gmail.com" into "//input[@name='username']"
#    Then Wait 1 seconds
    Then Type "hr9rsHU6TnWDYnpy" into "//input[@name='password']"
#    Then Wait 1 seconds
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//h3[text()=' Your device ']"


  Scenario: Login with incorrect credentials
    Given Open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"
#    Then Wait 1 seconds
    Then Verify presents of element "//h5[text()='Login to Your Account']"
#    Then Wait 1 seconds
    Then Type "catk.test@gmail.com" into "//input[@name='username']"
#    Then Wait 1 seconds
    Then Type "hr9rsHU6TnWDYnpy" into "//input[@name='password']"
#    Then Wait 1 seconds
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"

  Scenario: Log Out

  Scenario: Forgot Password
    Given Open ""

  Scenario: Create New Account

  Scenario: Click on 'Terms and Conditions'

  Scenario: Update Profile



# username: catk.test@gmail.com
# password:

#   Add credentials to the URL
#   full_url = f"https://{username}:{password}@{url}"