from instabot import *
import pickle
import undetected_chromedriver.v2 as uc

def save_cookies():
    options = uc.ChromeOptions()
    #options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #options.add_argument("user-data-dir=/home/eniacv/.config/google-chrome")
    #options.add_argument("--profile-directory=Default")
    #options.add_argument('--user-data-dir=C:/Users/EniacV/AppData/Local/Google/Chrome/User Data')
    if execution == "test":
        options.add_argument('--user-data-dir=/home/eniacv/.config/google-chrome')
    else:
        options.add_argument('--user-data-dir=C:/Users/EniacV/AppData/Local/Google/Chrome/User Data')


    browser = uc.Chrome(version_main=98, executable_path=chromedriver_path, options=options)
    browser.implicitly_wait(5)
    #sleep(5)
    browser.get('https://www.instagram.com/')
    sleep(5)
    file_to_save_cookies = ("cookies.pkl")
    pickle.dump(browser.get_cookies(), open(file_to_save_cookies, "wb"))

save_cookies()
