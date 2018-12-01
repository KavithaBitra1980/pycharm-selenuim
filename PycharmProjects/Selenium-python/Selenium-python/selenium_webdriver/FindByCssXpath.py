#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo of finding elements by CSS and XPATH

from selenium import webdriver

class findByCssXpath():
    def elementsBycssXpath(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(executable_path="C:\\firefoxdriver\\geckodriver.exe")
        driver.get(baseUrl)
        try :
            elementByCSS = driver.find_element_by_css_selector("#displayed-text")
            if elementByCSS is not None:
                print("the element found by CSS")

            elementByXpath = driver.find_element_by_xpath("//input[@id='name']")
            if elementByXpath is not None:
                print("the element found by xpath")

        except :
            print("Error not found element")
            raise Exception('raise an exception')
        finally :
            print("the code got executed")

ff = findByCssXpath()
ff.elementsBycssXpath()