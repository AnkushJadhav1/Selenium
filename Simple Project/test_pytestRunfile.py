from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get('https://www.facebook.com//')


def test_url():
    x = driver.current_url
    y = 'https://www.facebook.com/'
    return x == y


def test_loginIsEnable():
    x = driver.find_element(By.ID, 'email').is_enabled()
    y = True
    return x == y


def test_loginbutton():
    
    y = driver.find_element(By.NAME, 'login').is_enabled()
    x = True
    return x == y



driver.maximize_window()