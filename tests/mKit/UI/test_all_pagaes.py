import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from sys import platform
import src.pages.locators
import time

class TestmKit():
    browser = ''
    if platform == "linux" or platform == "linux2":
        print(platform)
        chrome_driver = "/home/test/auto-tests/chromedriver"
    elif platform == "win32":
        path = os.path.dirname(os.path.abspath('test_Partners.py'))
        chrome_driver = path + r"\chromedriver.exe"
    url = r"https://mkittest.alarislabs.com"
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_driver)
    browser.get(url)
    @pytest.fixture(scope='function')
    def setupandauth(self):
        #Определение типа ОС
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.ID, 'username').send_keys(src.pages.locators.mkit_login)
        self.browser.find_element(By.ID, 'password').send_keys(src.pages.locators.mkit_pass)
        self.browser.find_element(By.ID, 'log-btn').click()


    def test_all_pagaes_mkit(self, setupandauth):
        try:
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.mkit_dashboard).click()
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.mkit_campaigns).click()
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.mkit_recipients).click()
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.mkit_conversations).click()
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.mkit_financial_documents).click()
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.mkit_reports).click()
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.mkit_assets).click()
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.mkit_user_management).click()
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.mkit_audit).click()
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.mkit_account).click()
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.mkit_close).click()
        finally:
            self.browser.close()
            self.browser.quit()

