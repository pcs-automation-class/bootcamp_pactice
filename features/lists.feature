Feature: Lists
  # Enter feature description here

  Scenario: Open map for device
    Given Login as "test_1" in "dev" environment
    Then Click show on map button for "Device 3323"
    Then Wait 5 seconds