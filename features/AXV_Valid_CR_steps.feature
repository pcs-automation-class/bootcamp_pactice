Feature: Login with Valid ID and PW

Background:
  Given AXV Open "dev" environment

Scenario Outline: AXV Login with Correct Credentials
    Then AXV Type "<username>" into "//input[@name='username']"
    Then AXV Type "<password>" into "//input[@name='password']"
    Then AXV Click element "//button[text()=' Login ']"
    Then Wait 1 seconds
    Then AXV Verify presents of element "//h3[text()=' Your device ']"
    Examples:
      | username                  | password         |
      | test.axv.2000@gmail.com   | KgkbAz7RHCoVD7RE |