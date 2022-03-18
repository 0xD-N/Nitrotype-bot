import os
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchWindowException, InvalidCookieDomainException
from selenium.webdriver.common.by import By

#Selenium Driver. If you want to use chrome (or any browser): 

# download the chrome binary for your specific chrome version
# Move it to a path that is less likely to have issues (preferably in C:\Program Files (x86))
# change import above to (from selenium.webdriver.chrome.options)

#and lastly change the binary path in Automation class

class Automation():
    
    __BINARY_PATH = r"C:\Program Files (x86)\chromeDriver\chromedriver_win32\chromedriver.exe"
    
    def __init__(self):
        
        #C:\Users\david\AppData\Local\Google\Chrome\User Data
        self.__options = webdriver.ChromeOptions()
        
        self.__options.add_argument(f"--user-data-dir=C:\\Users\\david\\AppData\\Local\\Google\\Chrome\\User Data")
        self.__options.add_argument("--disable-blink-features=AutomationControlled")
        self.__options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
        self.__options.add_experimental_option('useAutomationExtension', False)
        self.__driver = webdriver.Chrome(executable_path=self.__BINARY_PATH, options=self.__options)
        
        
        self.getDriver().get("https://www.google.com/search?q=nitrotype&sxsrf=APq-WBuYHaiAIQhnlbDKSn6zjGb_y9WczA%3A1647310145562&source=hp&ei=QfUvYvDIH-i6qtsPi4u98AU&iflsig=AHkkrS4AAAAAYjADUeFui_25c3Srqnl_wt5fl8IydvkX&ved=0ahUKEwiw7bvAhMf2AhVonWoFHYtFD14Q4dUDCAg&uact=5&oq=nitrotype&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBQgAEIAEMgcIABCABBAKMgcIABCABBAKMgcIABCABBAKMgUIABCABDIHCAAQgAQQCjoECCMQJzoOCC4QgAQQsQMQxwEQ0QM6CwgAEIAEELEDEIMBOg4ILhCABBCxAxCDARDUAjoICAAQsQMQgwE6CwguEIAEELEDENQCOg4ILhCABBCxAxDHARCjAjoICAAQgAQQsQM6EQguEIAEELEDEMcBENEDENQCUABYiglg3ApoAHAAeACAAYsBiAGoBpIBAzUuNJgBAKABAQ&sclient=gws-wiz")
        os.system("cls")
        
    
    def getDriver(self):
        return self.__driver
        
    
        
    
class UrlHasChanged:
    
    def __init__(self, old_url):
        self.old_url = old_url

    def __call__(self, driver):
        return driver.current_url != self.old_url
    

class CountdownStarted:
      
    def __call__(self, driver: WebDriver):
        return len(driver.find_elements(By.XPATH, "//*//div[@class=\"dash-center\"]//following-sibling::*")) > 1

# the difference between this and UrlHasChanges is this method determins whether the page has been refreshed or changed. Used for the end of each race
class pageHasChanged:
    
    def __init__(self, old_url):
        self.old_url = old_url
    
    def __call__(self, driver: WebDriver):
        
        return driver.current_url != self.old_url or len(driver.find_elements(By.XPATH, "//*//div[@class =\"raceResults raceResults--default\"]")) == 0
    