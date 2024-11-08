# Created by lana-n at 11/6/24
Feature: Login Page Tests
  # Examples of login page tests
  Background:
    Given Open "dev" environment
    Then Verify presents of element "//h5[text()='Login to Your Account']"

  Scenario: Scenario: Valid login
    Then Type "kiwi2024+2@mailinator.com" into "//input[@name='username']"
    Then Type "kiwipass02" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//h3[text()=' Your device ']"

  Scenario: Scenario: Invalid email
    Then Type "kiwi2+2@mailinator.com" into "//input[@name='username']"
    Then Type "kiwipass02" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"

  Scenario: Scenario: Invalid password
    Then Type "kiwi2024+2@mailinator.com" into "//input[@name='username']"
    Then Type "kiwipass02020202" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"

  Scenario: Scenario: Invalid email and invalid password
    Then Type "kiwi2024+20000000@mailinator.com" into "//input[@name='username']"
    Then Type "kiwipass02020202" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "//p[text()='Invalid username or password']"