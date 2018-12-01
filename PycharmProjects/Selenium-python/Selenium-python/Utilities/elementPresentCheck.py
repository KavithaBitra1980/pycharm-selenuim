#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'
#Demo of Element is Present or not

from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.handyWrappers import HandyWrappers
import time

class elementChecks:
    def testelementCheck(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        hw = HandyWrappers(driver)
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        title = driver.title
        print('the title is',title)

        elemetcheck1 = hw.isElementPresent("name","id")
        #elemetcheck1.send_keys("test")
        print(elemetcheck1)
        time.sleep(3)

        elementCheck2 = hw.elementCheck("courses","name")
        print(elementCheck2)
        time.sleep(3)

        elementCheck3 = hw.elementCheck("a", By.TAG_NAME)
        print(elementCheck3)
        time.sleep(3)

        elementCheck4 = hw.elementCheck("//button[@id='openwindow']", By.XPATH)
        print(elementCheck4)
        time.sleep(3)

        elementCheck5 = hw.elementCheck("Sign Up", By.LINK_TEXT)
        print(elementCheck5)
        time.sleep(3)

        driver.close()



ff = elementChecks()
ff.testelementCheck()