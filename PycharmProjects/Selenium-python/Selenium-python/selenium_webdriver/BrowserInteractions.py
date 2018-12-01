#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'
#Demo of Browwser Interactions'

from selenium import webdriver

class BrowserInteractions():
    def testBrowser(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        title = driver.title
        print('the title is',title)
        driver.refresh()
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        current_URL = driver.current_url
        print('the current URL is',current_URL)
        driver.back()
        current_URL1 = driver.current_url
        print('the current URl is',current_URL1)
        driver.forward()
        current_URL2 = driver.current_url
        print('the current URl is', current_URL2)
        driver.back()
        page_sources = driver.page_source
        print('the page source is',page_sources)

        driver.quit()

ff = BrowserInteractions()
ff.testBrowser()

