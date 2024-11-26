from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import json
from pom.LoginPage import LoginPage
from pom.ABLoginPage import ABLoginPage


browser = "Chrome"


def before_all(context):
    with open("setup.json", "r") as file:
        context.credentials = json.load(file)


def before_scenario(context, scenario):
    if "EMULATE" not in scenario.name:
        if browser == "Chrome":
            chrome_options = ChromeOptions()
            context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                              options=chrome_options)
        elif browser == "Firefox":
            firefox_options = FirefoxOptions()
            context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                               options=firefox_options)
        else:
            assert False, "Unknown browser!"

        context.driver.maximize_window()
        context.login_page = LoginPage(context.driver)
        context.ab_login_page = ABLoginPage(context.driver)


def after_scenario(context, scenario):
    if "EMULATE" not in scenario.name:
        context.driver.quit()
