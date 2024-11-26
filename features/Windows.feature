Feature: Switch windows

# context.driver.window_handles                                       all windows id in list
# context.driver.current_window_handle                                current window id
# context.driver.switch_to.window(context.driver.window_handles[0])   switch to window by index
# context.driver.close()                                              to close current window

  Scenario: Customer portal
    Given Login as "test_1" in "dev" environment
    Then Click button "Settings"
    Then Click button "Billing"
    Then Click button "Customer Portal"
    Then Wait 10 seconds

# TODO Finish test when will have some element on new page

  Scenario: Some new scenario
    Given Login as "test_1" in "dev" environment
    Then Click button "Customer Portal"
    Then Wait 10 seconds
    Then New step


  Scenario: New scenario
    Given Login as "test_1" in "dev" environment
    Then Click button "Settings"
    Then Click button "Billing"
    Then New step