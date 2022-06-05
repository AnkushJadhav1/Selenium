import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.naukri.com/nlogin/login?URL=https://www.naukri.com/browse-jobs")

userid = driver.find_element(By.ID, 'usernameField')
userid.send_keys("jadhavankush.official@gmail.com")
print(f"Userid is Enable : {userid.is_enabled()}")

pwd = driver.find_element(By.ID, 'passwordField')
pwd.send_keys('Pass@1234')
print(f"Password is Enable : {pwd.is_enabled()}")

driver.find_element(By.XPATH,
                    '/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div/form/div[2]/div[3]/div/button[1]').click()
time.sleep(5)

driver.find_element(By.XPATH,
                    '/html/body/div[1]/div/ul[2]/li[2]/a/div[2]').click()
time.sleep(5)
print("Login Functionality Pass")

#driver.quit()
# -----------------------------------------------------------------------------------------------------------------------







