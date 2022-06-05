import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.amazon.in/')

driver.maximize_window()

# input_Fill = driver.find_element(By.ID, 'twotabsearchtextbox')
# print(f"This Input Tab is enabled : {input_Fill.is_enabled()}")
#
# signup = driver.find_element(By.CSS_SELECTOR, '#nav-signin-tooltip > a > span')
# print(f"Is there signup tab is enable : {signup.is_enabled()}")
#
# signup = driver.find_element(By.CSS_SELECTOR, '#nav-signin-tooltip > a > span')
# print(f"Is there signup tab is displayed : {signup.is_displayed()}")



#driver.quit()

time.sleep(5)

driver.find_element(By.CSS_SELECTOR, '#nav-signin-tooltip > a > span').click()

driver.find_element(By.ID, "ap_email").send_keys("7038222100")

driver.find_element(By.ID, "ap_password").send_keys("Pass@1234")

driver.find_element(By.ID, 'continue').click()





