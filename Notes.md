# Notes

Documentation of instructions and solutions to issues I have faced whilst practicing Selenium with Python.

## Web Drivers

### Downloading Web Drivers

- Go to the [Python Package Index](https://pypi.org/project/selenium/) website to download the latest web driver for your chosen web browser.
- For this project I will be using FireFox and Edge, so I have downloaded the relevant web drivers and stored them in the Drivers directory.

### Issues

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

