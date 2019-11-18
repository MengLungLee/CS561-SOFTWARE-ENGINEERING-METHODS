# -*- coding: utf-8 -*-
import logging
import random
import gc
import traceback

from time import sleep
from datetime import datetime
from selenium import webdriver
from mongoengine.queryset.visitor import Q
from selenium.webdriver.common.keys import Keys

import log
import Func_test

def open_crawl():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--disable-notifications')
    # chromeOptions.add_argument('--headless')
    chromeOptions.add_argument('--disable-gpu')

    driver = webdriver.Chrome(chrome_options=chromeOptions)

    try:
        crawler(driver)
        driver.close()
    except Exception as e:
        logging.info(traceback.format_exc())
        driver.close()
        
def crawler(driver):
    driver.get("http://people.oregonstate.edu/~chanchek/login.php")

    logging.info("Now testing restaurant recommendation system")
    # search for restaurant recommendation
    withoutSignupTest = True
    Func_test.test_restaurantSearch(driver)

    logging.info("Now testing new sign up function")
    # test sign up function
    Func_test.test_signup(driver)

    # logging.info("Now testing login function")
    # # test login function
    # Func_test.test_login(driver, withoutSignupTest, "test1766", "test1766")
    # sleep(1)


    logging.info("Now testing log out function")
    # test log out function
    Func_test.test_logout(driver)

    logging.info("Now testing login function")
    # test login function
    Func_test.test_login(driver, withoutSignupTest, "test1766", "test1766")
    sleep(1)

    logging.info("Now testing recipe recommendation system")
    # test recipe function
    Func_test.test_recipe(driver)
    sleep(1)

    logging.info("Now testing user profile system")
    # test userprofile function
    Func_test.test_userprofile(driver, "test1766", "test1766")
    sleep(1)

    logging.info("Now testing discussion board system")
    # test discussion function
    Func_test.test_discussion(driver)
    sleep(1) 

if __name__ == "__main__":
    open_crawl()
