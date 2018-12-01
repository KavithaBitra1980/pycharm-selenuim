#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class calendar_Selection():

    def test1_calendar_selection(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://www.expedia.com/"
        driver.implicitly_wait(15)
        driver.get(baseURL)
        title = driver.title
        print(title)

        driver.find_element(By.ID,"tab-flight-tab-hp").click()
        time.sleep(3)
        driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")
        wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                 ElementNotSelectableException])
        destTo = wait.until(EC.element_to_be_clickable((By.ID,"flight-destination-hp-flight")))
        destTo.send_keys("LAX")
        time.sleep(3)
        driver.find_element(By.ID,"flight-departing-hp-flight").click()
        time.sleep(3)
        date_selectFrom = driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=1]//button[contains(@class,'datepicker-cal-date') and contains(text(),'30')]")
        date_selectFrom.click()
        time.sleep(3)

        driver.find_element(By.ID,"flight-returning-hp-flight").click()
        dateSelectTo = driver.find_element(By.XPATH,"//div[@class='datepicker-cal-month'][position()=2]//button[contains(@class,'datepicker-cal-date') and contains(text(),'31')]")
        dateSelectTo.click()
        time.sleep(3)


        driver.find_element(By.CSS_SELECTOR,".btn-primary.btn-action.gcw-submit").click()
        selectElement = wait.until(EC.element_to_be_clickable((By.ID,"airlineRowContainer_UA")))
        selectElement.click()
        driver.close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
    def test2_calenderSelevtionIf(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://www.expedia.com/"
        driver.implicitly_wait(15)
        driver.get(baseURL)
        title = driver.title
        print(title)

        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("LAX")

        driver.find_element(By.ID, "flight-departing-hp-flight").click()
        time.sleep(3)
        cal_month = driver.find_elements(By.XPATH,"//div[@class='datepicker-cal-month'][position()=1]//button[not (contains(@class,'datepicker-cal-date disabled'))]")

        for date in cal_month:
            print(date.text)
            if "30" in date.text:
                date.click()
                break
        time.sleep(3)


        driver.find_element(By.ID, "flight-returning-hp-flight").click()
        time.sleep(3)
        cal_month2 = driver.find_elements(By.XPATH,"//div[@class='datepicker-cal-month'][position()=2]//button[not (contains(@class,'datepicker-cal-date disabled'))]")

        for date2 in cal_month2:
            print(date2.text)
            if "15" in date2.text :
                date2.click()
                break


        time.sleep(3)

        driver.close()
"""

ff = calendar_Selection()
ff.test1_calendar_selection()
#ff.test2_calenderSelevtionIf()


