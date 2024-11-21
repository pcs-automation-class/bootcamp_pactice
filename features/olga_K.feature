Feature: Login Page Tests
  Background:
    Given OK Open "dev" environment
    Then OK Wait 2 seconds
  # Examples of  login page tests

  Scenario: Login with correct credentials
    Then OK Verify presents of element "//h5[contains(text(), 'Login to Your Account')]"
    Then OK Wait 1 seconds
    Then OK Type "houseattheocean@gmail.com" into "//input[@type = 'text']"
    Then OK Wait 1 seconds
    Then OK Type "mCtwAtjpizSTWEz7" into "//input[@type = 'password']"
    Then OK Wait 1 seconds
    Then OK Click button "Login"
    Then OK Verify presents of element "//h3[text()=' Your device ']"

  Scenario: Forgot password feature
    Then OK Verify presents of element "//h5[contains(text(), 'Login to Your Account')]"
    Then OK Wait 1 seconds
    Then OK Click element "//a[text() = 'Forgot password?']"
    Then OK Verify presents of element "//h5[contains(text(), 'Restore Password')]"
    Then OK Type "houseattheocean@gmail.com" into "//input[@class = 'el-input__inner']"
    Then OK Click button "Send"
    Then OK Verify presents of element "//h5[text()='Please check your inbox. You will receive an email with instruction in case if such email exists in our DB ']"

  Scenario Outline: Login with empty credentials
    Then OK Type "<username>" into "//input[@type = 'text']"
    Then OK Type "<password>" into "//input[@type = 'password']"
    Then OK Click button "Login"
    Then OK Verify presents of element "<xpath_username>"
    Then OK Verify presents of element "<xpath_password>"
    Examples:
      | username                  | password          | xpath_username                    | xpath_password                       |
      | houseattheocean@gmail.com | Skip              | Skip                              | //div[text()='Password is required'] |
      | Skip                      | mCtwAtjpizSTWEz7  | //div[text()='Email is required'] | Skip                                 |
      | Skip                      | Skip              | //div[text()='Email is required'] | //div[text()='Password is required'] |

  Scenario Outline: Login with incorrect credentials
    Then OK Type "<username>" into "//input[@type = 'text']"
    Then OK Type "<password>" into "//input[@type = 'password']"
    Then OK Click button "Login"
    Then OK Verify presents of element "//p[text()='Invalid username or password']"
    Examples:
      | username                   | password         |
      | houseattheocean@gmail.com  | 123321           |
      | None                       | 1234567          |
      | pcs2@gmail.com             | hr9rsHU6TnWDYnpy |

  Scenario: Rename device
    Then OK Verify presents of element "//h5[contains(text(), 'Login to Your Account')]"
    Then OK Wait 1 seconds
    Then OK Type "houseattheocean@gmail.com" into "//input[@type = 'text']"
    Then OK Wait 1 seconds
    Then OK Type "mCtwAtjpizSTWEz7" into "//input[@type = 'password']"
    Then OK Wait 1 seconds
    Then OK Click button "Login"
    Then OK Wait 1 seconds
    Then OK Verify presents of element "//h3[text()=' Your device ']"
    Then OK Wait 2 seconds
    Then OK Click button "Device settings"
    Then OK Wait 2 seconds
    Then OK Click button "Device1"
    Then OK Wait 2 seconds
    Then OK Clear the field "//input[@class='el-input__inner']"
    Then OK Wait 1 seconds
    Then OK Type "New device2" into "//input[@class='el-input__inner']"
    Then OK Wait 1 seconds
    Then OK Click button "Update"

