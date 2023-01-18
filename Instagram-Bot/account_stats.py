from time import sleep
import logging
from config import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC

def get_stats(browser,username):
      logging.basicConfig(
        format = '%(levelname)s [%(asctime)s] %(message)s', datefmt = '%m/%d/%Y %r', level = logging.INFO)
      logger = logging.getLogger()
      sleep(random_sleep2)

      browser.get(
        f'https://www.instagram.com/{username}/')
      logger.info(f'{username}: Exploring #{username}')
      sleep(random_sleep2)

      posts = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[1]/div/span')
      media = posts.get_attribute("innerHTML")
      followers = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div/span')
      number_of_followers = followers.get_attribute("innerHTML")
      following = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div/span')
      number_of_following = following.get_attribute("innerHTML")

      return media, number_of_followers, number_of_following
