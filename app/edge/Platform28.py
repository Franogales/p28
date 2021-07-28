# from selenium import webdriver
# import os
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class Platform28:
    driver = None
    def __init__(self) -> None:
        self.setDriver()
        if self.isLogged() == True:
            if self.IsUnavailable():
                self.SetStatusAvailable()
            else:
                print("tiene otro estado que no es unavailable")
            if self.IsAvailable():
                print("si esta disponible")
            else:
                print("otro estado diferente a disponible")

        else:
            print("no esta logeado")
        pass

    def isLogged(self) -> bool :      
        # self.driver.get("https://apps.platform28.com/agent-desktop")

        script = 'return window.frames[0].document.querySelector("body > app-root > app-login > div > div.title.ng-star-inserted").innerText;'
        if self.detectElement(script,"Sign in to your account"):
            return False
        return True
        

    def setDriver(self):
        options = EdgeOptions()
        options.use_chromium = True
        options.add_experimental_option("debuggerAddress","localhost:8989")
        self.driver = Edge(executable_path=r"C:\tmpdata\edge\msedgedriver.exe", options = options)
    
    def IsUnavailable(self) ->bool:
        script = 'return document.querySelector("body > app-root > div > div.second-line > embedded-phone > mat-sidenav-container > mat-sidenav-content > div > ready-state-panel > div > div > div").innerText;'
        if self.detectElement(script,"Not Ready: Logged In"):
            return True
        return False

    def IsAvailable(self) ->bool:
        script = 'return document.querySelector("body > app-root > div > div.second-line > embedded-phone > mat-sidenav-container > mat-sidenav-content > div > ready-state-panel > div > div > div").innerText;'
        if self.detectElement(script,"Ready in Queues"):
            return True
        return False
    
    def clickStatus(self):
        element = '''
        var callback = arguments[arguments.length - 1];
        document.querySelector("body > app-root > div > div.second-line > embedded-phone > mat-sidenav-container > mat-sidenav-content > div > ready-state-panel > div > div > div").click();
        
        setTimeout(function(){
        callback("undefined");
        }, 2000);
        '''
        clicked = self.driver.execute_async_script(element)
        assert clicked=='undefined'
    
    def click(self,element):
        script = element+'.click()'
        self.driver.execute_script(script)
        print(element)

    def SetStatusAvailable(self):
        self.clickStatus()
        element = '''
        var callback = arguments[arguments.length - 1];
        document.querySelector("#cdk-overlay-0 > div > div > agent-state-dropdown > div > button:nth-child(2) > span").click()
        
        setTimeout(function(){
        callback("click");
        }, 2000);
        '''
        clicked = self.driver.execute_async_script(element)
        assert clicked=='click'

    def detectElement(self, script, spected)->bool:
        attempts = 0
        found = False
        while attempts <=5 and found == False:
            print(attempts)
            try:
                text = self.driver.execute_script(script=script)
                if text == spected:
                    found =True
                    return found
                attempts = attempts+1
                time.sleep(1)
            except Exception:
                attempts = attempts+1
                time.sleep(1)
                pass
        return False
