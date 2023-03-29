from time import sleep
from datetime import datetime
from config import TIME_OUT
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

def get_located(search: str, driver, by: MobileBy):
    return WebDriverWait(driver, TIME_OUT).until(
        EC.presence_of_element_located((by, search)))

def click_on(search: str, driver, by: MobileBy):
    get_located(search, driver, by).click()

def send_key(search: str, key: str, driver, by: MobileBy):
    get_located(search, driver, by).send_keys(key)

def scoll_down(times: int, driver):
    begin = 0
    while begin < times:
        action = TouchAction(driver)
        action.press(x=500, y=1200).move_to(x=500, y=0).release().perform()
        begin += 1

def get_strtime(format: str = "%Y-%m-%d_%H-%M-%S"):
    now = datetime.now()
    current_time = now.strftime(format)
    return current_time

def wait_until(wait_until: str):
    wait_until_datetime = datetime.strptime(wait_until, "%Y-%m-%d %H:%M:%S")
    while datetime.now() < wait_until_datetime:
        sleep(0.1)