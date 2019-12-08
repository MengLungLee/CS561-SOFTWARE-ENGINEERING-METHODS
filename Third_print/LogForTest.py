# -*- coding: utf-8 -*-
import logging
import requests
import random
from time import sleep
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.ui import Select
import log
import random
import gc
import traceback
from mongoengine.queryset.visitor import Q
from selenium.webdriver.common.keys import Keys

def test_signup(driver):
    btn_url = driver.find_element_by_class_name("signup").find_element_by_tag_name("a").get_attribute("href")
    driver.get(btn_url)
    s_id_box = driver.find_element_by_css_selector("input[name='uid']")
    s_pwd_box = driver.find_element_by_css_selector("input[name='pwd']")
    s_email_box = driver.find_element_by_css_selector("input[name='email']")

    test_id = "test1" + str(random.randint(1,1000))
    test_pwd = test_id
    test_email = "test1@fjsdo.com"

    print("Sign up with id: ", test_id)

    s_id_box.clear()
    s_id_box.send_keys(test_id)
    s_pwd_box.clear()
    s_pwd_box.send_keys(test_pwd)
    s_email_box.clear()
    s_email_box.send_keys(test_email)
    driver.find_element_by_css_selector("input[name='name']").click()
    driver.find_element_by_css_selector("input[name='phone']").click()
    driver.find_element_by_css_selector("input[name='meal']").click()
    sleep(1)

    sbm_btn = driver.find_element_by_css_selector("input[name='submit']")
    sbm_btn.click()

    sleep(2)
    # print(driver.cusrrent_url)

    if "indexmain" in driver.current_url:
        logging.info("Sign up successfully")
    else:
        logging.info("Sign up ERROR!!!")


def test_logout(driver):
    driver.find_element_by_class_name("logout").find_element_by_tag_name("a").click()
    if len(driver.find_elements_by_class_name("login"))> 0:
        # print(len(driver.find_elements_by_class_name("login")))
        logging.info("Logged out")
    else:
        logging.info("Log out ERROR!!!")


def test_login(driver, withoutSignup, uid, pwd):
    if withoutSignup == True:
        btn_url = driver.find_element_by_class_name("login").find_element_by_tag_name("a").get_attribute("href")
        driver.get(btn_url)

    id_box = driver.find_element_by_id("uid")
    pwd_box = driver.find_element_by_id("pwd")

    id_box.clear()
    id_box.send_keys(uid)
    pwd_box.clear()
    pwd_box.send_keys(pwd)
    sleep(1)

    sbm_btn = driver.find_element_by_id("sbm_btn")
    sbm_btn.click()

    sleep(2)

    if len(driver.find_elements_by_class_name("logout")) > 0:
        logging.info("Successfully logged in ")
    else:
        print("uid: ", uid)
        print("pwd: ", pwd)
        logging.info("Login error")

def test_restaurantSearch(driver):

    value_list = [["All", "cafe"], ["Name","cafe"], ["City","Gainesville"]]
    for ea_v in value_list:
        test_restaurant_menu_option(driver, ea_v[0], ea_v[1])

def test_restaurant_menu_option(driver, option, value):

    tmp = "drop-down menu option :" + value 
    logging.info(tmp)

    select = Select(driver.find_element_by_id('category'))
    select.select_by_value(option)
    sleep(1)
    search_box = driver.find_element_by_id("RestaurantName")
    search_box.clear()
    search_box.send_keys(value)
    sleep(1)
    
    srch_btn = driver.find_element_by_id("button")
    srch_btn.click()

    sleep(2)

    tmp_text = driver.find_element_by_css_selector("#msg > table > tbody > tr:nth-child(2)").text.lower()

    if value.lower() in tmp_text:
        logging.info("Successfully finished searching ")
    else:
        if driver.find_element_by_id("msg") == "Not found":
            logging.info("No result. --Successful")
        else: 
            logging.info("Something's wrong...")
            print(value)
            print(tmp_text)
def test_order_h(driver, withoutSignup, uname, order):
    if withoutSignup == True:
        btn_url = driver.find_element_by_class_name("login").find_element_by_tag_name("a").get_attribute("href")
        driver.get(btn_url)

    id_box = driver.find_element_by_id("uname")
    order_box = driver.find_element_by_id("order")

    id_box.clear()
    id_box.send_keys(uname)
    order_box.clear()
    order_box.send_keys(order)
    sleep(1)

    sbm_btn = driver.find_element_by_id("sbm_btn")
    sbm_btn.click()

    sleep(2)

    if len(driver.find_elements_by_class_name("logout")) > 0:
        logging.info("Successfully logged in ")
    else:
        print("uname: ", uname)
        print("order: ", order)
        logging.info("Login error")

def test_restaurantget(driver):

    value_list = [["All", "cafe"], ["Name","cafe"], ["City","Gainesville"]]
    for ea_v in value_list:
        test_restaurant_menu_option(driver, ea_v[0], ea_v[1])

def test_restaurant_menu_option(driver, option, value):

    tmp = "drop-down menu option :" + value 
    logging.info(tmp)

    select = Select(driver.find_element_by_id('category'))
    select.select_by_value(option)
    sleep(1)
    search_box = driver.find_element_by_id("RestaurantName")
    search_box.clear()
    search_box.send_keys(value)
    sleep(1)
    
    srch_btn = driver.find_element_by_id("button")
    srch_btn.click()

    sleep(2)

    tmp_text = driver.find_element_by_css_selector("#msg > table > tbody > tr:nth-child(2)").text.lower()

    if value.lower() in tmp_text:
        logging.info("Successfully finished searching ")
    else:
        if driver.find_element_by_id("msg") == "Not found":
            logging.info("No result. --Successful")
        else: 
            logging.info("Something's wrong...")
            print(value)
            print(tmp_text)

def test_order(driver):
    btn_url = driver.find_element_by_class_name("order").find_element_by_tag_name("a").get_attribute("href")
    driver.get(btn_url)
    
    if "order" in driver.current_url:
        logging.info("Successfully enter find order page.")
    else:
        logging.info("ERROR entering order page!!!")

    value_list = ["Title", "Ingredients", "Instructions"]
    for ea_v in value_list:
        test_order_menu_option(driver, ea_v)


def test_order_menu_option(driver, value):

    tmp = "drop-down menu option :" + value 
    logging.info(tmp)

    search_box = driver.find_element_by_id("ordername")
    search_box.clear()
    search_box.send_keys("fish")
    sleep(1)
    select = Select(driver.find_element_by_id('category'))
    select.select_by_value(value)
    sleep(1)

    srch_btn = driver.find_element_by_id("button")
    srch_btn.click()

    sleep(2)

    tmp_text = driver.find_element_by_css_selector("#msg > table > tbody > tr:nth-child(2)").text.lower()
    if "fish" in tmp_text:
        logging.info("Successfully finished searching ")
    else:
        if driver.find_element_by_id("msg") == "Not found":
            logging.info("No result. --Successful")
        else: 
            logging.info("Something's wrong...")
            print(value)
            print(tmp_text)

def test_feedback(driver):
    btn_url = driver.find_element_by_class_name("feedback").find_element_by_tag_name("a").get_attribute("href")
    driver.get(btn_url)
    
    if "feedback" in driver.current_url:
        logging.info("Successfully enter find feedback page.")
    else:
        logging.info("ERROR entering feedback page!!!")

    value_list = ["Title", "Ingredients", "Instructions"]
    for ea_v in value_list:
        test_feedback_menu_option(driver, ea_v)


def test_feedback_menu_option(driver, value):

    tmp = "drop-down menu option :" + value 
    logging.info(tmp)

    search_box = driver.find_element_by_id("feedbackname")
    search_box.clear()
    search_box.send_keys("fish")
    sleep(1)
    select = Select(driver.find_element_by_id('category'))
    select.select_by_value(value)
    sleep(1)

    srch_btn = driver.find_element_by_id("button")
    srch_btn.click()

    sleep(2)

    tmp_text = driver.find_element_by_css_selector("#msg > table > tbody > tr:nth-child(2)").text.lower()
    if "fish" in tmp_text:
        logging.info("Successfully finished searching ")
    else:
        if driver.find_element_by_id("msg") == "Not found":
            logging.info("No result. --Successful")
        else: 
            logging.info("Something's wrong...")
            print(value)
            print(tmp_text)

def test_userprofile(driver, uid, pwd):

    btn = driver.find_element_by_class_name("userprofile").find_element_by_tag_name("a").get_attribute("href")
    driver.get(btn)

    logging.info("Change id to {}".format(uid+"100"))

    ouid = driver.find_element_by_id("ouid")
    ouid.send_keys(uid)
    nuid = driver.find_element_by_id("nuid")
    nuid.send_keys(uid+"100")

    btn = driver.find_element_by_id("sbm_btn")
    btn.click()

    sleep(2)

    homeurl = driver.find_element_by_class_name("navbar-brand").get_attribute("href")
    driver.get(homeurl)

    sleep(1)

    test_logout(driver)
    
    test_login(driver, True, uid+"100", pwd)
    



def test_ufeeback(driver):
    btn_url = driver.find_element_by_class_name("discussion").find_element_by_tag_name("a").get_attribute("href")
    driver.get(btn_url)

    # add new post
    newpost = driver.find_element_by_id("sidebar").find_element_by_tag_name("a").get_attribute("href")
    driver.get(newpost)

    np_title = driver.find_element_by_name('title')
    np_title.send_keys("test post"+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    np_name = driver.find_element_by_name('name')
    np_name.send_keys("test")

    np_cont = driver.find_element_by_name('content')
    np_cont.send_keys("testing")

    sbm = driver.find_element_by_css_selector("#entries > form > p > input[type='submit']")
    sbm.click()

    tmp_text = driver.find_element_by_id("entries").text
    if "testing" in tmp_text:
        logging.info("Successfully posted ")
    else:
        logging.info("Something's wrong...")
        print(tmp_text)


    #reply
    reply = driver.find_element_by_css_selector("#sidebar > a:nth-child(2)").get_attribute("href")
    driver.get(reply)

    rp_name = driver.find_element_by_name('name')
    rp_name.send_keys("testR")

    rp_cont = driver.find_element_by_name('content')
    rp_cont.send_keys("test reply")

    sbm = driver.find_element_by_css_selector('#entries > form > input[type="submit"]:nth-child(4)')
    sbm.click()

    tmp_text = driver.find_element_by_id("entries").text
    if "testR" in tmp_text:
        logging.info("Successfully replied ")
    else:
        logging.info("Something's wrong...")
        print(tmp_text)

    # back to home page
    home_btn = driver.find_element_by_css_selector("#sidebar > a:nth-child(1)").get_attribute("href")
    driver.get(home_btn)

    logging.info("Finished all tests!!")



if __name__ == "__main__":
    open_crawl()
