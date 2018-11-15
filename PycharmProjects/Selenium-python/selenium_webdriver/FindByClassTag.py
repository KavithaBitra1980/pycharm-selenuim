#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo of finding elements by CSS and XPATH

from selenium import webdriver

class findByClassTag():
    def elementsByClassTag(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(executable_path="C:\\firefoxdriver\\geckodriver.exe")
        driver.get(baseUrl)
        try :
            elementByClass = driver.find_element_by_class_name("inputs")
            elementByClass.send_keys("This is kavitha")
            elementByClass.screenshot("inputs_sh1.png")
            if elementByClass is not None:
                print("the element found by ClassName")

            elementByTag = driver.find_element_by_tag_name("a")
            elementByTag.send_keys("Sending key to test tag")
            elementByTag.screenshot("tag_SH1.png")
            if elementByTag is not None:
                print("the element found by TagName")

        except :
            print("Error not found element")
            raise Exception('raise an exception')
        finally :
            print("the code got executed")

ff = findByClassTag()
ff.elementsByClassTag()
