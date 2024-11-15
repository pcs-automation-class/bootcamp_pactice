# Created by nati- at 11/2/2024
Feature: Login Page Tests
  # Examples of login page tests
  Background:
    Given Open "dev" environment
    Then Verify presents of element "//h5[text()='Login to Your Account']"

  Scenario: Login with correct credentials
    Then Type "sambosr@gmailbrt.com" into "//input[@name='username']"
    Then Wait 1 seconds
    Then Type "awvgFjTtM5GVgr3m" into "//input[@name='password']"
    Then Wait 1 seconds
    Then Click element "//button[text()=' Login ']"
    Then Wait 1 seconds
    Then Verify presents of element "//h3[text()=' Your device ']"

 Scenario: Forgot password feature testing
    Then NZ Verify presents of element "//h5[contains(text(), 'Login to Your Account')]"
    Then NZ Wait 1 seconds
    Then NZ Click element "//a[contains(text() = 'Forgot password?')]"
    Then NZ Verify presents of element "//h5[contains(text(), 'Restore Password')]"
    Then NZ Wait 1 seconds
    Then NZ Type "sambosr@gmailbrt.com" into "//input[@class = 'el-input__inner']"
    Then NZ Click element "//button[text() = ' Send ']"
    Then NZ Verify presents of element "//h5[text()='Please check your inbox. You will receive an email with instruction in case if such email exists in our DB ']"

  Scenario Outline: Login with incorrect user name
    Then Type "<username>" into "//input[@name='username']"
    Then Type "<password>" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"
    Examples:
      | username                      | password         |
      | sambosr+1@gmailbrt.com        | awvgFjTtM5GVgr3m |
      | pcs.automationclass@gmail.com | 1234567          |
      | sambosr@gmailbrt.com          | awvgFjTtM5GVgr3m |


  Scenario: Login with incorrect password
    Then Type "sambosr@gmailbrt.com" into "//input[@name='username']"
    Then Wait 1 seconds
    Then Type "2" into "//input[@name='password']"
    Then Wait 1 seconds
    Then Click element "//button[text()=' Login ']"
    Then Wait 1 seconds
    Then Verify presents of element "//p[text()='Invalid username or password']"


