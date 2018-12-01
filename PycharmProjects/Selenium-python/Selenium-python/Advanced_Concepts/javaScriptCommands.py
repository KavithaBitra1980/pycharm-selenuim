#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo for JavaScript commands

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class javaScriptCommands():
    def test_javaScript(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        #baseURL = "https://learn.letskodeit.com/p/practice"
        #driver.get(baseURL)
        driver.execute_script("window.location = 'https://learn.letskodeit.com/p/practice';")
        driver.implicitly_wait(10)

        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("test")
        time.sleep(3)

        title = driver.title
        print(title)

js = javaScriptCommands()
js.test_javaScript()