from time import sleep
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import json

# Function to open a URL in the specified environment
@step('CK Open "{env}" environment')
def open_url(context, env):
    # Environments dictionary placed inside the function
    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com",
        # Add other environments as needed
    }

    try:
        url = environments[env]
    except KeyError:
        raise ValueError(f"Environment '{env}' is not defined in the environments dictionary.")

    context.driver.get(url)
    label_xpath = "//h5[text()='Login to Your Account']"
    verify_presence_of_element(context, label_xpath)


# Function to log in
@step('CK Login as "{user}" in "{env}" environment')
def login_in_env_with_user_credentials(context, user, env):
    open_url(context, env)

    try:
        username = context.credentials[user]['username']
        password = context.credentials[user]['password']
    except KeyError:
        raise ValueError(f"User '{user}' is not found in the credentials dictionary.")

    username_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"
    type_text(context, username, username_xpath)
    type_text(context, password, password_xpath)
    ck_click_button(context, 'Login')

    device_label_xpath = "//h3[text()=' Your device ']"
    verify_presence_of_element(context, device_label_xpath)


# General function to verify the presence of an element
@step('CK Verify presence of element "{element_name}"')
def verify_presence_of_element(context, element_name):
    if element_name.lower() == "skip":
        print("Step is skipped")
        return

    # Check if the identifier is a known element name or an XPath
    elements_map = {
        "Name": "//div[@class='el-input__wrapper']//input[contains(@class, 'el-input__inner')]",
        # Add other element names as needed
    }

    xpath = elements_map.get(element_name, element_name)  # Use XPath directly if not in elements_map

    try:
        elements = WebDriverWait(context.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )
        assert len(elements) > 0, f"Element '{element_name}' with xpath '{xpath}' not found."
        print(f"Element '{element_name}' found with xpath: {xpath}")
    except TimeoutException:
        print(f"Timeout: Element '{element_name}' not found with xpath: {xpath}")
        raise


# Function to type text into a field
def type_text(context, text, xpath):
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    element.clear()
    element.send_keys(text)


# Function to click a button
@step('CK Click button "{name}"')
def ck_click_button(context, name):
    buttons = {
        'Login': "//button[contains(text(), 'Login')]",
        'Read more': "//button[text()='Read more']",
        'Log out': "//span[text()='Log out']",
        'Subscribe': "//a[text()='Subscribe']",
        'Show on map': "//button[text()='Show on map']",
        'Edit': "//div[@class='btns']/button[contains(text(), 'Edit')]",
        'Delete': "//div[@class='btns']/button[contains(text(), 'Delete')]",
        'Add New Device': "//span[text()='Add new device']/parent::button",
        'Update': "//span[text()='Update']/parent::button"
    }

    if name not in buttons:
        raise ValueError(f"Button '{name}' is not defined in the buttons dictionary.")

    button_xpath = buttons[name]
    button_element = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, button_xpath))
    )
    button_element.click()

# Updated function to wait for element visibility
def wait_for_element_visibility(context, xpath):
    try:
        element = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return element
    except TimeoutException:
        print(f"Timeout: Element with xpath '{xpath}' not found or not visible.")
        context.driver.save_screenshot("timeout_error_screenshot.png")  # Save screenshot for debugging
        raise


# Function for waiting
@step('CK Wait {sec} seconds')
def wait_sec(context, sec):
    sleep(int(sec))

# Function for clicking an element
@step('CK Click element by XPath "{xpath}"')
def click_element(context, xpath):
    element = context.driver.find_element(By.XPATH, xpath)
    # element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

# Function for typing text into a specific xpath
@step('CK Type "{text}" into "{xpath}"')
def type_text(context, text, xpath):
    if text.lower() == "none":
        text = ""  # Convert 'none' to an empty string
    if text != "Skip":
        element = context.driver.find_element(By.XPATH, xpath)
        element.send_keys(text)

# Function for renaming a field with test data
@step('CK Rename "{field_name}" to "{new_name}"')
def rename_name_field(context, field_name, new_name):
    # Dictionary of field XPaths
    fields = {
        'Name': "//div[@class='el-input__wrapper']//input[contains(@class, 'el-input__inner')]",
    }

    if field_name not in fields:
        raise ValueError(f"Field name '{field_name}' not found in fields dictionary.")

    try:
        # Locate the field element using a more generous wait time and suitable condition
        field_element = WebDriverWait(context.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, fields[field_name]))
        )
        field_element.clear()
        field_element.send_keys(new_name)
    except TimeoutException:
        print(f"Timeout: Could not find or interact with the element '{field_name}' with XPath '{fields[field_name]}'.")
        raise

# Function to open the Device Settings window
@step("CK Open window Device Settings")
def open_list_device_settings(context):
    xpath = "//a[contains(@href, 'device-settings')]"
    element = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    element.click()


# Function to verify device name update
@step('CK Verify device name is updated to "{new_name}"')
def verify_device_name_updated(context, new_name):
    updated_name_xpath = f"//span[text()='{new_name}']"
    try:
        element = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, updated_name_xpath))
        )
        displayed_name = element.text
        assert displayed_name == new_name, f"Expected device name '{new_name}', but got '{displayed_name}'."
        print(f"Device name '{new_name}' is successfully updated and displayed correctly.")
    except TimeoutException:
        print(f"Timeout: Device name '{new_name}' is not found on the page.")
        raise


# Function to open device settings by IMEI
@step("CK Open settings for device with IMEI '{imei}'")
def open_device_settings(context, imei):
    xpath = f"//td[text()='{imei}']/following-sibling::td//button[text()='Edit']"
    element = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    element.click()


# Function to verify a pop-up message
def verify_popup_message(context, device_name):
    expected_message = f"{device_name} successfully updated"
    popup_xpath = "//div[contains(@class, 'popup') or contains(@class, 'notification')]"
    popup_element = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, popup_xpath))
    )
    actual_message = popup_element.text
    assert expected_message in actual_message, f"Expected message: '{expected_message}', but got: '{actual_message}'"


@step('CK Verify pop-up message for "{device_name}"')
def verify_popup_message_step(context, device_name):
    verify_popup_message(context, device_name)

