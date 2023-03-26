from appium.webdriver.common.mobileby import MobileBy
from utils import click_on, send_key, scoll_down, get_located
from config import FACILITIY_SCROLL_MAPPING

def login(username: str, password: str, driver):
    send_key('com.fermax:id/edtEmail', username, driver, MobileBy.ID)
    send_key('com.fermax:id/edtPassword', password, driver, MobileBy.ID)
    click_on('com.fermax:id/btnLogin', driver, MobileBy.ID)

def locate_facility(facility: str, driver):
    click_on("//android.widget.TextView[@resource-id='com.fermax:id/tvTabName' and @text='Facilities']", driver, MobileBy.XPATH)
    scroll_times = FACILITIY_SCROLL_MAPPING[facility]
    if scroll_times:
        scoll_down(scroll_times, driver)

def book(day: str, time: str, driver):
    facility_linear_layout = get_located("//android.widget.LinearLayout[.//android.widget.TextView[@text='Tennis Court']]", driver, MobileBy.XPATH)
    click_on("com.fermax:id/btnBook", facility_linear_layout, MobileBy.ID)
    click_on(f"//android.widget.TextView[@resource-id='com.fermax:id/tvDate' and @text='{day}']", driver, MobileBy.XPATH)
    click_on(f"//android.widget.TextView[@resource-id='com.fermax:id/tvSlot' and @text='{time}']", driver, MobileBy.XPATH)

def pay(driver):
    click_on("//android.widget.TextView[@resource-id='com.fermax:id/tvSlotSet' and @text='OK']", driver, MobileBy.XPATH)
    click_on("com.fermax:id/lblPaymentTAndC", driver, MobileBy.ID)
    click_on("com.fermax:id/btnAgree", driver, MobileBy.ID)
    click_on("com.fermax:id/btnProceed", driver, MobileBy.ID)
    click_on("android:id/button1", driver, MobileBy.ID)