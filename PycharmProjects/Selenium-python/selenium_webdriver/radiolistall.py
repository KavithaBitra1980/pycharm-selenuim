#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#DEMo all

from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.select import Select
import time

class RadioCheckboxHidenShowElements():
    def testRadioCheckHideShow(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(20)

        radiobuttonBMW = driver.find_element(By.ID,"bmwradio")
        radiobuttonBMW.click()
        radio_display=radiobuttonBMW.is_displayed()
        print('the radio button got displayed',radio_display)
        time.sleep(5)

        CheckBox_BMW = driver.find_element(By.ID,"bmwcheck")
        CheckBox_BMW.click()
        checkbox_display = CheckBox_BMW.is_displayed()
        print('the Checkbox Displayed?',checkbox_display)
        time.sleep(5)

        Select_List = driver.find_element(By.ID,"carselect")
        sel = Select(Select_List)
        print('i selected',sel.select_by_visible_text("Honda"))
        time.sleep(5)




        driver.quit()

ff = RadioCheckboxHidenShowElements()
ff.testRadioCheckHideShow()


