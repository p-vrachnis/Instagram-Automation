from time import sleep
import logging
import sys
from credentials import *
from config import *
from account_stats import *
from load_cookies import *
from save_cookies import *
from home import *
import undetected_chromedriver.v2 as uc2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import warnings
from threading import Thread
import threading
from instafollow import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class client(object):
    user_likes = 0
    followed   = 0
    unfollowed = 0
    statistics = "None"
    succesfull = 0
    user_i     = 0

    def __init__(self, username,password, count, proxy):
        self.username = username
        self.password = password
        self.count    = count
        self.proxy    = proxy

    def run(self):
        client.user_i = self.count
        warnings.filterwarnings("ignore")
        logging.basicConfig(
            format = '%(levelname)s [%(asctime)s] %(message)s', datefmt = '%m/%d/%Y %r', level = logging.INFO)
        logger = logging.getLogger()
        logger.info(f"{self.username} started")

        #System.setProperty(ChromeDriverService.CHROME_DRIVER_SILENT_OUTPUT_PROPERTY,“true”)

        # Do this so we don't get DevTools and Default Adapter failure
        options = webdriver.ChromeOptions()
        # options.add_argument('--ignore-ssl-errors=yes')
        # options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        # options.add_argument("--dns-prefetch-disable")
        # options.add_argument("--disable-gpu")
        # options.add_argument("disable-features=NetworkService")
        # options.add_argument('disable-infobars')
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        #options.setPageLoadStrategy(PageLoadStrategy.NORMAL)
        #options.add_argument('--disable-dev-shm-usage')

        #set proxy
        options.add_argument('--proxy-server=%s' % self.proxy)

        # Initialize hub
        browser = webdriver.Remote(command_executor='http://hub:4444/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)

        # If selenium can't find an element, it waits 5 sec to let things load and tries again
        browser.implicitly_wait(5)

        #check ip
        # browser.get("https://www.google.com/search?client=firefox-b-d&q=whats+my+ip")
        # browser.get("https://www.whatismyip.com/")

        # Run chrome
        try:
            browser.get('https://www.instagram.com/')
        except TimeoutException:
            sleep(random_sleep1)
            browser.refresh()
        sleep(random_sleep1)

        #Allow essential cookies
        browser.find_element_by_xpath('//button[contains(text(), "Only allow essential cookies")]').click()
        sleep(random_sleep2)

        if mode == "save_cookies":
            cookies_mode = Save_Cookies(browser, self.username, self.password)
            cookies_mode.login()
            return
        else:
            load_cookies(browser, self.username)
        sleep(random_sleep1)

        logger.info(f'Logged in to {self.username}')

        # Save your login info? Not now
        try:
            WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/div/div/section/main/div/div/div/div/button"))).click()
            #browser.find_element_by_xpath("//*[@id='react-root']/div/div/section/main/div/div/div/div/button").click()
        except Exception:
            pass
            # sleep(random_sleep1)
            # browser.refresh()
            # sleep(random_sleep2)
            # WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/div/div/section/main/div/div/div/div/button"))).click()
        sleep(random_sleep1)

        # Turn on notifications? Not now
        try:
            WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]"))).click()
            #browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        except Exception:
            pass
        sleep(random_sleep1)

        #get account stats
        try:
            stats=get_stats(browser, self.username)
        except Exception:
            return
        client.statistics = "Media: " + stats[0] + "\nFollowers: "+ stats[1] + "\nFollowing: " + stats[2]
        logger.info(f"{self.username}: Stats phase succesfull")

        #Like from hashtag
        # Keep track of how many you like and comment
        likes = 0
        temp_likes = randint(20,30)
        comments = 0
        # Index for tags in hashtag list
        sleep(random_sleep2)
        for hashtag in hashtag_list[self.count]:
            if hashtag == "":
                break
            home_interrupt(self.username, browser)
            browser.get(
                f'https://www.instagram.com/explore/tags/{hashtag}/')
            logger.info(f'{self.username}: Exploring #{hashtag}')
            sleep(random_sleep2)

            try:
                # Click first thumbnail to open
                first_thumbnail = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]"))).click()

            except TimeoutException:
                sleep(random_sleep1)
                browser.refresh()
                sleep(random_sleep2)
                first_thumbnail = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]"))).click()

            max_likes = randint(like1, like2)
            number_of_posts = max_likes - clients[self.count][3]
            post = 0
            # Go through x number of photos per hashtag
            while post < number_of_posts:
                sleep(random_sleep2)
                try:
                    # Check if the post is already liked
                    # If not, then like, comment, and go to next post
                    browser.find_element_by_xpath("//*[@aria-label='Unlike']")
                    logger.info(f"{self.username}: Already liked")
                    number_of_posts += 1
                except Exception:
                    sleep (random_sleep2)
                    try:
                        #Like
                        browser.find_element_by_class_name('fr66n').click() # click the like button
                        likes += 1
                        sleep(wait_to_like)
                        client.user_likes = likes
                        logger.info(f"{self.username}: Likes {likes}")
                    except Exception:
                        pass

                if likes == (max_likes - (clients[self.count][3]/len(hashtag_list[self.count]))):
                    break
                elif likes == temp_likes:
                     temp_likes = temp_likes + randint(20,30)
                     #go to home to do some stuff
                     home_interrupt(self.username, browser)
                     browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
                     logger.info(f'{self.username}: Returning to #{hashtag}')
                     sleep(random_sleep2)
                     first_thumbnail = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]"))).click()



                # Go to next post
                sleep(wait_between_posts)
                try:
                    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='Next']"))).click()
                # except TimeoutException:
                #     sleep(random_sleep1)
                #     browser.refresh()
                #     sleep(random_sleep2)
                #     WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='Next']"))).click()

                except ElementClickInterceptedException:
                    return

                #browser.find_element_by_xpath("//*[@aria-label='Next']").click()
                logger.info(f'{self.username}: Getting next post')
                post += 1

        logger.info(f'{self.username}: liked {likes} posts')
        logger.info(f"{self.username}: Like phase succesfull")


        #follow from accounts
        if clients[self.count][4] == True:
            for account in follow[self.count]:
                insta_follower = InstaFollower(browser, account)
                insta_follower.find_followers()
                client.followed = client.followed + insta_follower.follow()
            logger.info(f"{self.username}: Follow phase succesfull")

        client.succesfull += 1


        browser.close()
