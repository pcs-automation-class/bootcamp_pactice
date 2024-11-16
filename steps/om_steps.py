from time import sleep

from behave import step
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@step('OM Open "{env}" environment')
def open_url(context, env):
    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com",
    }

    context.driver.get(environments[env])


@step('OM Wait {sec} seconds')
def wait_sec(context,sec):
    sleep(int(sec))


@step('OM Click element "{xpath}"')
def click_element(context,xpath):
    element = WebDriverWait(context.driver,15).until(EC.element_to_be_clickable((By.XPATH,xpath)))
    element.click()


@step('OM Type "{text}" into "{xpath}"')
def type_text(context,text,xpath):
    if text != "Skip":
        element = WebDriverWait(context.driver,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        element.send_keys(text)


@step('OM Verify page by title "{text}"')
def verify_title(context,text):
    sleep(1)
    title = context.driver.title
    assert title == text,f"Expected title: {text}, actual title: {title}. "


@step('OM Verify presents of element "{xpath}"')
def OM_verify_presents_of_element(context,xpath):
    if xpath != "Skip":
        # elements = context.driver.find_elements(By.XPATH, xpath)
        elements = WebDriverWait(context.driver,10).until(EC.presence_of_all_elements_located((By.XPATH,xpath)))
        assert len(elements) == 1,f"Expected 1 element, actual {len(elements)} elements"
    else:
        print("Step is skipped")


@step('OM Click button "{name}"')
def OM_click_button(context, name):
    buttons = {
        'Login': "//button[text()=' Login ']",
        'Read more': "//button[text()=' Login ']",
        'Log out': "//span[text()='Log out']",
        'Subscribe': "//a[text()='Subscribe']",
        'Update': "//button/span[text()='Update']",

    }

    element = WebDriverWait(context.driver,10).until(EC.element_to_be_clickable((By.XPATH,buttons[name])))
    # element = context.driver.find_element(By.XPATH, buttons[name])
    element.click()


@step("OM Click menu Active Jumps")
def open_active_jumps_menu(context, xpath):
    element = context.driver.find_element(By.XPATH, xpath)
    element.click()


@step("OM Click menu Devices")
def step_impl(context):
    pass


@step("OM Click menu Records")
def step_impl(context):
    pass


@step("OM Click menu LogBook")
def step_impl(context):
    pass


@step("OM Click menu Group Jumps")
def step_impl(context):
    pass


@step('OM Login as "{user}" in "{env}" environment')
def login_in_env_with_user_credentials(context,user,env):
    open_url(context,env)
    username_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"
    username = context.credentials[user]['username']
    password = context.credentials[user]['password']
    type_text(context,username,username_xpath)
    type_text(context,password,password_xpath)
    OM_click_button(context,'Login')
    OM_verify_presents_of_element(context,"//h3[@class=' Your device ']")


@step("OM Open window Device Settings")
def open_list_device_settings(context):
    click_element(context,"//a[contains(@href, 'device-settings')]")


@step('OM Click menu "{item}"')
def click_menu(context,item):
    items = {
        'Active Jumps': "//a[text()='Active Jumps']",
        'Devices': "//a[text()='Devices']",
        'Records': "//a[text()='Records']",
        'Logbook': "//a[text()='LogBook']",
        'Group Jumps': "//a[text()='Group Jumps']",
    }
    click_element(context,items[item])


@step('OM Clear input field "{xpath}"')
def clear_field(context,xpath):
    element = WebDriverWait(context.driver,15).until(EC.element_to_be_clickable((By.XPATH,xpath)))
    element.click()
    element.send_keys(Keys.COMMAND + "a")
    element.send_keys(Keys.DELETE)
