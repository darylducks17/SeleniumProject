# Notes

Documentation of instructions, notes and solutions to issues I have faced whilst practicing Selenium with Python.

## Downloading Web Drivers

- Go to the [Python Package Index](https://pypi.org/project/selenium/) website to download the latest web driver for your chosen web browser.
- For this project I will be using FireFox and Edge, so I have downloaded the relevant web drivers and stored them in the Drivers directory.

## Selenium Waits

- When a page loads in the browser the elements which we want to interact with may load at different time intervals and if the element is not located it will throw an error. 

    ###### Implicit Wait
    - This is used to tell the web driver to wait for a certain amount of time before it throws an error. 

    ###### Explicit Wait
    - This is used to tell the web driver to wait for certain conditions or maximum time exceeded before throwing errors. 
    - Gives better options than implicit wait as it waits for dynamically loaded elements as well. 

## Issues

- If Selenium throws an error whilst the tests are running about executable_path being deprecated, just follow this [tutorial](https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python).
    ###### TL;DR
    - Ensure that Webdriver Manager for Python is installed in CMD: `pip install webdriver-manager` 
    - Found that importing the web driver service fixes the issue. 
    ```
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.firefox.service import Service
        driver =  webdriver.<BROWSER>(service=Service('C:\Drivers\<WEBDRIVER>.exe')) 
    ``` 

- Selenium might throw an error saying that the WebDriver object has no attribute 'find_element_by_<...>. Follow this [page](https://stackoverflow.com/questions/72773206/selenium-python-attributeerror-webdriver-object-has-no-attribute-find-el) and you'll find the answer. 
    ###### TL;DR
    - Selenium 4.3.0 has removed the method, so either use
        `driver.find_element('name', 'q')` --> to find elements by name 
        
        or use the following if you want to find 
        ```
        from selenium.webdriver.common.by import By
        driver.find_element/s(By.<CLASS_NAME, XPATH, LINK_TEXT, ID, CSS_SELECTOR, NAME, PARTIAL_LINK_TEXT, TAG_NAME>, 'q')
        ```