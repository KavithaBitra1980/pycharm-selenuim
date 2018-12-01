#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo for Switching windows
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class switchWindow_eshakti():
    def test_switchWindow(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://www.eshakti.com/"
        driver.implicitly_wait(15)
        driver.get(baseURL)
        title = driver.title
        print(title)

        time.sleep(5)

        parentHandler = driver.current_window_handle
        driver.find_element(By.XPATH,"//nav[@id='menu']//a[contains(@href,'/Shop/New Arrivals')]").click()
        driver.execute_script("window.scrollBy(0,200);")
        driver.find_element(By.ID,"quickview0").click()

        handlers = driver.window_handles
        for handle  in handlers:
            if handle not in parentHandler:
                driver.switch_to.window(handle)
                print(handle)
                driver.execute_script("window.scrollBy(0,3200);")
                time.sleep(15)
                driver.find_element(By.ID,"ContentPlaceHolder1_btnAddtoBag").click()
                time.sleep(15)
                alert1 = driver.switch_to.alert
                alert1.accept()
                driver.save_screenshot("addtobag1.png")

        #driver.switch_to.default_content()

        driver.switch_to.window(parentHandler)
        time.sleep(10)
        #driver.close()



ff = switchWindow_eshakti()
ff.test_switchWindow()
