from time import sleep

from behave import step
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@step('Open "{env}" environment')
def open_url(context, env):
    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com",
    }

    context.driver.get(environments[env])


@step('Wait {sec} seconds')
def wait_sec(context, sec):
    sleep(int(sec))


@step('Click element "{xpath}"')
def click_element(context, xpath):
    element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()


@step('Type "{text}" into "{xpath}"')
def type_text(context, text, xpath):
    if text != "Skip":
        element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
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
        'Settings': "//a[contains(@class, 'profile-btn')]",
        'Billing': "//button[text()='Billing']",
        'Customer Portal': "//button[text()='Customer Portal']"
    }

    element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, buttons[name])))
    # element = context.driver.find_element(By.XPATH, buttons[name])
    element.click()


@step("Click menu Active Jumps")
def open_active_jumps_menu(context, xpath):
    element = context.driver.find_element(By.XPATH, xpath)
    element.click()


@step("Click menu Devices")
def step_impl(context):
    pass


@step("Click menu Records")
def step_impl_1(context):
    pass


@step("Click menu LogBook")
def step_impl_2(context):
    pass


@step("Click menu Group Jumps")
def step_impl_3(context):
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


@step('Click menu "{item}"')
def click_menu(context, item):
    items = {
        'Active Jumps': "//a[text()='Active Jumps']",
        'Devices': "//a[text()='Devices']",
        'Records': "//a[text()='Records']",
        'Logbook': "//a[text()='LogBook']",
        'Group Jumps': "//a[text()='Group Jumps']",
    }
    click_element(context, items[item])


@step('Clear input field "{xpath}"')
def clear_field(context, xpath):
    element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()
    element.send_keys(Keys.COMMAND + "a")
    element.send_keys(Keys.DELETE)


@step('Enter username for user "{name}"')
def enter_username(context, name):
    context.login_page.enter_username(context.credentials[name]['username'])


@step('Clear username')
def clear_username(context):
    context.login_page.clear_username()


@step('Enter password for user "{pwd}"')
def enter_password(context, pwd):
    context.login_page.enter_password(context.credentials[pwd]['password'])


@step("Click login button")
def click_login_btn(context):
    context.login_page.click_login_button()


@step("New step")
def step_impl(context):
    print("New step")
