import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class saleforcelogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_Login_Tab(self):
        self.driver.get('https://login.salesforce.com/')
        self.driver.find_element(By.ID, 'username').send_keys("jadhavankush14101997@gmail.com")
        self.driver.find_element(By.ID, 'password').send_keys("Pass@1234")
        self.driver.find_element(By.ID, 'Login').click()

    def test_Login_with_invalid(self):
        self.driver.get('https://login.salesforce.com/')
        self.driver.find_element(By.ID, 'username').send_keys("jadhavankush14101997@gmail.com")
        self.driver.find_element(By.ID, 'password').send_keys("Pass@111")
        self.driver.find_element(By.ID, 'Login').click()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Test Case Pass")

