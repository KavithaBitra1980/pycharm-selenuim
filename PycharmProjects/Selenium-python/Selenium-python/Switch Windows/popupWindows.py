#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo of Pop up windows

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class popupWindows():
    def testPopupWindows(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver.implicitly_wait(15)
        driver.get(baseURL)
        title = driver.title
        print(title)

        driver.find_element(By.ID,"name").send_keys("test")
        driver.find_element(By.ID,"alertbtn").click()
        time.sleep(5)
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(5)
        driver.find_element(By.ID, "name").send_keys("test")
        driver.find_element(By.ID,"confirmbtn").click()
        time.sleep(5)
        confirm1 = driver.switch_to.alert
        time.sleep(5)
        confirm1.dismiss()

ff = popupWindows()
ff.testPopupWindows()