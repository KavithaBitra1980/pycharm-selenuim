#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import  *
from wait_types.explicit_wait_type import ExplicitWaitType

class ExplicitwaitType_Demo():
    def test_emplicit_wait_Type_demo(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://www.expedia.com/"
        driver.implicitly_wait(10)
        wait = ExplicitWaitType(driver)
        driver.get(baseURL)
        title = driver.title
        print(title)

        driver.find_element(By.ID,"tab-flight-tab-hp").click()
        driver.find_element(By.ID,"flight-type-roundtrip-label-hp-flight").click()
        driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")
        time.sleep(3)
        driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("LAX")
        time.sleep(3)
        driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("11/28/2018")
        rd = driver.find_element(By.ID,"flight-returning-hp-flight")
        rd.clear()
        rd.send_keys("12/12/2018")
        driver.find_element(By.CSS_SELECTOR,".btn-primary.btn-action.gcw-submit").click()
        time.sleep(3)

        #driver.find_element(By.ID,"stopFilter_stops-0").click()

        element = wait.waitForElement("stopFilter_stops-0")
        #print(type(element))
        element.click()


        driver.close()


ff = ExplicitwaitType_Demo()
ff.test_emplicit_wait_Type_demo()