from selenium import webdriver

driver = webdriver.Chrome()


driver.get("https://www.facebook.com/")

driver.maximize_window()

print(driver.current_url)

print(driver.title)

driver.close()      # Close current window
driver.quit()       # Quits all windows opened by your driver
