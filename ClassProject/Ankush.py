import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Creating ClassFiles object of Chrome
driver.get('https://seleniumbase.io/demo_page')

inputElement = driver.find_element(By.ID, "myTextInput")
print("Input Text: ", inputElement.get_attribute("value"))
print("Input type: ", inputElement.get_attribute("type"))
print("Input ID: ", inputElement.get_attribute("id"))
print("Input Name: ", inputElement.get_attribute("name"))

radioButton = driver.find_element(By.ID, "radioButton2")
print("Ratio Button is Enable : ", radioButton.is_enabled())

radioButton = driver.find_element(By.CSS_SELECTOR, "#tbodyId > tr:nth-child(8) > td:nth-child(4)")
print("Ratio Button is Displayed : ", radioButton.is_displayed())


driver.quit()

# inputElement.clear()




