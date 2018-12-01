#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'


from selenium import webdriver
class FindByIdName():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        #driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Firefox(executable_path="C:\\firefoxdriver\\geckodriver.exe")
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")
        elementByName = driver.find_element_by_name("show-hide")
        elementById2 = driver.find_element_by_id("multiple-select-example")
        elementByName2 = driver.find_element_by_name("multiple-select-example")


        if elementById is not None :
            print("We found Element by Id")

        if elementByName != None :
            print("we found Element by Name")



        if elementById2 != None:
                print("We found Element by Id2")
        else:
                print("id2 not found")

        if elementByName2 != None:
                print("we found Element by Name2")
        else:
                print("name2 not found")



ff =  FindByIdName()
ff.test()

"""
We found Element by Id
we found Element by Name
We found Element by Id2
we found Element by Name2

Process finished with exit code 0

"""