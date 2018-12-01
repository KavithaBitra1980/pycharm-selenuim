#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo of Drag and drop

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

        driver.switch_to.frame(0)
        dragElement = driver.find_element(By.ID,"draggable")
        dropElement = driver.find_element(By.ID,"droppable")
        time.sleep(4)
        try:
            action = ActionChains(driver)
            #action.drag_and_drop(dragElement,dropElement).perform()
            action.click_and_hold(dragElement).move_to_element(dropElement).release(dropElement).perform()
            time.sleep(5)
            print('drop and drop performed')
        except:
            print('Not performed')

dd = dragnDrop()
dd.test_dragnDrop()

