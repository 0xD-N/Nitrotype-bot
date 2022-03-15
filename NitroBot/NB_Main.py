import time
import os
from selenium.webdriver.opera.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException, NoSuchWindowException
from selenium.common.exceptions import StaleElementReferenceException
from NitroBot.Automation.Automation import Automation, UrlHasChanged
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def start():
    
    A = Automation()
    
    run = True
    
   
    while run:
        
        count = 0
        while (A.getDriver().current_url != "https://www.nitrotype.com/race"):
    
            try:
                
                WebDriverWait(A.getDriver(), 1).until(UrlHasChanged(A.getDriver().current_url))
                
            except TimeoutException:
                
                if count >= 300:
                    os.system("cls")
                    print("Nitrotype wasn't in race mode for 5 minutes. Quitting..")
                    return
                else:
                    print(count)
                    count += 1
        
        print("all is good")
           
        
        