#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

# DEMO for Auto Complete or Auto suggest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AutoComplete():
    def testAutoComplete(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://www.southwest.com/"
        driver.implicitly_wait(15)
        driver.get(baseURL)
        title = driver.title
        print(title)

        depart = driver.find_element(By.ID,"air-city-departure")
        depart.send_keys("New")
        time.sleep(3)
        driver.find_element(By.XPATH,"//li[contains(text(),'NY - LGA')]").click()
        driver.save_screenshot("autocomplete.png")
        #driver.close()
ff = AutoComplete()
ff.testAutoComplete()
