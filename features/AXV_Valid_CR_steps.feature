# Created by Anna at 11/12/24
Feature: Login with Valid ID and PW
  # Enter feature description here

Background:
  Given AXV Open "dev" environment

Scenario Outline: AXV Login with Correct Credentials
    Then AXV Type "<username>" into "//input[@name='username']"
    Then AXV Type "<password>" into "//input[@name='password']"
    Then AXV Click element "//button[text()=' Login ']"
    Then AXV Verify presents of element "//h3[text()=' Your device ']"
    Examples:
      | username                  | password         |
      | axv.2000@gmail.com        | KgkbAz7RHCoVD7RE |