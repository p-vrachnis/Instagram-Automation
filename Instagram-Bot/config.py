from random import randint
from credentials import *
import sys

# execution = "test"
execution = "production"

mode = "normal"
if len(sys.argv) > 2:
    mode = sys.argv[2]
#mode = "save_cookies"

number_of_accounts = 5

# Global list of hashtags to go through
#hashtag_list = "athens"

# Global list of accounts to follow it's followers
# accounts_to_follow_from = ["antica_restaurant"]

#execution type: test or production
if execution == "test":
    #max_likes = 1

    like1 = 1
    like2 = 1

    follow1 = 1
    follow2 = 1

else:
    #max_likes = randint(150/280, 200/320)
    like1 = 100
    like2 = 125
    #max_follows = randint (30/50, 50/80) # 0
    follow1 = 10
    follow2 = 15

# Time to wait in between processing instagram posts in seconds
# Enter lower and upper limit in randint()
wait_between_posts = randint(15, 20)

random_sleep1 = randint (10, 15)
random_sleep2 = randint (15, 20)
random_sleep3 = randint (20, 25)

# Time to wait in between liking a post and commenting on it in seconds
# Enter lower and upper limit in randint()
# wait_to_like = randint(110,130)
# wait_to_follow = randint(160, 190)
wait_to_comment = randint(15, 20)
wait_to_like = randint(15, 20)
wait_to_follow = randint(10, 20)

# Chance of commenting on photo
# i.e. chance_to_comment = 4 means a 1/4 chance
chance_to_comment = 1

# List of comments to be randomly chosen from
comments_list = ['Love this!', 'Nice shot :)', 'Amazing~', 'Looks great! :)', 'Beautiful']

# def comment():
#     # Random chance of commenting
#     do_i_comment = 0
#     #do_i_comment = randint(1, chance_to_comment)
#     if do_i_comment == 1:
#         try:
#             # Comment
#             browser.find_element_by_xpath("//form").click()
#             comment = browser.find_element_by_xpath("//textarea")
#
#             sleep(wait_to_comment)
#
#             rand_comment_index = randint(0, len(comments_list))
#             comment.send_keys(comments_list[rand_comment_index])
#             comment.send_keys(Keys.ENTER)
#             logger.info(
#                 f"Commented '{comments_list[rand_comment_index]}'")
#             comments += 1
#
#         except Exception:
#             # Continue to next post if comments section is limited or turned off
#             continue

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
***IMPORTANT***

Please be aware of Instagram's daily limits for likes and comments to avoid getting banned

https://socialpros.co/instagram-daily-limits#Instagram%E2%80%99s_Daily_Limits_in_2020

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
