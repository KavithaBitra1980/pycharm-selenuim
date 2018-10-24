#Import selenium webdriver

from selenium import webdriver as wd
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
driver = wd.Firefox(executable_path='C:\Program Files\geckodriver\geckodriver.exe')
driver.get('http://www.google.com')