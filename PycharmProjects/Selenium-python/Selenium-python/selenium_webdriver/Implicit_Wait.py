#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'
#Demo for Implicit_wait

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Implicitwait():
    def test_implicit_wait(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver.implicitly_wait(10)
        driver.get(baseURL)
        title = driver.title
        print(title)

        driver.find_element(By.LINK_TEXT,"Login").click()
        driver.find_element(By.ID,"user_email").send_keys("test@email.com")
        driver.find_element(By.ID,"user_password").send_keys("password")
        driver.find_element(By.NAME,"commit")
        driver.close()

ff = Implicitwait()
ff.test_implicit_wait()
