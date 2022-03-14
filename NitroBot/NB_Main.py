import time
import os
from selenium.webdriver.opera.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from NitroBot.Automation.Automation import Automation, UrlHasChanged
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def start():
    
    A = Automation().getDriver()
    
    run = True
    
    while run:
        
        if(A.current_url != "https://www.youtube.com/"):
            
            while A.current_url != "https://www.youtube.com/":
                
                try:
                    WebDriverWait(A, 60*5).until(UrlHasChanged(A.current_url))
                except TimeoutException:
                    os.system("cls")
                    print("Failed to connect to youtube")
                    A.quit()
            
        else:
            
           print("All is good")
        