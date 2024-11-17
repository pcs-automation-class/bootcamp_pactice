from time import sleep
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




@step('CK Open "{env}" environment')
def open_url(context, env):
    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com",
        # "qa": "https://test:FjeKB9ySMzwvDUs2XACpfu@qa.linkmygear.com",
        # "uat": "https://test:FjeKB9ySMzwvDUs2XACpfu@uat.linkmygear.com"
    }
    context.driver.get(environments[env])
    label_xpath = "//h5[text()='Login to Your Account']"
    verify_presence_of_element(context, label_xpath)


@step('CK Wait {sec} seconds')
def wait_sec(context, sec):
    sleep(int(sec))


@step('CK Click element "{xpath}"')
def click_element(context, xpath):
    element = context.driver.find_element(By.XPATH, xpath)
    # element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()



@step('CK Type "{text}" into "{xpath}"')
def type_text(context, text, xpath):
    if text.lower() == "none":
        text = ""  # Convert 'none' to an empty string
    if text != "Skip":
        element = context.driver.find_element(By.XPATH, xpath)
        element.send_keys(text)


@step('CK Verify page by title "{text}"')
def verify_title(context, text):
    sleep(1)
    title = context.driver.title
    assert title == text, f"Expected title: {text}, actual title: {title}. "


@step('CK Verify presence of element "{xpath}"')
def verify_presence_of_element(context, xpath):
    if xpath != "Skip":
        print(f"Verifying presence of element with xpath: {xpath}")
        elements = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        assert len(elements) > 0, f"Element with xpath '{xpath}' not found."
    else:
        print("Step is skipped")


def verify_presents_of_element(context, xpath):
    print(f"Verify element with xpath {xpath} presents")
    # elements = context.driver.find_elements(By.XPATH, xpath)
    elements = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
    assert len(elements) == 1

@given('CK the login page is open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Given the login page is open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"')

@step('CK Click button "{name}"')
def ck_click_button(context, name):
    buttons = {

        'Login': "//button[text()='Login']",
        'Read more': "//button[text()='Read more']",
        'Log out': "//span[text()='Log out']",
        'Subscribe': "//a[text()='Subscribe']",
        'Subscribe2': "//a[text()='Subscribe2']",
        'Show on map': "//button[text()='Show on map']",
        'Demo Jump': "//button[text()='Demo Jump']",
        'Resend Activation Link': "//button[text()='Resend Activation Link']",
        # Device Settings
        'Edit': "//div[@class='btns']/button[contains(text(), 'Edit')]",
        'Delete': "//div[@class='btns']/button[contains(text(), 'Delete')]",
        'Add New Device': "//span[text()='Add new device']/parent::button"
    }

    element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, buttons[name])))
    # element = context.driver.find_element(By.XPATH, buttons[name])
    element.click()

@step('CK Type "{text}" into "{field_name}"')
def type_text_in_field(context, text, field_name):
    # Dictionary of field XPaths
    fields = {
        'Name': "//div[@class='el-input__wrapper']//input[contains(@class, 'el-input__inner')]",
    }
    # Wait for the field to be present and interactable
    field_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, fields[field_name]))
    )
    # Clear the field and type the text
    field_element.clear()
    field_element.send_keys(text)


@step("CK Click menu Devices")
def step_impl(context):
    pass

@step("CK Click menu Records")
def step_impl(context):
    pass

@step("CK Click menu LogBook")
def step_impl(context):
    pass

@step("CK Click menu Group Jumps")
def step_impl(context):
    pass

@step('CK Login as "{user}" in "{env}" environment')
def login_in_env_with_user_credentials(context, user, env):
    open_url(context, env)
    username_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"
    username = context.credentials[user]['username']
    password = context.credentials[user]['password']
    type_text(context, username, username_xpath)
    type_text(context, password, password_xpath)
    ck_click_button(context, 'Login')
    verify_presence_of_element(context, "//h3[text()=' Your device ']")


@step("CK Open window Device Settings")
def open_list_device_settings(context):
    # Define the XPath for the "Device Settings" link
    xpath = "//a[contains(@href, 'device-settings')]"

    # Wait for the element to be clickable
    element = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )

    # Click the "Device Settings" link
    element.click()

@step("CK Open settings for device with IMEI '{imei}'")
def open_device_settings(context, imei):
    # Construct the XPath using the IMEI
    xpath = f"//td[text()='{imei}']/following-sibling::td//button[text()='Edit']"

    # Wait for the "Edit" button to be clickable
    element = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )

    # Click the "Edit" button to open the device settings
    element.click()


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