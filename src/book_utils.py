import logging
from appium.webdriver.common.mobileby import MobileBy
from utils import click_on, send_key, scoll_down, get_located, wait_until
from config import FACILITIY_SCROLL_MAPPING, FACILITIY_NAME_MAPPING

def login(username: str, password: str, driver):
    send_key('com.fermax:id/edtEmail', username, driver, MobileBy.ID)
    send_key('com.fermax:id/edtPassword', password, driver, MobileBy.ID)
    click_on('com.fermax:id/btnLogin', driver, MobileBy.ID)

def locate_facility(facility: str, driver):
    click_on("//android.widget.TextView[@resource-id='com.fermax:id/tvTabName' and @text='Facilities']", driver, MobileBy.XPATH)
    scroll_times = FACILITIY_SCROLL_MAPPING[facility]
    if scroll_times:
        scoll_down(scroll_times, driver)

def book(day: str, time: str, facility: str, is_next_month: bool, time_until: str, driver):
    def click_facility():
        facility_linear_layout = get_located(
            f"//android.widget.LinearLayout[.//android.widget.TextView[@text='{FACILITIY_NAME_MAPPING[facility]}']]", driver, MobileBy.XPATH)
        click_on("com.fermax:id/btnBook", facility_linear_layout, MobileBy.ID)
        logging.info("clicked on book")

    if is_next_month:
        click_facility()
        wait_until(time_until)
        logging.info(f"{time_until} has been reached")
        click_on("com.fermax:id/calendar_right_arrow", driver, MobileBy.ID)
        logging.info("next month")
    else:
        wait_until(time_until)
        logging.info(f"{time_until} has been reached")
        click_facility()

    click_on(f"//android.widget.TextView[@resource-id='com.fermax:id/tvDate' and @text='{day}']", driver, MobileBy.XPATH)
    logging.info(f"selected day {day}")
    click_on(f"//android.widget.TextView[@resource-id='com.fermax:id/tvSlot' and @text='{time}']", driver, MobileBy.XPATH)
    logging.info(f"selected time {time}")
    click_on("com.fermax:id/tvSlotSet", driver, MobileBy.ID)
    logging.info("clicked ok")

def pay(driver):
    click_on("com.fermax:id/lblPaymentTAndC", driver, MobileBy.ID)
    logging.info("payment t and c")
    click_on("com.fermax:id/btnAgree", driver, MobileBy.ID)
    logging.info("payment agree")
    click_on("com.fermax:id/btnProceed", driver, MobileBy.ID)
    logging.info("payment proceed")
    click_on("android:id/button1", driver, MobileBy.ID)
    logging.info("payment confirmd")