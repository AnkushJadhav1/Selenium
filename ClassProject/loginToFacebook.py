from selenium import webdriver
from selenium.webdriver.common.by import By


# download webdriver online and then save in python location
driver = webdriver.Chrome()

driver.get("https:/www.facebook.com/")

# enter the id value using inspect and find id/name value.
driver.find_element(By.ID, "email").send_keys("abc@gmail.com")

driver.find_element(By.ID, "pass").send_keys("Pass@123")

driver.find_element(By.LINK_TEXT, "Log In").click()   # link_text means inner HTML

