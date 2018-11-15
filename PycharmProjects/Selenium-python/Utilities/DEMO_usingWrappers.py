#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'


#Demo of Using wrappers
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.handyWrappers import HandyWrappers
import time

class usingWrappers:
    def testWrappers(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        hw = HandyWrappers(driver)
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        title = driver.title
        print('the title is',title)

        textFiled = hw.getElement("name")
        textFiled.send_keys("Test")
        time.sleep(3)

        textFiled3 = hw.getElement("bmwcheck")
        textFiled3.click()
        time.sleep(3)

        textfiled2 = hw.getElement("//input[@id='name']",locatorType="xpath")
        textfiled2.clear()
        time.sleep(3)

        textfiled4 = hw.getElement("//input[@id='bmwradio']", locatorType="xpath")
        textfiled4.click()
        time.sleep(3)

        textfiled5 = hw.getElement("//button[@id='openwindow']", locatorType="xpath")
        textfiled5.click()
        time.sleep(3)
        driver.save_screenshot("newwindows.png")
        #driver.close()

        textfiled6 = hw.getElement("Sign Up", locatorType="link_text")
        textfiled6.click()
        time.sleep(3)
        driver.save_screenshot("newwindows1.png")
        driver.back()

        textfiled7 = hw.getElement("courses", locatorType="name")
        print(textfiled7)
        time.sleep(3)
        driver.save_screenshot("newwindows3.png")

        driver.quit()




ff = usingWrappers()
ff.testWrappers()