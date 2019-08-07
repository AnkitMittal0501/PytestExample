from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DriverLaunch:
    def __init__(self):
        self.driver =webdriver.Chrome(executable_path="chromedriver.exe")

    def driverInitiate(self,url=None):
        if url!=None:
            self.driver.get(url)
        return self.driver
    def eventHandling(self):
        act=ActionChains(self.driver)
        return act
    def explicitWait(self):
        wait=WebDriverWait(self.driver,20)
