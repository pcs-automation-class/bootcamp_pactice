from time import sleep
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys


# @step('OM Open "{env}" environment')
# def open_url(context, env):
#     # print(f"Opening url {url}")
#     environments = {
#         "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
#         "prod": "https://app.linkmygear.com",
#         # "qa": "https://test:FjeKB9ySMzwvDUs2XACpfu@qa.linkmygear.com",
#         # "uat": "https://test:FjeKB9ySMzwvDUs2XACpfu@uat.linkmygear.com"
#     }
#     context.driver.get(environments[env])
#     label_xpath = "//h5[text()='Login to Your Account']"
#     verify_presents_of_element(context, label_xpath)


@step('OM Type "{text}" into "{xpath}"')
def type_text(context, text, xpath):
    if text != "Skip":
        # element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element = context.driver.find_element(By.XPATH, xpath)
        element.send_keys(text)

# look to the code
@step('OM Verify presents of element "{xpath}"')
def verify_presents_of_element(context, xpath):
    if xpath != "Skip":
        print(f"Verifying element with xpath: {xpath} presents")
        elements = WebDriverWait(context.driver,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        assert len(elements) == 1
    else:
        print("Step is skipped")


@step('OM Click element "{xpath}"')
def click_element(context,xpath):
    element = context.driver.find_element(By.XPATH,xpath)
    element.click()


# @step('the login page is open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"')
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(
#         u'STEP: Given the login page is open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"')
@step("OM Wait {sec} seconds")
def wait_sec(context,sec):
    sleep(int(sec))
