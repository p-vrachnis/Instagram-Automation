from threading import Thread
import threading
from random import randint
from credentials import *
from config import *
from instabot import *
from discordbot import *
from account_stats import*
from proxies import *
import time
import logging

def main():
    logging.basicConfig(
        format = '%(levelname)s [%(asctime)s] %(message)s', datefmt = '%m/%d/%Y %r', level = logging.INFO)
    logger = logging.getLogger()
    sleep(5)
    name = sys.argv[1]
    start_time  = datetime.today().strftime('%H:%M:%S')
    start_timer = time.time()

    for i in range (len(clients)):
        if str(name) == clients[i][0]:
            new_client = client(clients[i][0],clients[i][1], i, proxies[i])
            try:
                new_client.run()
            except Exception:
                logger.info(f"{clients[i][0]}: Error exiting")

    if client.succesfull > 0:
        logger.info(f"{name}: Completed succesfully")
        #if execution == "production":
        with open('txt files/Results.txt', 'a') as f:
            f.write("%s --> Success \n" %name )
    else:
        logger.info(f"{name}: Completed unsuccesfully")
        #if execution == "production":
        with open('txt files/Results.txt', 'a') as f:
            f.write("%s --> Failure \n" %name )

    with open('txt files/%s.txt' %name , 'a') as f:
        f.write("{0}: Likes={1} Follows={2} \n".format((datetime.today().strftime('Date: %d-%m-%Y')), (client.user_likes), (client.followed)))

    end_timer  = time.time() - start_timer
    total_time = time.strftime('%H:%M:%S', time.gmtime(end_timer))
    end_time   = datetime.today().strftime('%H:%M:%S')

    if mode == "save_cookies":
        pass
    else:
        send_to_discord(total_time,start_time,end_time)


main()
quit()
