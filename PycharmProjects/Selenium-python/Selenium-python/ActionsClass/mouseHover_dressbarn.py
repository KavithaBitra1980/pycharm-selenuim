#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'
#DEMO of Mouse Hover

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
class mouseHover_DressBarn():
    def test_mouseHover_Dressbarn(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://www.abercrombie.com/shop/us"
        driver.implicitly_wait(15)
        driver.get(baseURL)
        title = driver.title
        print(title)

        womens = driver.find_element(By.XPATH,"//li[@id='cat-12203-largescreen']//a[contains(@class,'rs-nav__cat-label rs-hide-xs rs-hide-sm')]")
        time.sleep(3)
        try:
            action = ActionChains(driver)
            action.move_to_element(womens).perform()
            newArrivals = driver.find_element(By.XPATH,"//*[@id='cat-12252-largescreen']/a[contains(@class,'rs-nav-link--minor')]")
            newArrivals.click()
            #action.move_to_element(newArrivals).click().perform()
            time.sleep(5)
            newtitle = driver.title
            print(newtitle)
            driver.save_screenshot("aberNew.png")
            print("Actions performed")
        except:
            print("Action cant performed")


mm = mouseHover_DressBarn()
mm.test_mouseHover_Dressbarn()

