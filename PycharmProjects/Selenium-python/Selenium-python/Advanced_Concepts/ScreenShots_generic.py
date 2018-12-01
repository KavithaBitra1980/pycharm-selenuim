#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshot_generic():
    def test_Screenshot(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver.implicitly_wait(15)
        driver.get(baseURL)
        title = driver.title
        print(title)

        driver.find_element(By.LINK_TEXT,"Login").click()
        driver.find_element(By.ID,"user_email").send_keys("test@email.com")
        driver.find_element(By.ID,"user_password").send_keys("abcabc")
        driver.find_element(By.NAME,"commit").click()
        self.takeScreenshot(driver)
        driver.close()



    def takeScreenshot(self,driver):

        screenShotDirectory = "C:\\users\\Bitra\\SeleniumScreenshots"
        fileName = str(round(time.time() * 1000) )+ ".png"
        destinationFile = screenShotDirectory + fileName

        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory-->::" + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")

ss = Screenshot_generic()
ss.test_Screenshot()
