from config import *
from credentials import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import logging
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

SCROLL_PAUSE_TIME = 5

class InstaFollower:
    def __init__(self, browser, account):
        self.browser = browser
        self.people = []
        self.account = account

    def find_followers(self):
        sleep(random_sleep2)
        self.browser.get(
          f'https://www.instagram.com/{self.account}/')
        sleep(random_sleep2)

        followers = self.browser.find_element_by_css_selector("ul li a")
        followers.click()
        sleep(random_sleep1)

    def follow(self):
        logging.basicConfig(
            format = '%(levelname)s [%(asctime)s] %(message)s', datefmt = '%m/%d/%Y %r', level = logging.INFO)
        logger = logging.getLogger()
        sleep(random_sleep1)
        self.people = self.browser.find_elements_by_css_selector("li div div button")
        max_follows = randint(follow1, follow2)
        follow_limit = max_follows
        followed = 0
        try:
            for person in self.people:
                if person.text == "Follow":
                    sleep(wait_to_follow)
                    sleep(random_sleep2)
                    person.click()
                    followed += 1
                    logger.info(f'{self.account}: follows {followed}')
                    sleep(random_sleep2)
                    sleep(wait_to_follow)
                else:
                    logger.info(f"{self.account}: Already followed")
                if followed == follow_limit:
                    break
            sleep(random_sleep1)
            return followed

        except Exception:
            return followed
