from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com//")

driver.find_element(By.ID, "email").send_keys("7038222100")

driver.find_element(By.ID, "pass").send_keys("Pass@1234")

driver.find_element(By.NAME, 'login').click()

print("Login successful")

driver.quit()
