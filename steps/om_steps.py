from time import sleep

from behave import step
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@step('OM Open "{env}" environment')
def OM_open_url(context, env):
    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com",
    }

    context.driver.get(environments[env])


@step('OM Wait {sec} seconds')
def OM_wait_sec(context, sec):
    sleep(int(sec))


@step('OM Click element "{xpath}"')
def OM_click_element(context, xpath):
    element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()


@step('OM Type "{text}" into "{xpath}"')
def OM_type_text(context, text, xpath):
    if text != "Skip":
        element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(text)


@step('OM Verify page by title "{text}"')
def OM_verify_title(context, text):
    sleep(1)
    title = context.driver.title
    assert title == text, f"Expected title: {text}, actual title: {title}. "


@step('OM Verify presents of element "{xpath}"')
def OM_verify_presents_of_element(context, xpath):
    if xpath != "Skip":
        # elements = context.driver.find_elements(By.XPATH, xpath)
        elements = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        assert len(elements) == 1, f"Expected 1 element, actual {len(elements)} elements"
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
        'Edit': "(//button[contains(text(), ' Edit ')])[1]",
        'Add new device': "//span[contains(text(), 'Add new device')]",
        '+ Add new device': "//div[@class='form-submit']",
        'Delete': "(//button[@class='lmg-btn lmg-btn--sm lmg-btn--w-100 lmg-btn--red'])[1]",
        'Delete_1': "//button[@class='lmg-btn lmg-btn--red']",
    }

    element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, buttons[name])))
    element.click()


@step("OM Click menu Active Jumps")
def OM_open_active_jumps_menu(context, xpath):
    element = context.driver.find_element(By.XPATH, xpath)
    element.click()


@step("OM Click menu Devices")
def OM_step_impl(context):
    pass


@step("OM Click menu Records")
def OM_step_impl_1(context):
    pass


@step("OM Click menu LogBook")
def OM_step_impl_2(context):
    pass


@step("OM Click menu Group Jumps")
def OM_step_impl_3(context):
    pass


@step('OM Login as "{user}" in "{env}" environment')
def OM_login_in_env_with_user_credentials(context, user, env):
    OM_open_url(context, env)
    username_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"
    username = context.credentials[user]['username']
    password = context.credentials[user]['password']
    OM_type_text(context, username, username_xpath)
    OM_type_text(context, password, password_xpath)
    OM_click_button(context, 'Login')
    OM_verify_presents_of_element(context, "//h3[@class=' Your device ']")


@step("OM Open window Device Settings")
def OM_open_list_device_settings(context):
    OM_click_element(context, "//a[contains(@href, 'device-settings')]")


@step('OM Click menu "{item}"')
def OM_click_menu(context, item):
    items = {
        'Active Jumps': "//a[text()='Active Jumps']",
        'Devices': "//a[text()='Devices']",
        'Records': "//a[text()='Records']",
        'Logbook': "//a[text()='LogBook']",
        'Group Jumps': "//a[text()='Group Jumps']",
    }
    OM_click_element(context, items[item])


@step('OM Clear input field "{xpath}"')
def OM_clear_field(context, xpath):
    element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()
    element.send_keys(Keys.COMMAND + "a")
    element.send_keys(Keys.DELETE)


@step('OM Pop-up window "{xpath}" should appear')
def OM_window_opened(context, xpath):
    element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    print(f"Pop-up window with text: {element.text} ")


@step('I choose "{imei}" from the "{dropdown_menu}"')
def choose_from_dropdown(context, imei, dropdown_menu):
    dropdown_menu_xpath = dropdown_menu

    class_name = "el-scrollbar__view el-select-dropdown__list"
    imei_xpath = f"//ul[@class='{class_name}']"

    # imei_xpath = f"//ul[@class='el-scrollbar__view el-select-dropdown__list']"

    # Wait for the dropdown menu to be clickable and click it
    dropdown_element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, dropdown_menu_xpath))
    )
    dropdown_element.click()

    # Wait for the option to appear and click it
    option_element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, imei_xpath))
    )
    option_element.click()

    # Confirmation log
    print(f"Selected imei: '{imei}' from the dropdown menu.")


@step('OM Verify the pop-up message "{message}" is displayed')
def OM_verify_popup_message(context, message):

    popup_xpath = "//div[contains(@class, 'el-message') and contains(@class, 'el-message--success')]"

    try:

        popup_element: WebElement = WebDriverWait(context.driver, 10).until(
          EC.presence_of_element_located((By.XPATH, popup_xpath))
        )

# Fetch the test of message
        popup_text = popup_element.text
        print(f"Pop-up message capture: {popup_text}")

        assert message in popup_text, f"{popup_text} not found in pop-up"

    except TimeoutException:
        raise AssertionError(f"Pop-up message {message} did not appear in pop-up")


@step("OM Pop-up window should appear")
def window_appear(context):
    OM_verify_presents_of_element(context, "//h3[@class='modal-title']")


@step('OM Enter username "{name}"')
def OM_enter_username(context, name):
    context.login_page.enter_username(name)


@step('OM Clear username')
def OM_clear_username(context):
    context.login_page.OM_clear_username()


@step('OM Enter password "{pwd}"')
def OM_enter_password(context, pwd):
    context.login_page.enter_password(pwd)


@step("OM Click login button")
def OM_click_login_btn(context):
    context.login_page.click_login_button()

# @step('OM Click element "{forgot_password}"')
# def OM_forgot_password(context, forgot_password):
#     context.login_page.forgot_password(forgot_password)
