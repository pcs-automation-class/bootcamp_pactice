from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# def before_all(context):
#     print("before_all")


# def before_feature(context, feature):
#     print("before_feature")
#
#
def before_scenario(context, scenario):
    # print("before_scenario")

    # context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    chrome_options = ChromeOptions()
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    context.driver.maximize_window()

# def before_step(context, step):
#     print("before_step")
#
#
# def after_step(context, step):
#     print("after_step")


def after_scenario(context, scenario):
    print("after_scenario")
    context.driver.quit()

# def after_feature(context, feature):
#     print("after_feature")


# def after_all(context):
#     """
#     Clean up the testing environment after all tests have run.
#
#     :param context: The Behave context object that holds shared data between steps and hooks.
#     """
#     context.driver.quit()
