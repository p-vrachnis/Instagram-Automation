# import logging
# from config import *
# import logging
# import logging.handlers
# import logging.config
#
# default_logger = logging.getLogger("instabot")
# logging_file = "instabot.log"
# logging.basicConfig(filename=logging_file, format='%(asctime)s %(levelname)-8s %(message)s', level=logging.DEBUG)
# default_logger.setLevel(logging.DEBUG)
# # Add the log message handler to the logger
# handler = logging.handlers.RotatingFileHandler(
#     logging_file, backupCount=5)
#
# default_logger.addHandler(handler)
#
#
# def stopLogging():
#     logging.config.stopListening()
#
#
# def follow():
# 	for i in fam:
# 		browser.visit("https://www.instagram.com/" + i)
# 		browser.is_text_present('Follow', wait_time=10)
# 		browser.find_by_text('Follow').first.click()
# 		browser.is_text_present('Following', wait_time=10)
#
# def unfollow():
# 	for i in fam:
# 		browser.visit("https://www.instagram.com/" + i)
# 		browser.is_text_present('Following', wait_time=10)
# 		browser.find_by_text('Following').first.click()
# 		browser.is_text_present('Unfollow', wait_time=10)
# 		browser.find_by_text('Unfollow').first.click()
# 		browser.is_text_present('Follow', wait_time=10)
