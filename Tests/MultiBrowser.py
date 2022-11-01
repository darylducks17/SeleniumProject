from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service

#driver = webdriver.Edge(executable_path='C:\Drivers\msedgedriver.exe')
driver = webdriver.Firefox(service=Service('C:\Drivers\geckodriver.exe'))

driver.get('http://demo.guru99.com/test/newtours/')

#returns HTMl code of the page
print(driver.page_source)
#prints the url of the page
print(driver.current_url)
#prints title of the page 
print(driver.title)

#close the browser one at a time 
driver.close()

#closes all the open browsers
driver.quit()