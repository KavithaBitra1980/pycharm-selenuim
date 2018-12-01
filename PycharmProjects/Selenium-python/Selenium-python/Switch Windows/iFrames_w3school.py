#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo for Iframes

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class switchIFrames_w3():
    def testswitchIFrames_w3(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://www.w3schools.com/html/html_iframe.asp"
        driver.implicitly_wait(15)
        driver.get(baseURL)
        title = driver.title
        print(title)

        driver.switch_to.frame("w3-clear nextprev")
        driver.find_element(By.XPATH,"//a[@class='w3-bar-item w3-button] contains(@href,'/sql/default.asp')").click()
        time.sleep(3)
        driver.switch_to.default_content()
        driver.find_element(By.XPATH, "//a[@class='w3-bar-item w3-button] contains(@href,'/php/default.asp')").click()
        time.sleep(3)


ff = switchIFrames_w3()
ff.testswitchIFrames_w3()