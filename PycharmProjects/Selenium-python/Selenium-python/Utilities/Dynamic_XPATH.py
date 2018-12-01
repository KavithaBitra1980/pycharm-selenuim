#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

# Demo for Building Dynamic Xpath

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Dynamic_xpath():
    def test_dynamicxpath(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://letskodeit.teachable.com"
        driver.implicitly_wait(10)
        driver.get(baseURL)
        title = driver.title
        print(title)

        driver.find_element(By.LINK_TEXT, "Login").click()

        useremail1 = driver.find_element(By.ID,"user_email")
        useremail1.send_keys("test@email.com")
        password = driver.find_element(By.ID,"user_password")
        password.send_keys("abcabc")
        commitbtn = driver.find_element(By.NAME,"commit")
        commitbtn.click()
        driver.save_screenshot("dynamicxpathscreen1.png")
        time.sleep(4)

        driver.find_element(By.LINK_TEXT,"All Courses").click()

        search = driver.find_element(By.ID,"search-courses")
        search.send_keys("JavaScript")
        time.sleep(3)

        course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        courseLocator = course.format("JavaScript for beginners")
        courseElemet = driver.find_element(By.XPATH,courseLocator)
        courseElemet.click()
        driver.save_screenshot("dynamixpath2.png")
        time.sleep(3)


        driver.find_element(By.LINK_TEXT, "All Courses").click()
        time.sleep(3)
        course2 = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        course2Locator = course2.format('Learn Python 3 from scratch')
        course2Element = driver.find_element(By.XPATH,course2Locator)
        course2Element.click()
        time.sleep(3)
        driver.close()

ff = Dynamic_xpath()
ff.test_dynamicxpath()