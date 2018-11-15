#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo of List of elements

from selenium import webdriver
from selenium.webdriver.common.by import By

class listOfElements():
    def list(self):
        driver = webdriver.Firefox(executable_path="C:\\firefoxdriver\\geckodriver.exe")
        baseUrl = baseUrl = "https://learn.letskodeit.com/p/practice"
        driver.get(baseUrl)

        elementslistByClassName = driver.find_elements_by_class_name("btn-style")
        length1 = len(elementslistByClassName)

        print(length1)
        if elementslistByClassName is not None:
            print('elements found')
        else:
            print('element not found')

        elementslistByTagName = driver.find_elements(By.TAG_NAME,"td")
        length2 = len(elementslistByTagName)

        print(length2)
        if elementslistByTagName is not None:
            print('tag elements found')
        else:
            print('tag element not found')


ff = listOfElements()
ff.list()


