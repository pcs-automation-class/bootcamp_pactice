from time import sleep
from xml.etree.ElementPath import xpath_tokenizer

from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys


@step('Open "{env}" environment')
def open_url(context, env):
    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com",
    }

    context.driver.get(environments[env])
    label_xpath = "//h5[text()='Login to Your Account']"
    verify_presents_of_element(context, label_xpath)


@step('Wait {sec} seconds')
def wait_sec(context, sec):
    sleep(int(sec))


@step('Click element "{xpath}"')
def click_element(context, xpath):
    # element = context.driver.find_element(By.XPATH, xpath)
    element =  WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()


@step('Type "{text}" into "{xpath}"')
def type_text(context, text, xpath):
    element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    # element = context.driver.find_element(By.XPATH, xpath)
    element.send_keys(text)


@step('Verify page by title "{text}"')
def verify_title(context, text):
    sleep(1)
    title = context.driver.title
    assert title == text, f"Expected title: {text}, actual title: {title}. "


@step('Verify presents of element "{xpath}"')
def verify_presents_of_element(context, xpath):
    if xpath != "Skip":
        # elements = context.driver.find_elements(By.XPATH, xpath)
        elements = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        assert len(elements) == 1, f"Expected 1 element, actual {len(elements)} elements"
    else:
        print("Step is skipped")


@step('Click button "{name}"')
def ab_click_button(context, name):
    buttons = {
        'Login': "//button[text()=' Login ']",
        'Read more': "//button[text()=' Login ']",
        'Log out': "//span[text()='Log out']",
        'Subscribe': "//a[text()='Subscribe']",
        'Update': "//button/span[text()='Update']",

    }

    element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, buttons[name])))
    # element = context.driver.find_element(By.XPATH, buttons[name])
    element.click()


@step("Go to menu Active Jumps")
def open_active_jumps_menu(context):
    pass

@step("Go to menu devices")
def step_impl(context):
    pass


@step("Go to menu records")
def step_impl(context):
    pass


@step("Go to menu logbook")
def step_impl(context):
    pass


@step("Go to menu group jumps")
def step_impl(context):
    pass


@step('Login as "{user}" in "{env}" environment')
def login_in_env_with_user_credentials(context, user, env):
    open_url(context, env)
    username_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"
    username = context.credentials[user]['username']
    password = context.credentials[user]['password']
    type_text(context, username, username_xpath)
    type_text(context, password, password_xpath)
    ab_click_button(context, 'Login')
    verify_presents_of_element(context, "//h3[text()=' Your device ']")


@step("Open window Device Settings")
def open_list_device_settings(context):
    click_element(context, "//a[contains(@href, 'device-settings')]")
    # xpath = "//a[contains(@href, 'device-settings')]"
    # element =  WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    # element.click()