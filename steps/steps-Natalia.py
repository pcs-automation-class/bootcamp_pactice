from time import sleep

from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys


@step('NZ Open "{env}" environment')
def open_url(context, env):
    # print(f"Opening url {url}")
    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com",
        # "qa": "https://test:FjeKB9ySMzwvDUs2XACpfu@qa.linkmygear.com",
        # "uat": "https://test:FjeKB9ySMzwvDUs2XACpfu@uat.linkmygear.com"
    }
    context.driver.get(environments[env])
    label_xpath = "//h5[text()='Login to Your Account']"
    verify_presents_of_element(context, label_xpath)


@step('NZ Wait {sec} seconds')
def wait_sec(context, sec):
    sleep(int(sec))


@step('NZ Click element "{xpath}"')
def click_element(context, xpath):
    element = context.driver.find_element(By.XPATH, xpath)
    # element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()


@step('NZ Type "{text}" into "{xpath}"')
def type_text(context, text, xpath):
    if text != "Skip":
        # element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element = context.driver.find_element(By.XPATH, xpath)
        element.send_keys(text)


@step('NZ Verify page by title "{text}"')
def verify_title(context, text):
    sleep(1)
    title = context.driver.title
    assert title == text, f"Expected title: {text}, actual title: {title}. "


@step('NZ Verify presents of element "{xpath}"')
def verify_presents_of_element(context, xpath):
    if xpath != "Skip":
        print(f"Verify element with xpath {xpath} presents")
        # elements = context.driver.find_elements(By.XPATH, xpath)
        elements = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        assert len(elements) == 1
    else:
        print("Step is skipped")


@step('NZ the login page is open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Given the login page is open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"')


