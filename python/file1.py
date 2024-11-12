# from python.file3 import print_hello2
from lib2to3.fixes.fix_input import context

from python.file2 import greetings
from python.file3 import *

# import python.file3
# python.file3.print_hello()

print_hello()
abc = print_hello2()
print(f"This is from file 2: {abc}")
print_hello3()
greetings()


# ------

context = None

def open_url(context, env):
    # print(f"Opening url {url}")
    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com",
    }
    context.driver.get(environments[env])
    label_xpath = "//h5[text()='Login to Your Account']"
    verify_presents_of_element(context, label_xpath)


def input_following_credentials(context):
    # print(context.table.rows)
    for row in context.table.rows:
        if row.cells[0] == "username":
            type_text(context, row.cells[1], "//input[@name='username']")
        elif row.cells[0] == "password":
            type_text(context, row.cells[1], "//input[@name='password']")


def type_text(context, text, xpath):
    if text != "Skip":
        # element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element = context.driver.find_element(By.XPATH, xpath)
        element.send_keys(text)

open_url(context, "dev")
input_following_credentials(context)
type_text(context, "pcs.automationclass@gmail.com", "//input[@name='username']")