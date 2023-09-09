import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from sys import platform
import time
pages = ['button[class*="header__icon"]'
        ,'div[class*="sidebar__item__hidden sidebar__item__expanded"] a[href="/"]'

]

class TestBo():
    browser = ''
    @pytest.fixture(scope='function')
    def setupandauth(self):
        #Определение типа ОС
        if platform == "linux" or platform == "linux2":
            print(platform)
            chrome_driver = "/usr/local/bin/chromedriver"
        elif platform == "win32":
            path = os.path.dirname(os.path.abspath('test_Partners.py'))
            chrome_driver = path + r"\chromedriver.exe"

        url = r"https://mkittest-admin.alarislabs.com"
        options = Options()
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_driver)
        self.browser.get(url)
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.ID, 'username').send_keys('backoffice-manager')
        self.browser.find_element(By.ID, 'password').send_keys('newpassword!')
        self.browser.find_element(By.ID, 'log-btn').click()

    # def test_all(self, setupandauth):
    #     self.browser.find_element(By.CSS_SELECTOR,'button[class*="header__icon"]').click()
    #     self.browser.find_element(By.CSS_SELECTOR,'div[class*="sidebar__item__hidden sidebar__item__expanded"] a[href*="/accounts"]').click()
    #     accounts = self.browser.find_element(By.CSS_SELECTOR,'div[class*="screen-header undefined"] div[class*="3aYKA"]')
    #     assert accounts.text == "Accounts"



    def test_all_pagaes_bo(self, setupandauth):
        try:
            self.browser.find_element(By.CSS_SELECTOR, 'button[class*="header__icon"]').click()
            self.browser.find_element(By.CSS_SELECTOR, 'div[class*="sidebar__item__hidden sidebar__item__expanded"] a[href="/"]').click()
            self.browser.find_element(By.CSS_SELECTOR, 'div[class*="sidebar__item__hidden sidebar__item__expanded"] a[href*="/accounts"]').click()
            self.browser.find_element(By.CSS_SELECTOR, 'div[class*="sidebar__item__hidden sidebar__item__expanded"] a[href*="/agreements"]').click()
            self.browser.find_element(By.CSS_SELECTOR, 'a[href="/sender-ids"]').click()
            self.browser.find_element(By.CSS_SELECTOR, 'div[class*="sidebar__item__hidden sidebar__item__expanded"] a[href*="/chatbots"]').click()
            self.browser.find_element(By.CSS_SELECTOR, 'a[href="/rate-plans"]').click()
            self.browser.find_element(By.CSS_SELECTOR, 'a[href="/rates"]').click()
            self.browser.find_element(By.CSS_SELECTOR, 'a[href="/payments"]').click()
            self.browser.find_element(By.CSS_SELECTOR, 'a[href="/charges"]').click()
            self.browser.find_element(By.CSS_SELECTOR, 'a[href="/mcc-mnc"]').click()
            self.browser.find_element(By.CSS_SELECTOR, 'a[href="/backoffice-users"]').click()
            self.browser.find_element(By.CSS_SELECTOR, 'a[href="/mKit-users"]').click()
            self.browser.find_element(By.CSS_SELECTOR, 'a[href="/settings"]').click()
        finally:
            self.browser.close()
            self.browser.quit()
