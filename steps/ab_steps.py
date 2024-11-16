from behave import step
# from selenium.webdriver.common.keys import Keys

from steps import type_text

@step('AB Input following credentials')
def input_following_credentials(context):
    # print(context.table.rows)
    for row in context.table.rows:
        if row.cells[0] == "username":
            type_text(context, row.cells[1], "//input[@name='username']")
        elif row.cells[0] == "password":
            type_text(context, row.cells[1], "//input[@name='password']")

# @step('AB Type "{text}" into "{xpath}"')
# def type_text(context, text, xpath):
#     print("This is my step")

@step('AB Open "{env}" environment')
def open_url(context, env):
    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com",
        # "qa": "https://test:FjeKB9ySMzwvDUs2XACpfu@qa.linkmygear.com",
        # "uat": "https://test:FjeKB9ySMzwvDUs2XACpfu@uat.linkmygear.com"
    }
    context.driver.get(environments[env])
    label_xpath = "//h5[text()='Login to Your Account']"
    verify_presents_of_element(context, label_xpath)