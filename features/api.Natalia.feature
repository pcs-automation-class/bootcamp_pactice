Feature: Test API
  # Not tests. Scenarios send messages to emulate device behaviour

  Scenario: EMULATE Add device message
    Given Create new record for device with following data
      | key       | value                |
      | imei      | 333333333333335      |
      | date      | 20241117             |
      | jump      | 3                    |
      | latitude  | 41.9216270344041     |
      | longitude | -87.64674914989571   |


  Scenario: EMULATE Device heartbeat message
    Given Create new heartbeat message for device with following data
      | key       | value           |
      | imei      | 333333333333335 |
      | date      | 20241118        |
      | latitude  | 37.770198       |
      | longitude | -121.641856     |
      | battery   | 34               |
#      states: idle, on, off
      | state     | off            |

#  Then Login as "test_1" in "dev" environment
#  Then Verify presents of element "//div[./h4[text()='Device 1']]//span[contains(text(), '34')]"