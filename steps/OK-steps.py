from time import sleep

from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


@step('OK Open "{env}" environment')
def ok_open_url(context, env):
    # print(f"Opening url {url}")
    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com",
    }
    context.driver.get(environments[env])
    label_xpath = "//h5[text()='Login to Your Account']"
    ok_verify_presents_of_element(context, label_xpath)


@step('OK Wait {sec} seconds')
def ok_wait_sec(context, sec):
    sleep(int(sec))


@step('OK Click element "{xpath}"')
def ok_click_element(context, xpath):
    element = context.driver.find_element(By.XPATH, xpath)
    # element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()


@step('OK Type "{text}" into "{xpath}"')
def ok_type_text(context, text, xpath):
    if text != "Skip":
        # element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element = context.driver.find_element(By.XPATH, xpath)
        element.send_keys(text)


@step('OK Verify page by title "{text}"')
def ok_verify_title(context, text):
    sleep(1)
    title = context.driver.title
    assert title == text, f"Expected title: {text}, actual title: {title}. "


@step('OK Verify presents of element "{xpath}"')
def ok_verify_presents_of_element(context, xpath):
    if xpath != "Skip":
        print(f"Verify element with xpath {xpath} presents")
        # elements = context.driver.find_elements(By.XPATH, xpath)
        elements = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        assert len(elements) == 1
    else:
        print("Step is skipped")


@step('OK Clear the field "{xpath}"')
def ok_clear_input_field(context, xpath):
    input_field = context.driver.find_element(By.XPATH, xpath)
    input_field.click()
    input_field.send_keys(Keys.CONTROL, 'a')
    input_field.send_keys(Keys.DELETE)


@step('OK Click button "{name}"')
def ok_click_button(context, name):
    buttons = {
        'Login': "//button[text()=' Login ']",
        'Read more': "//button[text()=' Login ']",
        'Log out': "//span[text()='Log out']",
        'Subscribe': "//a[text()='Subscribe']",
        'Update': "//button/span[text()='Update']",
        'Send': "//button[text() = ' Send ']",
        'Device settings': "//a[@href='#/device-settings']/i",
        'Device1': "(//button[text() = ' Edit '])[1]" #second device on the page for testing the rename feature
    }
    element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, buttons[name])))
    # element = context.driver.find_element(By.XPATH, buttons[name])
    element.click()

