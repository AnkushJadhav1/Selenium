from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")

elements = driver.find_elements(By.TAG_NAME, "a")  # Find element on web page

for element in elements:
    print(element.text)

element = driver.find_element(By.LINK_TEXT, "seleniumbase.com")
element.click()
