import pickle
from config import *
from time import sleep
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

def load_cookies(browser,username):
    file_to_load_cookies = ("cookies/%s.pkl" % username)
    cookies = pickle.load(open(file_to_load_cookies, "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    sleep(random_sleep2)
    browser.get('https://www.instagram.com/')
    sleep(random_sleep2)
