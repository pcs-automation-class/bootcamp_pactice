Feature: Login Page Tests
  Background:
    Given Open "dev" environment
    Then Wait 2 seconds
  # Examples of login page tests

  Scenario: Login with correct credentials
    Then Verify presents of element "//h5[contains(text(), 'Login to Your Account')]"
    Then Wait 1 seconds
    Then Type "houseattheocean@gmail.com" into "//input[@type = 'text']"
    Then Wait 1 seconds
    Then Type "mCtwAtjpizSTWEz7" into "//input[@type = 'password']"
    Then Wait 1 seconds
    Then Click element "//button[@type = 'submit']"
    Then Verify presents of element "//h3[text()=' Your device ']"

  Scenario: Forgot password feature
    Then Verify presents of element "//h5[contains(text(), 'Login to Your Account')]"
    Then Wait 1 seconds
    Then Click element "//a[text() = 'Forgot password?']"
    Then Verify presents of element "//h5[contains(text(), 'Restore Password')]"
    Then Type "houseattheocean@gmail.com" into "//input[@class = 'el-input__inner']"
    Then Click element "//button[text() = ' Send ']"
    Then Verify presents of element "//h5[text()='Please check your inbox. You will receive an email with instruction in case if such email exists in our DB ']"

  Scenario Outline: Login with empty credentials
    Then Type "<username>" into "//input[@type = 'text']"
    Then Type "<password>" into "//input[@type = 'password']"
    Then Click element "//button[@type = 'submit']"
    Then Verify presents of element "<xpath_username>"
    Then Verify presents of element "<xpath_password>"
    Examples:
      | username                  | password          | xpath_username                    | xpath_password                       |
      | houseattheocean@gmail.com | Skip              | Skip                              | //div[text()='Password is required'] |
      | Skip                      | mCtwAtjpizSTWEz7  | //div[text()='Email is required'] | Skip                                 |
      | Skip                      | Skip              | //div[text()='Email is required'] | //div[text()='Password is required'] |

  Scenario Outline: Login with empty user name and or password
    Then Type "<username>" into "//input[@name='username']"
    Then Type "<password>" into "//input[@name='password']"
    Then Click element "//button[text()=' Login ']"
    Then Verify presents of element "<xpath_username>"
    Then Verify presents of element "<xpath_password>"
    Examples:
      | username      | password | xpath_username                    | xpath_password                       |
      | pcs@gmail.com | Skip     | Skip                              | //div[text()='Password is required'] |
      | Skip          | 1234567  | //div[text()='Email is required'] | Skip                                 |
      | Skip          | Skip     | //div[text()='Email is required'] | //div[text()='Password is required'] |

  Scenario Outline: Login with incorrect credentials
    Then Type "<username>" into "//input[@type = 'text']"
    Then Type "<password>" into "//input[@type = 'password']"
    Then Click element "//button[@type = 'submit']"
    Then Verify presents of element "//p[text()='Invalid username or password']"
    Examples:
      | username                   | password         |
      | houseattheocean@gmail.com  | 123321           |
      | None                       | 1234567          |
      | pcs2@gmail.com             | hr9rsHU6TnWDYnpy |