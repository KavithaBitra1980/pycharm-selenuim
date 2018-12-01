#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'
#DEMO of Mouse Hover

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
class mouseHover():
    def test_mouseHover(self):
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver.implicitly_wait(15)
        driver.get(baseURL)
        title = driver.title
        print(title)

        driver.execute_script("window.scrollBy(0,600);")
        element = driver.find_element(By.ID,"mousehover")
        time.sleep(3)
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            time.sleep(3)
            #driver.find_element(By.XPATH,"//div[@class='mouse-hover-content']//a[text()='Top']").click()
            elementReload = driver.find_element(By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Reload']")
            actions.move_to_element(elementReload).click().perform()
            time.sleep(3)
            driver.find_element(By.LINK_TEXT,'Sign Up').click()
            time.sleep(3)
            print('Element Found')
        except:
            print('Element not Found')




mm = mouseHover()
mm.test_mouseHover()

