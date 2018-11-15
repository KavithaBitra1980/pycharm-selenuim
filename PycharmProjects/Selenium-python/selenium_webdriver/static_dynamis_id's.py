#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Dynamic and Static Id's Demonstration

from selenium import webdriver

class staticDynamicId():
    def sdIdTest(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path="C:\\firefoxdriver\\geckodriver.exe")
        driver.get(baseUrl)
        elementbyId = driver.find_element_by_id("name")

        if elementbyId is not None :
            print("the name found")

        driver.get("https://www.yahoo.com/")
        elementbyId2 = driver.find_element_by_id("yui_3_18_0_3_1541290176650_103")

        if elementbyId2 is not None :
            print("the element of yahoo found")


sd = staticDynamicId()
sd.sdIdTest()



