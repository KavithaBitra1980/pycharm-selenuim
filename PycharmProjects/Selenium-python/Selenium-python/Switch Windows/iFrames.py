#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class switchIFrames():
    def testswitchIFrames(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver.implicitly_wait(15)
        driver.get(baseURL)
        title = driver.title
        print(title)
        Height = driver.execute_script("return window.innerHeight;")
        print(Height)
        driver.execute_script("window.scrollBy(0,1100);")

        #driver.switch_to.frame("courses-iframe")
        #driver.switch_to.frame("iframe-name")
        driver.switch_to.frame(0)

        time.sleep(5)
        driver.find_element(By.ID,"search-courses").send_keys("python")
        driver.save_screenshot("iframsdate.png")
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-1100);")
        driver.find_element(By.ID,"name").send_keys("testautomation")
        time.sleep(3)
ff = switchIFrames()
ff.testswitchIFrames()
