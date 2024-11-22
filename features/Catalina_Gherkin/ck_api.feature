Feature: Test API
  # Not tests. Scenarios send messages to emulate device behaviour

  Scenario: EMULATE Add device message
    Given Create new record for device with following data
      | key       | value           |
      | imei      | 333333333333352 |
      | date      | 20241116        |
      | jump      | 1               |
      | latitude  | -19.4           |
      | longitude | 133.5243937     |


  Scenario: EMULATE Device heartbeat message
    Given Create new heartbeat message for device with following data
      | key       | value           |
      | imei      | 333333333333324 |
      | date      | 20241114        |
      | latitude  | 37.770198       |
      | longitude | -121.641856     |
      | battery   | 100             |
#      states: idle, on, off
      | state     | off             |