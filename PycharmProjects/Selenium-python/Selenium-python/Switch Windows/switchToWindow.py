#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo for Switching windows
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class switchWindow():
    def test_switchWindow(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver.implicitly_wait(15)
        driver.get(baseURL)
        title = driver.title
        print(title)

        parentHandle = driver.current_window_handle
        print('The Parent Handle is',parentHandle)

        driver.find_element(By.ID,"openwindow").click()
        time.sleep(3)

        handles = driver.window_handles
        for handle in handles:
            print("Handle",handle)
            if handle  not in parentHandle:
                driver.switch_to.window(handle)
                print("The Window is switched is to child window that is search")
                searchBox = driver.find_element(By.ID,"search-courses")
                searchBox.send_keys("python")
                driver.save_screenshot("python.png")
                time.sleep(3)
                driver.close()
        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID,"name").send_keys("name")
        time.sleep(5)


ff = switchWindow()
ff.test_switchWindow()
