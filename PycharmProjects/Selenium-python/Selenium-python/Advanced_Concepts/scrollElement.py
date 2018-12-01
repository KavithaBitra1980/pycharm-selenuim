#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class scrollElemente():
    def testScrollElement(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver.implicitly_wait(15)
        driver.get(baseURL)
        title = driver.title
        print(title)

        driver.execute_script("window.scrollBy(0,1100);")
        time.sleep(3)
        print("1")
        driver.execute_script("window.scrollBy(0,-1100);")
        time.sleep(3)
        print("2")
        element = driver.find_element(By.ID,"mousehover")
        time.sleep(3)
        print("3")
        driver.execute_script("arguments[0].scrollIntoView(true);",element)
        time.sleep(3)
        print("4")
        driver.execute_script("window.scrollBy(0,-250);")
        time.sleep(3)
        print("4")
        driver.execute_script("window.scrollBy(0,1100);")
        time.sleep(3)
        print("5")
        location = element.location_once_scrolled_into_view
        print("location " +str(location))


ss = scrollElemente()
ss.testScrollElement()