#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo Radio Element and Check boxes

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RadioCheckobox():
    def testRadioCheckd(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(20)

        BMWRadioButton = driver.find_element(By.ID,"bmwradio")
        BMWRadioButton.click()
        driver.save_screenshot("bmw.png")
        time.sleep(3)

        BnzRadioButton = driver.find_element(By.ID, "benzradio")
        BnzRadioButton.click()
        driver.save_screenshot("bnz.png")
        time.sleep(3)


        BMWCheckBox = driver.find_element(By.ID, "bmwcheck")
        BMWCheckBox.click()
        driver.save_screenshot("BMWCheckBox.png")
        time.sleep(3)

        #BMWCheckBox.clear()

        BnZCheckBox = driver.find_element(By.ID, "benzcheck")
        BnZCheckBox.click()
        driver.save_screenshot("BnZCheckBox.png")
        time.sleep(3)

        print('is Radio Button for BMW selected or not ?',str(BMWRadioButton.is_selected()))
        print('is Radio Button for BNZ selected or not ?', str(BnzRadioButton.is_selected()))
        print('is BMW Check Box for BMW selected or not ?', str(BMWCheckBox.is_selected()))
        print('is Benz check box for selected or not ?', str(BnZCheckBox.is_selected()))

        driver.quit()



ff = RadioCheckobox()
ff.testRadioCheckd()