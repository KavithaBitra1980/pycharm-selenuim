#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

class GetAttribute_expedia:
    def testAttribute(self):
        baseUrl = "https://www.expedia.com/"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        title = driver.title
        print('the title is',title)

        getelement = driver.find_element(By.ID,"package-destination-hp-package")
        result = getelement.get_attribute("class")
        print('the attribute value is:clear-btn-input gcw-storeable text gcw-destination gcw-required gcw-distinct-locations', result)
        time.sleep(3)

        getelement1 = driver.find_element(By.ID, "tab-flight-tab-hp")
        result1 = getelement1.get_attribute("data-lob")
        print('the attribute value1 is:flight', result1)
        time.sleep(3)

        getelement2 = driver.find_element(By.ID, "package-advanced-preferred-class-hp-package")
        result2 = getelement2.get_attribute("class")
        print('the attribute value2 is', result2)
        time.sleep(3)



        driver.quit()

ff = GetAttribute_expedia()
ff.testAttribute()



