from time import sleep

from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# steps/UI/steps.py
from steps.UI.steps import type_text

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
