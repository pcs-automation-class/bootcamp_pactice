from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.header_login = (By.XPATH, "//h5[text()='Login to Your Account']")
        self.username = (By.XPATH, "//input[@name='username']")
        self.password = (By.XPATH, "//input[@name='password']")
        self.button_login = (By.XPATH, "//button[text()=' Login ']")
        self.forgot_password = (By.XPATH, "//a[text()='Forgot password?']")
        self.create_account = (By.XPATH, "//a[text()='Create an account']")

    def enter_username(self, username):
        # element = self.driver.find_element(*self.username)
        element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.username))
        element.send_keys(username)
        # self.driver.find_element(*self.username).send_keys(username)

    def clear_username(self):
        # element = self.driver.find_element(*self.username)
        element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.username))
        element.click()
        element.send_keys(Keys.COMMAND + "a")
        element.send_keys(Keys.DELETE)

    def enter_password(self, password):
        # element = self.driver.find_element(*self.password)
        element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.password))
        element.send_keys(password)

    def click_login_button(self):
        # element = self.driver.find_element(*self.button_login)
        element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_login))
        element.click()
