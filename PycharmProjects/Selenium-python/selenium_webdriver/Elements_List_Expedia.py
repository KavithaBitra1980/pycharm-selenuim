#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo of Elements LIst

from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

class ElemetsList():
    def testList(self):
        baseUrl = "https://expedia.com"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(20)

        radioButtonslist = driver.find_elements(By.XPATH, "//input[contains(@type, 'radio') and contains(@name, 'package-type')]")


        size = len(radioButtonslist)
        print('the size of the radio buttons is ', size)




        for each_radioButton in radioButtonslist:
            is_Selected = each_radioButton.is_selected()

        if not is_Selected:
            each_radioButton.click()
            time.sleep(3)
        sizetable = len(elementsList)
        print('the size of the table is',sizetable)

ff = ElemetsList()
ff.testList()

