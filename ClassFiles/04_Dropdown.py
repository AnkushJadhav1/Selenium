from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get('https://seleniumbase.io/demo_page')

inputElement = driver.find_element(By.ID, "mySelect")

dropdown = Select(inputElement)

dropdown.select_by_index(3)

dropdown.select_by_value('50%')

dropdown.select_by_visible_text('Set to 25%')

dropdown.select_by_index(3)

