#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'
#DEMO of an element whether is enabled or NOT

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class enabledORNot():
    def testenabled(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(20)

        e1 = driver.find_element_by_class_name("gLFyf")
        e1State = e1.is_enabled()
        print("e1 is enabled or not",str(e1State))
        e1.send_keys("america")
        time.sleep(3)
        if e1 is not None:
            print("element found")

        e2 = driver.find_element_by_class_name("RNNXgb")
        e2State = e2.is_enabled()
        print("e1 is enabled or not", str(e2State))
        e2.send_keys("India")
        time.sleep(3)
        if e2 is not None:
            print("element found")

        driver.close()

ff = enabledORNot()
ff.testenabled()





