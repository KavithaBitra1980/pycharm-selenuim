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

class Emplicitwait():
    def test_emplicit_wait(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://www.expedia.com/"
        driver.implicitly_wait(10)
        driver.get(baseURL)
        title = driver.title
        print(title)

        driver.find_element(By.ID,"tab-flight-tab-hp").click()
        driver.find_element(By.ID,"flight-type-roundtrip-label-hp-flight").click()
        driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")
        time.sleep(3)
        driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("LAX")
        time.sleep(3)
        driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("11/30/2018")
        rd = driver.find_element(By.ID,"flight-returning-hp-flight")

        rd.clear()
        time.sleep(5)
        rd.clear()
        rd.send_keys("12/12/2018")
        driver.find_element(By.CSS_SELECTOR,".btn-primary.btn-action.gcw-submit").click()
        driver.save_screenshot("search_expedia1.png")

        #driver.find_element(By.ID,"stopFilter_stops-0").click()

        wait = WebDriverWait(driver,10,poll_frequency=1,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID,"stopFilter_stops-0")))
        element.click()
        driver.close()


ff = Emplicitwait()
ff.test_emplicit_wait()