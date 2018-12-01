#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

class GetAttribute:
    def testAttribute(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        title = driver.title
        print('the title is',title)

        getelement = driver.find_element(By.ID,"displayed-text")
        result = getelement.get_attribute("placeholder")
        print('the attribute value is', result)
        time.sleep(3)

        getelement1 = driver.find_element(By.ID, "hide-textbox")
        result1 = getelement1.get_attribute("onclick")
        print('the attribute value1 is', result1)
        time.sleep(3)

        getelement2 = driver.find_element(By.ID, "confirmbtn")
        result2 = getelement2.get_attribute("value")
        print('the attribute value2 is', result2)
        time.sleep(3)



        driver.quit()

ff = GetAttribute()
ff.testAttribute()



