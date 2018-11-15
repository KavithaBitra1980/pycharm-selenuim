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
        baseUrl = "https://www.expedia.com/"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(20)

        FlightsHotelRadioButton = driver.find_element(By.ID,"fh-fh-hp-package")
        FlightsHotelRadioButton.click()
        driver.save_screenshot("Flight+Hotel.png")
        time.sleep(3)

        FHCRadioButton = driver.find_element(By.ID, "fhc-fhc-hp-package")
        FHCRadioButton.click()
        driver.save_screenshot("Flight+Hotel+Car.png")
        time.sleep(3)


        FCRadioButton = driver.find_element(By.ID, "fc-fc-hp-package")
        FCRadioButton.click()
        driver.save_screenshot("Flight+Car.png")
        time.sleep(3)

        #BMWCheckBox.clear()

        HCRadioButton = driver.find_element(By.ID, "hotel-car-package-type-hp-package")
        HCRadioButton.click()
        driver.save_screenshot("Hotel+Car.png")
        time.sleep(3)

        print('is Radio Button for Flight+Hotel selected or not ?',str(FlightsHotelRadioButton.is_selected()))
        print('is Radio Button for Flight+Hotel+Car selected or not ?', str(FHCRadioButton.is_selected()))
        print('is BMW Check Box for Flight+Car selected or not ?', str(FCRadioButton.is_selected()))
        print('is Benz check box for Hotel+Car selected or not ?', str(HCRadioButton.is_selected()))

        driver.quit()



ff = RadioCheckobox()
ff.testRadioCheckd()