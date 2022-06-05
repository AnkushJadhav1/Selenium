import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_Google_Search_Tab(self):
        self.driver.get("https://www.google.com//")
        self.driver.find_element(By.NAME, "q").send_keys("Python Class in Pune")
        self.driver.find_element(By.NAME, "btnK").click()

    def test_Amazon(self):
        self.driver.get('https://www.amazon.in/')
        self.driver.find_element(By.ID, 'twotabsearchtextbox').is_selected()
        self.driver.find_element(By.CSS_SELECTOR, '#nav-signin-tooltip > a > span').click()
        self.driver.find_element(By.ID, "ap_email").send_keys("7038222100")
        self.driver.find_element(By.ID, 'continue').click()
        self.driver.find_element(By.ID, "ap_password").send_keys("Pass@1234")
        self.driver.find_element(By.ID, 'continue').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Case Pass")
