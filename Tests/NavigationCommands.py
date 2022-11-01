from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
import time 

driver = webdriver.Edge(service=Service('C:\Drivers\msedgedriver.exe'))

driver.get('http://demo.guru99.com/test/newtours/')
print(driver.title)

driver.get('https://www.pavantestingtools.com/')
print(driver.title)

#goes back to the previous page  
driver.back()
print(driver.title)

#goes to the following page
driver.forward()
print(driver.title)

#closes the browser
driver.close()
