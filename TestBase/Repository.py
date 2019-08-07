from pytestExample.TestBase import TestBase
from selenium.webdriver.common.by import By
class Repo(TestBase.DriverLaunch):
    @staticmethod
    def colorSelection(driver):
        ele=driver.find_element(By.XPATH,"//div[@class='f_variation']/ul/li/span[2]")
        return ele
