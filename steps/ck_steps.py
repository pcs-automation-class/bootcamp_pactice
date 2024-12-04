from time import sleep
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys



@step('CK Open "{env}" environment')
def open_url(context, env):
    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com",
    }

    try:
        url = environments[env]
    except KeyError:
        raise ValueError(f"Environment '{env}' is not defined in the environments dictionary.")

    context.driver.get(url)
    label_xpath = "//h5[text()='Login to Your Account']"
    verify_presence_of_element(context, "Login to Your Account")


# Function to log in
@step('CK Login as "{user}" in "{env}" environment')
def login_in_env_with_user_credentials(context, user, env):
    # Call open_url to navigate to the environment
    open_url(context, env)

    # Fetch user credentials (replace this with your credentials storage logic)
    credentials = {
        "test_1": {"username": "catk.test@gmail.com", "password": "strongpassword"}
    }

    user_credentials = credentials.get(user)
    if not user_credentials:
        raise ValueError(f"Credentials for user '{user}' not found.")

    # Locate the username and password fields
    username_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"

    # Type username and password
    type_text(context, user_credentials["username"], username_xpath)
    type_text(context, user_credentials["password"], password_xpath)

    # Click the login button
    ck_click_button(context, "Login")

    # Verify the presence of "Your device"
    verify_presence_of_element(context, "Your device")


# General function to verify the presence of an element
@step('CK Verify presence of element "{element_name}"')
def verify_presence_of_element(context, element_name):
    if element_name.lower() == "skip":
        print("Step is skipped")
        return

    elements_map = {
        "Name": "//div[@class='el-input']//input[@type='text']",
        "Forgot password?": "//a[text()='Forgot password?']",
        "Your email": "//input[@type='text']",
        "Login to Your Account": "//h5[text()='Login to Your Account']",
        "Your device": "//h3[text()=' Your device ']"

    }

    # Get the XPath for the given element name
    xpath_template = elements_map.get(element_name)
    if not xpath_template:
        raise ValueError(f"Element '{element_name}' is not mapped in elements_map or is invalid!")

    # Replace placeholders in the XPath (if any)
    xpath = xpath_template.format(new_name=element_name)

    # Use Selenium to find the element
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        print(f"Element '{element_name}' is present.")
    except Exception as e:
        raise AssertionError(f"Element '{element_name}' not found. Details: {e}")


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
        'Update': "//span[text()='Update']/parent::button",
        "Forgot password?": "//a[text()='Forgot password?']",
        "Send": "//button[contains(@class, 'btn-primary') and contains(@class, 'w-100')]"
    }

    if name not in buttons:
        raise ValueError(f"Button '{name}' is not defined in the buttons dictionary.")

    button_xpath = buttons[name]
    button_element = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, button_xpath))
    )
    button_element.click()
    # context.driver.execute_script("arguments[0].click();", button_element)
    print(f"DEBUG: Clicked button: {name}")


# Updated function to wait for element visibility
def wait_for_element_visibility(context, xpath):
    try:
        element = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return element
    except TimeoutException:
        print(f"Timeout: Element with xpath '{xpath}' not found or not visible.")
        context.driver.save_screenshot("timeout_error_screenshot.png")
        raise


# Function for waiting
@step('CK Wait {sec} seconds')
def wait_sec(context, sec):
    sleep(int(sec))


# Function for clicking an element
@step('CK Click element by XPath "{xpath}"')
def click_element(context, xpath):
    element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()


# Function for renaming a field with test data
@step('CK Rename "{field_name}" to "{new_name}"')
def rename_name_field(context, field_name, new_name):
    fields = {
        'Name': "//div[@class='el-input__wrapper']//input[contains(@class, 'el-input__inner')]",
    }

    if field_name not in fields:
        raise ValueError(f"Field name '{field_name}' not found in fields dictionary.")

    try:
        field_element = WebDriverWait(context.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, fields[field_name]))
        )
        field_element.clear()
        field_element.send_keys(new_name)
    except TimeoutException:
        print(f"Timeout: Could not find or interact with the element '{field_name}' with XPath '{fields[field_name]}'.")
        raise


# Function to open a window based on a given element's XPath
@step('CK Open window "{window_name}"')
def open_window(context, window_name):
    # Define a mapping of window names to their XPaths and expected verification text
    windows = {
        "Device Settings": {
            "xpath": "//a[contains(@href, 'device-settings')]",
            "verification_text": "Device Settings"
        },
        "Forgot password?": {
            "xpath": "//a[normalize-space()='Forgot password?']",
            "verification_text": "Restore Password"
        }
    }

    # Get the specific details for the requested window
    window_details = windows.get(window_name)
    if not window_details:
        raise ValueError(f"Window '{window_name}' is not mapped.")

    # Locate and click the element
    element = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, window_details["xpath"]))
    )
    element.click()

    # Verify that the desired page has opened
    assert window_details["verification_text"] in context.driver.page_source, (
        f"Failed to open '{window_name}' page. "
        f"Expected to see '{window_details['verification_text']}' in the page source."
    )



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
@step('CK Verify pop-up message for "{device_name}"')
def verify_popup_message_step(context, device_name):
    verify_popup_message(context, device_name)


def verify_popup_message(context, device_name):
    expected_message = f"{device_name} succesfully updated"
    popup_xpath = "//div[contains(@class, 'el-message') and contains(@class, 'el-message--success')]"
    popup_element = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, popup_xpath))
    )
    actual_message = popup_element.text
    assert expected_message in actual_message, f"Expected message: '{expected_message}', but got: '{actual_message}'"


# Function to verify updated device name presence
@step('CK Verify updated device name presence "{new_name}"')
def verify_updated_device_name_presence(context, new_name):
    xpath = f"//span[text()='{new_name}']"
    try:
        elements = WebDriverWait(context.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )
        assert len(elements) > 0, f"Updated device name '{new_name}' with xpath '{xpath}' not found."
        print(f"Updated device name '{new_name}' found with xpath: {xpath}")
    except TimeoutException:
        print(f"Timeout: Updated device name '{new_name}' not found with xpath: {xpath}")
        raise


@step('CK the user enters a valid "{email}" into the "Your Email" field')
def enter_valid_email(context, email):
    email_field_xpath = "//input[@type='text']"
    email_field = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, email_field_xpath))
    )
    email_field.clear()
    email_field.send_keys(email)

    # Debugging: Check the entered value in the email field
    entered_email = email_field.get_attribute('value')
    print(f"DEBUG: Entered email in field: {entered_email}")

    assert entered_email == email, f"Expected email '{email}' but found '{entered_email}' in the field."



from time import sleep

@step('CK a confirmation message appears')
def verify_confirmation_message(context):
    # Refined XPath for the confirmation message
    confirmation_message_xpath = "(//h5[contains(@class, 'card-title') and contains(@class, 'text-center')])[2]"

    try:
        # Wait for the confirmation message to be visible
        confirmation_message = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, confirmation_message_xpath))
        )
        # Debugging: Capture the actual message text
        actual_text = confirmation_message.text.strip()
        print(f"DEBUG: Actual confirmation message: {actual_text}")

        # Expected message
        expected_text = "Please check your inbox. You will receive an email with instruction in case if such email exists in our DB"
        assert expected_text in actual_text, f"Expected message '{expected_text}', but got '{actual_text}'"
    except TimeoutException:
        # Save a screenshot and page source for debugging
        context.driver.save_screenshot("timeout_error_debug.png")
        print("DEBUG: Confirmation message not found within the wait time.")
        print(context.driver.page_source)
        raise



