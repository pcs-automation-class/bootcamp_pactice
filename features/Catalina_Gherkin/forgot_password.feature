# Created by catalinab at 11/27/24
Feature: Forgot Password Functionality

  Background:
    Given CK Open "dev" environment

  Scenario Outline: Successfully restoring a password
    Then CK Open window "Forgot password?"
    Then CK Verify presence of element "Your email"
    When CK the user enters a valid "catk.test@gmail.com" into the "Your Email" field
    And CK Click button "Send"
    Then CK a confirmation message appears
    And CK the user receives a password reset email

  Examples:
    | email                  |
    | catk.test@gmail.com    |
