from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Edge(service=Service('C:\Drivers\msedgedriver.exe'))

driver.get('https://demo.guru99.com/test/newtours/')

username = driver.find_element('name', 'userName')
password = driver.find_element(By.NAME,'password')

#returns true/false based on username element status
print(username.is_displayed())
print(username.is_enabled())

#returns true/false based on the status of password element
print(password.is_displayed())
print(password.is_enabled())

#username.send_keys('mercury')
#password.send_keys('mercury')
#driver.find_element('name', 'submit').click()
driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a').click()

round_trip = driver.find_element(By.CSS_SELECTOR,'input[value="roundtrip"]')
#print status of roundtrip radio button
print("Status of round trip radio button:", round_trip.is_selected())

one_way = driver.find_element(By.CSS_SELECTOR, 'input[value="oneway"]')
#prints status of one way trip radio button
print("Status of one way radio button:", one_way.is_selected())

driver.close()