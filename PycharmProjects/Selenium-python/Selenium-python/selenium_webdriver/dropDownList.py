#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.select import Select
import time

class ElemetSelectList():
    def testSelect(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(20)

        elementsSelect = driver.find_element(By.ID,"carselect")
        sel = Select(elementsSelect)

        sel_index=sel.select_by_index(2)
        print('the value by index is',sel_index)
        time.sleep(3)

        sel_value = sel.select_by_value("bmw")
        print('the value by value is',sel_value)
        time.sleep(3)

        sel_visualvalue = sel.select_by_visible_text("Honda")
        print('The visual value is',sel_visualvalue)



ff = ElemetSelectList()
ff.testSelect()
