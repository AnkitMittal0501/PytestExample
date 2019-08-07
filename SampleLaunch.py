from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://www.shopclues.com")
driver.maximize_window()
driver.refresh()
exwait=WebDriverWait(driver,60)
l=driver.find_elements_by_xpath("//div[@class='moe-button-wrapper']/button")
print("length is ",len(l))
try:
    exwait.until(EC.visibility_of(l[0]))
    l[0].click()
except Exception:
    print("No element")
act=ActionChains(driver)
ele=driver.find_elements_by_xpath("//div[contains(@class,'nav-down')]//ul//li")
act.move_to_element(ele[0]).perform()
print(len(ele))
original =driver.current_window_handle

exwait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'nav-down')]//ul//li[1]//ul//li")))
driver.find_element_by_xpath("//div[contains(@class,'nav-down')]//ul//li[1]//ul//li[2]/a").click()
windows=driver.window_handles
for window in windows:
    if original!= window:
        driver.switch_to.window(window)
        exwait.until(EC.presence_of_element_located((By.XPATH,"//div[@id='product_list']//div[3]//a[2]")))
        originalanother=driver.current_window_handle
        driver.find_element(By.XPATH,"//div[@id='product_list']//div[3]//a[2]").click()
        windowAnother=driver.window_handles
        secondWindow=windowAnother[1]
        for window in windowAnother:
            if window != originalanother and window!= original:
                driver.switch_to.window(window)
                #print(driver.title)
                title=driver.title
                print(title)
ele = driver.find_elements(By.XPATH, "//div[@class='f_variation']/ul/li/span[2]")
act.move_to_element(ele[0]).click(ele[0]).perform()
