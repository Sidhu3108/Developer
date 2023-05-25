from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# from td_facebook import page_url, page_title,user_name, password_fb
# from facebook.helper import *
import time
import csv

from Facebook.helper import webdriver_browser
from Facebook.test_data import *

#locators

login_email_id = "//*[@placeholder='Email address or phone number']"
login_password_name = 'pass'
login_btn_name = 'login'

driver = webdriver_browser('EDGE')
def check_title():
    global driver

    driver.get(page_url)
    assert driver.title == page_title

def test_sinup():
    try:
        driver.get(page_url)

        email_txt = driver.find_element(By.XPATH, login_email_id)
        email_txt.send_keys(user_name)
        driver.find_element(By.NAME, login_password_name).send_keys(password_fb)
        driver.find_element(By.NAME, login_btn_name).click()


    except NoSuchElementException:
        print("Element not foundy")
    except AssertionError:
        print("element not enabled")

        print("XYZ")