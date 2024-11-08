from time import sleep

from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys


@step('AB Input following credentials')
def input_following_credentials(context):
    print(context.table.rows)


@step('AB Type "{text}" into "{xpath}"')
def type_text(context, text, xpath):
    print("This is my step")
