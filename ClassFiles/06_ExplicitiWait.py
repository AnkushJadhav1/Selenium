from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

driver.find_element(By.XPATH, '//*[@id="start"]/button').click()

element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="loading"]')))
print(element.get_attribute('innerHTML'))

element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="finish"]/h4')))
print(element.get_attribute('innerHTML'))


# ---------------------------  Other Way not working  --------------
#
# new_element = WebDriverWait(driver, 10, ignored_exceptions=[Exception])
#
# element = new_element.until(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="loading"]')))
# print(element.get_attribute('innerHTML'))
#
# element = new_element.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="finish"]/h4')))
# print(element.get_attribute('innerHTML'))

driver.quit()