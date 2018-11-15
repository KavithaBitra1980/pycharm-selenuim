#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo of By_class,Name

from selenium import webdriver
from selenium.webdriver.common.by import By

class byClass():
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(executable_path="C:\\firefoxdriver\\geckodriver.exe")
        driver.get(baseUrl)

        elementby_Id = driver.find_element(By.ID,"name")

        if elementby_Id is not None:
            print("we found the element by ID")

        elementby_Xpath = driver.find_element(By.XPATH,"//input[@id='name']")
        if elementby_Xpath is not None:
            print("we found the element by XPATH")


        elementby_LinkText = driver.find_element(By.LINK_TEXT,"Login")
        if elementby_LinkText is not None:
            print("we found the element by LinkText")

        elementby_CSS = driver.find_element(By.CSS_SELECTOR,"#displayed-text")
        if elementby_CSS is not None:
            print("we found the element by CSS_SELECTOR")

        elementby_class = driver.find_element(By.CLASS_NAME,"inputs")
        if elementby_class is not None:
            print("we found the element by CLASS_NAME")

        elementby_tag = driver.find_element(By.TAG_NAME,"legend")
        if elementby_tag is not None:
            print("we found the element by TAG_NAME")

        elementby_partialtag = driver.find_element(By.PARTIAL_LINK_TEXT,"Sign Up")
        if elementby_partialtag is not None:
            print("we found the element by PARTIAL_LINK_TEXT")




cl = byClass()
cl.test()