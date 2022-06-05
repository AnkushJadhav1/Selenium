from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com//")

driver.find_element(By.NAME,
                    'q').send_keys("Credence IT Professional Training Institute")
time.sleep(3)

driver.find_element(By.NAME, 'btnK').click()

driver.find_element(By.XPATH,
                    "/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a").click()



