Feature: Test API
  # Not tests. Scenarios send messages to emulate device behaviour

  Scenario: EMULATE Add device message
    Given Create new record for device with following data
      | key       | value                |
      | imei      | 333333333333309      |
      | date      | 20241120             |
      | jump      | 2                    |
      | latitude  | 46.8666666666678     |
      | longitude | -113.84567834566889  |


  Scenario: EMULATE Device heartbeat message
    Given Create new heartbeat message for device with following data
      | key       | value           |
      | imei      | 333333333333309 |
      | date      | 20241120        |
      | latitude  | 37.770198       |
      | longitude | -121.641856     |
      | battery   | 10              |
#      states: idle, on, off
      | state     | off             |

    
