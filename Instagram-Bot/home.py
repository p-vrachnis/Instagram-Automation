import logging
from config import *
from time import sleep

def loop(browser, logger, username):
    sleep(random_sleep1)
    logger.info(f"{username}: Scrolling")
    for i in range(5):
        browser.execute_script('window.scrollTo(0,200)')
        sleep(random_sleep1)
    sleep(random_sleep2)
    browser.get(f'https://www.instagram.com/')
    sleep(random_sleep2)
    logger.info(f"{username}: Opening story")
    browser.find_element_by_class_name("OE3OK ").click()
    sleep(random_sleep3)
    logger.info(f"{username}: Closing story")
    browser.find_element_by_class_name("wpO6b  ").click()
    sleep(random_sleep2)

def home_interrupt(username, browser):
    logging.basicConfig(
        format = '%(levelname)s [%(asctime)s] %(message)s', datefmt = '%m/%d/%Y %r', level = logging.INFO)
    logger = logging.getLogger()
    logger.info(f"{username}: Going to homepage")
    sleep(random_sleep1)
    for i in range(1):
        loop(browser, logger, username)
