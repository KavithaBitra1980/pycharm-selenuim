#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo for Logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
class dragnDrop():
    def test_dragnDrop(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://jqueryui.com/droppable/"
        driver.implicitly_wait(10)
        driver.get(baseURL)
        title = driver.title
        print(title)
