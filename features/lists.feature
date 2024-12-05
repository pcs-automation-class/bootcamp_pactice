Feature: Lists
  # Enter feature description here

  Scenario: Open map for device
    Given Login as "test_1" in "dev" environment
#    Then Click show on map button for "Device 3323"
#    Then Click show device "Device 3323" on map
    Then Open news with text "Jasmine Supports"
    Then Wait 5 seconds