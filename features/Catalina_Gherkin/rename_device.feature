# Created by catalinab at 11/16/24
Feature: Test devices
  # Enter feature description here

  Scenario Outline: Rename Device
    Given CK Login as "test_1" in "dev" environment
    Then CK Open window "Device Settings"
    Then Wait 2 seconds
    Then CK Click button "Edit"
    Then CK Rename "Name" to "<new_name>"
    Then Click button "Update"
    Then CK Verify pop-up message for "<new_name>"
    Then CK Verify updated device name presence "<new_name>"
    Then CK Verify device name is updated to "<new_name>"
    Examples:
      | new_name                             |
      | John                                 |
