#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo of Drag and drop

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
class dragnDrop_W3():
    def test_dragnDrop_W3(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "http://www.seleniumframework.com/Practiceform/"
        driver.implicitly_wait(10)
        driver.get(baseURL)
        title = driver.title
        print(title)

        dragElement = driver.find_element(By.ID,"draga")
        dropElement = driver.find_element(By.ID,"dragb")

        #dragElement = driver.find_element(By.XPATH,"//button[@id='draga']")
        #dropElement = driver.find_element(By.XPATH,"//button[@id='dragb']")
        time.sleep(3)
        try:
            actions= ActionChains(driver)
            #action.drag_and_drop(dragElement,dropElement).perform()
            actions.click_and_hold(dragElement).move_to_element(dropElement).release(dropElement).perform()
            time.sleep(15)
            print("Action performed")
        except:
            print("Action Not performed")


dd = dragnDrop_W3()
dd.test_dragnDrop_W3()

