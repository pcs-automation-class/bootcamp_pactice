Feature: Login Page Tests

Scenario: Valid login

Given the login page is open "dev.linkmygear.com"

And user "Kiwi Tester" has valid credentials

When user enters username "kiwi2024+2@mailinator.com" into username field "//input[@name='username']"

And password "kiwipass02" into password field "//input[@name='password']"

And clicks on Login button "//button[text()=' Login ']"

Then user is logged in
  
And can see Your Devices text "//input[text()=' Your Devices ']"

And can see Error Message1 text "//input[text()=' Your Email or Password is not valid ']"
