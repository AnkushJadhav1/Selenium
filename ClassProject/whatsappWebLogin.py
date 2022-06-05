import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.google.com//')

driver.find_element(By.NAME, "q").send_keys("web whatsapp")

time.sleep(3)

driver.find_element(By.CSS_SELECTOR,
                    "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > "
                    "div.UUbT9 > div.aajZCb > div.CqAVzb.lJ9FBc > center > input.gNO89b").click()
time.sleep(5)

#driver.find_element(By.CLASS_NAME, "iUh30 tjvcx").click()


