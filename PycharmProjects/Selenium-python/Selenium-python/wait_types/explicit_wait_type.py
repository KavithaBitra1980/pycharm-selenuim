#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

from traceback import print_stack
from Utilities.handyWrappers import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import  *

class ExplicitWaitType():
    def __init__(self,driver):
        self.driver = driver
        self.hw = HandyWrappers(driver)

    def waitForElement(self,locator,locatorType='id',timeout=10,pollFrequency=0.5):
        element = None
        try:
            byType = self.hw.getByType(locatorType)
            print("Waiting for maximum ::" + str(timeout) + " :: seconds for elemnt to be clickable")
            wait = WebDriverWait(self.driver,timeout=timeout,poll_frequency=pollFrequency,ignored_exceptions=[ElementNotSelectableException,
                                                                                                              NoSuchElementException,
                                                                                                              ElementNotVisibleException])
            element =wait.until(EC.element_to_be_clickable((byType,locator)))
            print("Element appeared on the web page")
        except:
            print("element not appeared on the web page")
            #print_stack()
        return element