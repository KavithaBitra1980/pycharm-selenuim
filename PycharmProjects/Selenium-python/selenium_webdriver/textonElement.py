#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#DEMO To get TEXT froma n element
from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

class TextElement():
    def testText(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        title = driver.title
        print('the title is',title)

        textElement = driver.find_element(By.ID,"openwindow")
        gettextElement = textElement.text
        print('the element is',gettextElement)
        time.sleep(3)

        textElementRadio = driver.find_element(By.ID,"radio-btn-example")
        gettextElementRadio = textElementRadio.text
        print('the radio button example elements text is',gettextElementRadio)

        textElementSelect= driver.find_element(By.ID, "select-class-example")
        gettextElementSelect = textElementSelect.text
        print('the select class example elements text is', gettextElementSelect)

        textElementTable = driver.find_element(By.ID, "product")
        gettextElementTable= textElementTable.text
        print('the Web Table example elements text is', gettextElementTable)


        driver.close()

ff = TextElement()
ff.testText()