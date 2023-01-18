import pickle
from time import sleep
import logging
from config import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC


class Save_Cookies:
    def __init__(self, browser, username, password):
        self.browser = browser
        self.username = username
        self.password = password

    def login(self):
        logging.basicConfig(
            format = '%(levelname)s [%(asctime)s] %(message)s', datefmt = '%m/%d/%Y %r', level = logging.INFO)
        logger = logging.getLogger()
        # #Accept all
        # sleep(random_sleep2)
        # try:
        #     #browser.find_element_by_xpath('//button[contains(text(), "Accept All")]').click()
        #     WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accept All")]'))).click()
        # except Exception:
        #     pass
        #     # sleep(random_sleep1)
        #     # browser.refresh()
        #     # sleep(random_sleep1)
        #     # WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accept All")]'))).click()
        #
        # sleep(random_sleep2)

        #Get the login elements and type in your credentials
        username = self.browser.find_element_by_name('username')
        username.send_keys(self.username)
        password = self.browser.find_element_by_name('password')
        password.send_keys(self.password)
        sleep(random_sleep2)

        # Click the login button
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()
        #WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='loginForm']/div/div[3]/button"))).click()

        #If login information is incorrect, program will stop running
        try:
            if self.browser.find_element_by_xpath("//*[@id='slfErrorAlert']"):
                self.browser.close()
                sys.exit('Error: Login information is incorrect')
            else:
                pass
        except:
            sleep(random_sleep2)
            pass
        sleep(random_sleep2)

        file_to_save_cookies = ("cookies/%s.pkl" % self.username)
        cookies = self.browser.get_cookies()
        for cookie in cookies:
            if cookie.get('expiry', None) is not None:
                cookie['expires'] = cookie.pop('expiry')
        pickle.dump(cookies, open(file_to_save_cookies, "wb"))
        #pickle.dump(self.browser.get_cookies(), open(file_to_save_cookies, "wb"))
        logger.info(f"cookies saved succesfully for {self.username}")
