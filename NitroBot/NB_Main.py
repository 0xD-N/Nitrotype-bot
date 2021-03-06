import time
import os
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException, NoSuchWindowException
from selenium.common.exceptions import StaleElementReferenceException
from NitroBot.Automation.Automation import Automation, CountdownStarted, UrlHasChanged, pageHasChanged
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
    

def start():
    
    A = Automation()
    
    run = True

    gameIsOver = False
    
    performType = True
    
    try:
        while run:
            
            while (A.getDriver().current_url != "https://www.nitrotype.com/race"):
        
                try:
                    
                    WebDriverWait(A.getDriver(), 300).until(UrlHasChanged(A.getDriver().current_url))
                    
                except TimeoutException:
            
                        os.system("cls")
                        print("Nitrotype wasn't in race mode for 5 minutes. Quitting..")
                        return
            
           
            #if the game is over wait until the page is refreshed or changed to continue (up to 5 minutes)
            if gameIsOver:
                
                #waits until the page is refreshed or the page is redirected elsewhere
                time.sleep(4)
                WebDriverWait(A.getDriver(), 300).until(pageHasChanged(A.getDriver().current_url))

                gameIsOver = False
                performType = True
                continue
            else:
                #wait until countdown starts
                WebDriverWait(A.getDriver(), 60).until(CountdownStarted())
                
                #wait 3 seconds before typing
                time.sleep(3)
                
                
                #input for typing
                inputBox: WebElement = (WebDriverWait(A.getDriver(), 10).until(lambda d: d.find_element(By.XPATH, "//input")))

                fullText = "".join((WebDriverWait(A.getDriver(), 10).until(lambda d: d.find_element(By.XPATH, "//*//div[@class=\"dash-copy\"]"))).text.split("\n"))
                
                with open("test.txt", "w") as f:
                    
                    for word in fullText:
                        f.write(word)
                if performType:
                    print("beginning to type")
                while performType:
                    
                    # inputBox: WebElement = (WebDriverWait(A.getDriver(), 10).until(lambda d: d.find_elements(By.XPATH, "//input")))
                    letter = A.getDriver().find_elements(By.XPATH, "//*//div[@class=\"dash-copy\"]//*[contains(@class, \"is-waiting\")]")
                    
                    if(len(letter) == 0):
                        performType = False
                        gameIsOver = True
                    else:
                        
                        inputBox.send_keys(Keys.SPACE if letter[0].text == "&nbsp;" else letter[0].text)
                        
                        #time.sleep(0.000000015)

                if not performType:
                    print("Not typing")
                    
    except TimeoutException as e:
        print(f"\nLine {e.__traceback__.tb_lineno}: {e}")
        A.getDriver().quit()
            #//*//div[@class="dash-copy"]
            #//*//div[@class="dash-center"]//following-sibling::* (use to determine if the game has started countdown)
           
        
        