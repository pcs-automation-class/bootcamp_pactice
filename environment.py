from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
import json


def before_all(context):
    with open("setup.json", "r") as file:
        context.credentials = json.load(file)


def before_scenario(context, scenario):
    if "EMULATE" not in scenario.name:
        chrome_options = ChromeOptions()
        context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        context.driver.maximize_window()


def after_scenario(context, scenario):
    if "EMULATE" not in scenario.name:
        context.driver.quit()
