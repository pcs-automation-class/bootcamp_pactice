from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
import json


def before_all(context):
    with open("setup.json", "r") as file:
        context.credentials = json.load(file)


#
# def before_feature(context, feature):
#     print("before_feature")


def before_scenario(context, scenario):
    # print("before_scenario")

    chrome_options = ChromeOptions()
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    context.driver.maximize_window()

# def before_step(context, step):
#     print("before_step", step.name)

#
# def after_step(context, step):
#     print("after_step")


def after_scenario(context, scenario):
    # print("after_scenario")
    context.driver.quit()

# def after_feature(context, feature):
#     print("after_feature")

#
# def after_all(context):
#     """
#     Clean up the testing environment after all tests have run.
#
#     :param context: The Behave context object that holds shared data between steps and hooks.
#     """
#     # context.driver.quit()
