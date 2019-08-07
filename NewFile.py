from pytestExample.TestBase import Repository
from selenium.webdriver.support import expected_conditions as EC

tb=Repository.Repo()
driver=tb.driverInitiate("https://www.shopclues.com/indian-beauty-art-silk-blended-mysore-printed-womens-saree-136717517.html")
act=tb.eventHandling()
driver.maximize_window()
wait=tb.explicitWait()
driver.maximize_window()
#ele = driver.find_elements(By.XPATH,"//div[@class='f_variation']/ul/li/span[2]")
act.move_to_element(Repository.Repo.colorSelection(driver)).click(Repository.Repo.colorSelection(driver)).perform()
# elem=driver.find_elements(By.ID,"buy")
# act.move_to_element(elem[0]).click(elem[0]).perform()
# wait.until(EC.presence_of_element_located((By.ID, "main_user_login")))
#
# driver.find_element(By.ID,"main_user_login").send_keys("ankitkrmittal25@gmail.com")
# driver.find_element(By.NAME,"password").send_keys("Noida@123")
# driver.find_element(By.ID,"login_button").click()
# exwait.until(EC.presence_of_element_located((By.ID,"proceed_to_payment_button")))
# driver.find_element(By.ID,"proceed_to_payment_button").click()
