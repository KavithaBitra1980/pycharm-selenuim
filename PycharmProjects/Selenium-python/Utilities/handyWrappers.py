#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo of Handy wrappers

from selenium.webdriver.common.by import By

class HandyWrappers():

    def __init__(self,driver):
        self.driver = driver

    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return  By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'class_name':
            return By.CLASS_NAME
        elif locatorType == 'tag_name':
            return By.TAG_NAME
        elif locatorType == 'link_text':
            return By.LINK_TEXT
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'partial_link_text':
            return By.PARTIAL_LINK_TEXT
        else:
            print("The Locator Type is not supported")

    def getElement(self,locator,locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            print("Element Found")
        except:
            print("Element Not Found")
        return element

    def isElementPresent(self,locator,byType):
        try:
            element = self.driver.find_element(byType,locator)
            if element is not None:
                print("element Found")
                return True
            else:
                return False
        except:
            print("Element Not Found")
            return False

    def elementCheck(self,locator,byType):
        try:
            elementlist = self.driver.find_elements(byType,locator)
            if len(elementlist) > 0 :
                print('The element Found')
                return True
            else:
                return False
        except:
            print('The Element Not Found')
            return False





