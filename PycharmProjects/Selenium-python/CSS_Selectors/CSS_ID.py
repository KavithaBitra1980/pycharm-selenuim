#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#DEMO of CSS _Selector

from selenium import  webdriver

class css_select():
    def demoCSS(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver.get(baseURL)

        elementByCssID = driver.find_element_by_css_selector("#displayed-text")

        if elementByCssID is not None:
            print("element found")

        elementByCssClass = driver.find_element_by_css_selector(".displayed-class")

        if elementByCssClass is not None:
            print("Class element found")

        elementByCssMulti_Class = driver.find_element_by_css_selector(".btn-style.class1.class2")

        if elementByCssMulti_Class is not None:
            print("Multi-Class2 element found")

        elementByCssMulti_Class_Wild = driver.find_element_by_css_selector("input[class*='block']")

        if elementByCssMulti_Class_Wild is not None:
            print("Multi-Class-wild element found")


        driver.save_screenshot("multi_button3.png")


ff = css_select()
ff.demoCSS()

