from selenium import webdriver

driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
driver.set_page_load_timeout(20)
driver.get("http://newtours.demoaut.com")
print(driver.title)
driver.save_screenshot("C:\Selenium-python\home.png")
driver.maximize_window()
driver.implicitly_wait(10)
driver.close()
driver.quit()