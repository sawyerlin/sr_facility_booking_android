import logging
import click

from appium import webdriver
from config import DESIRED_CAPABILITIES
from book_utils import login, locate_facility, book, pay
from utils import get_strtime, wait_until

@click.command()
@click.option('--username', '-u', required=True, help='username')
@click.option('--password', '-p', required=False, help='password')
@click.option('--facility', '-f', required=True, help='facility name, mapping can be found in config')
@click.option('--day', '-d', required=True, help='day')
@click.option('--time', '-t', required=True, help='time')
@click.option('--time_until', '-tu', default="23:59:58", help='specific time on when the facility booking start')
def main(username, password, facility, day, time, time_until):
    password = password if password else click.prompt('Password', hide_input=True)
    try:
        driver = webdriver.Remote('http://localhost:4723/wd/hub', DESIRED_CAPABILITIES)
        login(username, password, driver)
        logging.info("finish login")
        locate_facility(facility, driver)
        logging.info(f"located facility {facility}")

        wait_until(time_until)
        logging.info(f"{time_until} has been reached")

        book(day, time, driver)
        logging.info(f"choosed facility {day} {time}")

        pay(driver)
        logging.info("paied facility")
    except Exception as ex:
        logging.error(ex)

if __name__ == '__main__':
    strtime = get_strtime()
    filename = f"logs/sr_facility_book-{strtime}.log"
    logging.basicConfig(filename=filename, level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
    main()