#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class windowSizes():
    def test_windowSize(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        #baseURL = "https://learn.letskodeit.com/p/practice"
        #driver.get(baseURL)
        driver.execute_script("window.location = 'https://learn.letskodeit.com/p/practice';")

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth")
        print("Height" +str(height))
        print("Width" + str(width))


ws = windowSizes()
ws.test_windowSize()