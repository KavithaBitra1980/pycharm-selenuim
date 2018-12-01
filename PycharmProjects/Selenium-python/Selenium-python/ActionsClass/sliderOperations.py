#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo for Slider

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
class slideElement():
    def test_slideElement(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://jqueryui.com/slider/"
        driver.implicitly_wait(10)
        driver.get(baseURL)
        title = driver.title
        print(title)

        driver.switch_to.frame(0)
        slideElement = driver.find_element(By.XPATH,"//div[@id='slider']//span")
        time.sleep(3)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(slideElement,100,0).perform()
            time.sleep(5)
            print("Element slided")
        except:
            print("not slided'")


ss = slideElement()
ss.test_slideElement()