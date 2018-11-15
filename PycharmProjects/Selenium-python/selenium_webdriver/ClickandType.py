#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo of Click and Type on web element
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class clickandType():
    def ClickType(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"

        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        try:
            Login = driver.find_element(By.XPATH,"//div[@id='navbar']//a[@href='/sign_in']")
            Login.click()
        #time.sleep(3)
            emailField = driver.find_element(By.ID, "user_email")
            emailField.send_keys("test@test.com")
        #time.sleep(3)
            passwordFiels = driver.find_element(By.ID, "user_password")
            passwordFiels.send_keys("test")

        #time.sleep(3)
            emailField.clear()

        #time.sleep(3)
            emailField.send_keys("test")


            driver.find_element(By.NAME,"commit").click()
            driver.save_screenshot("page1.png")
            driver.quit()
        except:
            print("error")
        finally:
            print("got executed")



ff = clickandType()
ff.ClickType()