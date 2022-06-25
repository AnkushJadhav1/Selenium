from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://seleniumbase.io/demo_page')

inputElement = driver.find_element(By.ID, 'myTextInput2')

print(f"Input Text : {inputElement.get_attribute('text')}")
print(f"Input Value : {inputElement.get_attribute('value')}")
print(f"Input Type : {inputElement.get_attribute('type')}")
print(f"Input Id : {inputElement.get_attribute('id')}")
print(f"Input ClassFiles : {inputElement.get_attribute('ClassFiles')}")
print(f"Input Name : {inputElement.get_attribute('name')}")
print("Inner HTML", inputElement.get_attribute("innerHTML"))
links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))

driver.back()  # redirect to previous page/url

driver.forward()    # Redirect to next