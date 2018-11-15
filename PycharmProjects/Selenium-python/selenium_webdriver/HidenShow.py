#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.select import Select
import time

class HidenShowElements():
    def testHideShow(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(20)

        textBoxElement = driver.find_element(By.ID,"displayed-text")
        textBoxState = textBoxElement.is_displayed()
        print('The sate os the text box is',str(textBoxState))
        time.sleep(3)

        driver.find_element(By.ID,"hide-textbox").click()
        hideElementState =textBoxElement.is_displayed()
        print('the state of hide box is',hideElementState)
        time.sleep(10)


        driver.find_element(By.ID,"show-textbox").click()
        showElementState =textBoxElement.is_displayed()
        print('the state of hide box is',showElementState)
        time.sleep(10)

        driver.close()

ff = HidenShowElements()
ff.testHideShow()

