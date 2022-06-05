import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com//")

driver.maximize_window()

driver.find_element(By.NAME,
                    "q").send_keys("Youtube")
time.sleep(3)

driver.find_element(By.NAME,
                    "btnK").click()

driver.find_element(By.XPATH,
                    "/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div["
                    "1]/a/h3").click()

search_container = driver.find_element(By.ID,
                                       "search-container")

print(f"search-container is Enable : {search_container.is_enabled()}")

time.sleep(3)

driver.find_element(By.NAME, "search_query").send_keys("Automation Animation Video")

driver.find_element(By.ID, 'search-icon-legacy').click()

time.sleep(3)

driver.get("https://www.youtube.com/watch?v=5Q_gi3pWFPs")

time.sleep(10)

driver.quit()

