import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://the-internet.herokuapp.com/javascript_alerts")


inputElement = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
inputElement.click()

time.sleep(3)
# driver.switch_to_alert().accept()       # older version syntax
driver.switch_to.alert.accept()     # Ok  # click on ok

# driver.switch_to_alert().dismiss()       # older version syntax
# driver.switch_to.alert.dismiss()     # Cancel  # click on Cancel


