from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Edge(service=Service('C:\Drivers\msedgedriver.exe'))

driver.get('https://demo.guru99.com/test/newtours/index.php')

#applies to all the elements
driver.implicitly_wait(10)

assert 'Welcome: Mercury Tours' in driver.title
driver.find_element('name', 'userName').send_keys('mercury')
driver.find_element('name', 'password').send_keys('mercury')
driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a').click()

driver.close()