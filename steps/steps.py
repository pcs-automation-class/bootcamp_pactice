from time import sleep

from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys


@step('Open "{env}" environment')
def open_url(context, env):
    # print(f"Opening url {url}")
    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com",
        # "qa": "https://test:FjeKB9ySMzwvDUs2XACpfu@qa.linkmygear.com",
        # "uat": "https://test:FjeKB9ySMzwvDUs2XACpfu@uat.linkmygear.com"
    }
    context.driver.get(environments[env])


@step('Wait {sec} seconds')
def wait_sec(context, sec):
    sleep(int(sec))



@step('Click element "{xpath}"')
def click_element(context, xpath):
    #element = context.driver.find_element(By.XPATH, xpath)
    element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()


@step('Type "{text}" into "{xpath}"')
def type_text(context, text, xpath):
    # element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    element = context.driver.find_element(By.XPATH, xpath)
    element.send_keys(text)


@step('Verify page by title "{text}"')
def verify_title(context, text):
    sleep(1)
    title = context.driver.title
    assert title == text, f"Expected title: {text}, actual title: {title}. "


@step('Verify presents of element "{xpath}"')
def verify_presents_of_element(context, xpath):
    elements = context.driver.find_elements(By.XPATH, xpath)
    #elements = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
    assert len(elements) == 1


# @step('the login page is open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"')
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(
#         u'STEP: Given the login page is open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"')


@step('Click button "{name}"')
def click_button(context, name):
    buttons = {
        'Login': "//button[text()=' Login ']",
        'Read more': "//button[text()=' Login ']",
        'Log out': "//span[text()='Log out']",
        'Subscribe': "//a[text()='Subscribe']",
        'Subscribe2': "//a[text()='Subscribe2']",
    }

    element = context.driver.find_element(By.XPATH, buttons[name])
    element.click()


@step("Click menu Active Jumps")
def open_active_jumps_menu(context, xpath):
    element = context.driver.find_element(By.XPATH, xpath)
    element.click()

@step("Click menu Devices")
def step_impl(context):
    pass


@step("Click menu Records")
def step_impl(context):
    pass


@step("Click menu LogBook")
def step_impl(context):
    pass


@step("Click menu Group Jumps")
def step_impl(context):
    pass

# @step('Click menu "{item}"')
# def click_menu(context, item):
#     items = {
#         'Active Jumps': "//a[text()='Active Jumps']",
#         'Devices': "//a[text()='Devices']",
#         'Records': "//a[text()='Records']",
#         'Logbook': "//a[text()='LogBook']",
#         'Group Jumps': "//a[text()='Group Jumps']",
#     }
#
#     element = context.driver.find_element(By.XPATH, items[item])
#     element.click()