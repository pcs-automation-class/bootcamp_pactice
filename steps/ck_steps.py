from time import sleep
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


@step('CK Open "{env}" environment')
def open_url(context, env):
    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com"
    }
    if env not in environments:
        raise ValueError(f"Environment '{env}' is not defined.")

    context.driver.get(environments[env])
    label_xpath = "//h5[text()='Login to Your Account']"
    verify_presence_of_element(context, label_xpath)


@step('CK Wait {sec} seconds')
def wait_sec(context, sec):
    sleep(int(sec))


@step('CK Click element "{xpath}"')
def click_element(context, xpath):
    element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

    # Explicitly wait for the next page to load or a specific element to appear
    try:
        WebDriverWait(context.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//h3[text()=' Your device ']"))
        )
    except TimeoutException:
        raise AssertionError("The next page did not load within the expected time.")


@step('CK Type "{text}" into "{xpath}"')
def type_text(context, text, xpath):
    if text != "Skip":
        element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(text)


@step('CK Verify page by title "{text}"')
def verify_title(context, text):
    sleep(1)
    title = context.driver.title
    assert title == text, f"Expected title: {text}, actual title: {title}."


@step('CK Verify presence of element "{xpath}"')
def verify_presence_of_element(context, xpath):
    if xpath != "Skip":
        print(f"Verifying presence of element with XPath: {xpath}")
        try:
            element = WebDriverWait(context.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            assert element is not None, f"Element with XPath '{xpath}' not found or not visible."
        except TimeoutException:
            context.driver.save_screenshot('screenshot.png')
            print("Screenshot saved for debugging.")
            raise AssertionError(f"Timed out waiting for element with XPath: {xpath}")
    else:
        print("Step is skipped")

@step('the login page is open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Given the login page is open "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"')
