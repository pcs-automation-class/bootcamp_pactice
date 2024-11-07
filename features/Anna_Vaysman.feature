Feature: Login Page Tests
  # Examples of login page tests

  Scenario: Login with correct credentials
    Given Open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"
    Then Wait 3 seconds
    Then Verify presents of element "//h5[text()='Login to Your Account']"
    Then Wait 3 seconds
    Then Type "test.axv.2000@gmail.com" into "//*[@id="app"]/layout-loginlayout/section/div/div/div[2]/div/form/div[1]/div/input"
    Then Wait 3 seconds
    Then Type "KgkbAz7RHCoVD7RE" into "//*[@id="app"]/layout-loginlayout/section/div/div/div[2]/div/form/div[2]/input"
    Then Wait 3 seconds
    Then Click element "//*[@id="app"]/layout-loginlayout/section/div/div/div[2]/div/form/div[3]/button"
    Then Verify presents of element "//h3[text()=' Your device ']"