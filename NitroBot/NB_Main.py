import time
import os
from selenium.webdriver.opera.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException, NoSuchWindowException
from selenium.common.exceptions import StaleElementReferenceException
from NitroBot.Automation.Automation import Automation, CountdownStarted, UrlHasChanged
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
                    count += 1
        
        WebDriverWait(A.getDriver(), 10).until(CountdownStarted())
        run = True
        
        with open("test.txt", "w") as f:
            
            while run:
                
                letter = A.getDriver().find_elements(By.XPATH, "//*//div[@class=\"dash-copy\"]//*[contains(@class, \"is-waiting\")]")
                
                if(len(letter) == 0):
                    run = False
                else:
                    f.write(letter[0].text + "\n")
                
        #//*//div[@class="dash-copy"]
        #//*//div[@class="dash-center"]//following-sibling::* (use to determine if the game has started countdown)
        #print("all is good")
           
        
        