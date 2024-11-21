from time import sleep
import requests
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

BASE_URL = 'https://dev.linkmygear.com/'


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
        elements = (WebDriverWait(context.driver, 10).
                    until(EC.presence_of_all_elements_located((By.XPATH, xpath))))
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
        'Device1': "(//button[text() = ' Edit '])[1]" # second device on the page for testing the rename feature
    }
    element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, buttons[name])))
    # element = context.driver.find_element(By.XPATH, buttons[name])
    element.click()


@step('OK Create new record for device with following data') # API
def ok_add_new_device(context):
    endpoint = 'device-data/airguard/log/v1'
    data = {}
    for row in context.table.rows:
        data[row.cells[0]] = row.cells[1]

    message = (
        f"{data['imei']},{data['date']}191400.000,{data['jump']},3249.34,676.98,32.22,-115,1,1,{data['date']}211429.000,"
        f"{data['latitude']},{data['longitude']},2573.600,,,1,,2.5,,,,20,4,,,28,,,|,771,-115,1723324527")

    response = requests.post(BASE_URL + endpoint, data=message)
    assert response.status_code == 201, f"{response.status_code}: {response.text}"


@step('OK Create new heartbeat message for device with following data') # API
def ok_add_new_device1(context):
    endpoint = 'device-data/airguard/heartbeat/v1'
    data = {}
    for row in context.table.rows:
        data[row.cells[0]] = row.cells[1]

    if data['state'] == "on":
        state = 1
    elif data['state'] == "off":
        state = 2
    else:
        state = 0
    message = (f"{data['imei']},4.05,12.0,39.11,-66,ATT, {data['date']}190424.000,"
               f"{data['latitude']},{data['longitude']},9,{data['date']}190421.000,{data['battery']},{state},,,|,123;")
    response = requests.post(BASE_URL + endpoint, data=message)
    assert response.status_code == 201, f"{response.status_code}: {response.text}"


@step("OK Click menu Active Jumps")
def ok_open_active_jumps_menu(context, xpath):
    element = context.driver.find_element(By.XPATH, xpath)
    element.click()


@step("OK Click menu Devices")
def ok_step_impl(context):
    pass


@step("OK Click menu Records")
def ok_step_impl1(context):
    pass


@step("OK Click menu LogBook")
def ok_step_impl2(context):
    pass


@step("OK Click menu Group Jumps")
def step_impl3(context):
    pass
