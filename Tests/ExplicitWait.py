from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Edge(service=Service('C:\Drivers\msedgedriver.exe'))
#maximising the browser
driver.maximize_window()

driver.get('https://www.lastminute.com/')

#click accept all button
#driver.find_element(By.XPATH, '//*[@id="iubenda-cs-banner"]/div/div/div/div[3]/div[2]/button[2]').click()
#click flights tab
driver.find_element(By.XPATH, '//*[@id="app-header"]/header/nav[2]/div/ul/li[2]/a').click()
#enter departure city/airport 
#driver.find_element(By.XPATH, '//*[@id="hub-csw-container"]/div[2]/div/form/div/div[1]/div/div/div/div/div[2]').click()
#driver.find_element(By.CSS_SELECTOR, 'input[id="mui-3"]').send_keys('NYC')
#enter arrival city/airport 
driver.find_element(By.CSS_SELECTOR, 'input[id="mui-4"]').click()
#click departure date input box
driver.find_element(By.XPATH, '//*[@id="hub-csw-container"]/div[4]/div/form/div[2]/div[2]/div/div/div[1]/button').click()
#click departure date
driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/section/div/div/div[2]/div[2]/button[1]').click()
#click return date
driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/section/div/div/div[2]/div[2]/button[13]').click()
#click close calendar button
driver.find_element(By.XPATH, '/html/body/div[4]/div/footer/div[2]/button').click()
#click find button
driver.find_element(By.XPATH, '//*[@id="hub-csw-container"]/div[4]/div/form/div[2]/div[5]/button').click()

driver.close()