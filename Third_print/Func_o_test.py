# -*- coding: utf-8 -*-
import logging
import requests
import random

from time import sleep
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.ui import Select

import log

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

def test_userprofile(driver, uname, order):

    btn = driver.find_element_by_class_name("userprofile").find_element_by_tag_name("a").get_attribute("href")
    driver.get(btn)

    logging.info("Change id to {}".format(uname+"100"))

    ouname = driver.find_element_by_id("ouname")
    ouname.send_keys(uname)
    nuname = driver.find_element_by_id("nuname")
    nuname.send_keys(uname+"100")

    btn = driver.find_element_by_id("sbm_btn")
    btn.click()

    sleep(2)

    homeurl = driver.find_element_by_class_name("navbar-brand").get_attribute("href")
    driver.get(homeurl)

    sleep(1)

    test_logout(driver)
    
    test_login(driver, True, uname+"100", order)
    



def test_discussion(driver):
    btn_url = driver.find_element_by_class_name("discussion").find_element_by_tag_name("a").get_attribute("href")
    driver.get(btn_url)

    # add new post
    newpost = driver.find_element_by_id("sidebar").find_element_by_tag_name("a").get_attribute("href")
    driver.get(newpost)

    np_title = driver.find_element_by_name('title')
    np_title.send_keys("test post"+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    np_name = driver.find_element_by_name('name')
    np_name.send_keys("test")

    np_cont = driver.find_element_by_name('order1')
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

    rp_cont = driver.find_element_by_name('order1')
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
