import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get('https://www.wise.live/')

driver.find_element(By.XPATH, "/html/body/section[1]/div[2]/div/div/div[2]/div/a[4]").click()

time.sleep(2)

driver.find_element(By.CSS_SELECTOR,
                    '#app > div > main > div > div > div > div > div.pa-md-10.pa-6.login-card.rounded-lg.v-card.v-sheet.theme--light > button:nth-child(2) > span').click()

time.sleep(5)

driver.find_element(By.ID, "identifierId").send_keys("jadhavankush0007@gmail.com")

driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()





