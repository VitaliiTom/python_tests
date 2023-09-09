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
    @pytest.fixture(scope='function')
    def setupandauth(self):
        #Определение типа ОС
        if platform == "linux" or platform == "linux2":
            print(platform)
            chrome_driver = "/home/test/auto-tests/chromedriver"
        elif platform == "win32":
            path = os.path.dirname(os.path.abspath('test_Dashboard.py'))
            chrome_driver = path + r"\chromedriver.exe"

        url = r"https://mkittest.alarislabs.com"
        options = Options()
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_driver)
        self.browser.get(url)
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.ID, 'username').send_keys(src.pages.locators.mkit_login)
        self.browser.find_element(By.ID, 'password').send_keys(src.pages.locators.mkit_pass)
        self.browser.find_element(By.ID, 'log-btn').click()

    def test_dashboard_show(self, setupandauth):
        try:
            time.sleep(2)
            label_real = self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.mkit_dashboard_label)
            assert label_real.text == 'Dashboard'
        finally:
            self.browser.close()
            self.browser.quit()

    def test_dashboard_goto_contact(self, setupandauth):
        try:
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.mkit_recipients).click()
            time.sleep(2)
            label_real = self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.mkit_contact_label)
            assert label_real.text == "Contacts\nNew Contact"
        finally:
            self.browser.close()
            self.browser.quit()

# def test_dashboard():
#     path = os.path.dirname(os.path.abspath('test_Dashboard.py'))
#     chrome_driver = path + r"\chromedriver.exe"
#     # chrome_driver = "/usr/local/bin/chromedriver"
#     url = r"https://mkittest.alarislabs.com"
#     options = Options()
#     options.add_argument('--headless')
#     browser = webdriver.Chrome(chrome_driver)
#     browser.get(url)
#     browser.implicitly_wait(10)
#     user = browser.find_element(By.ID, 'username')
#     user.send_keys('mkit')
#     password = browser.find_element(By.ID, 'password')
#     password.send_keys('newpassword')
#     log_btn = browser.find_element(By.ID, 'log-btn')
#     log_btn.click()
#     if browser.find_element(By.CLASS_NAME, 'dashboard__top'):
#         print("Успешное отображение главной страницы" + '\n')
#     browser.find_element(By.XPATH, '//img[@src ="/static/media/exit.5ea4c9ff.svg"]').click()

# def test_add_contact():
#     path = os.path.dirname(os.path.abspath('test_Dashboard.py'))
#     chrome_driver = path + r"\chromedriver.exe"
#     url = r"https://mkittest.alarislabs.com"
#     options = Options()
#     options.add_argument('--headless')
#     browser = webdriver.Chrome(chrome_driver)
#     browser.get(url)
#     browser.implicitly_wait(10)
#     user = browser.find_element(By.ID, 'username')
#     user.send_keys('mkit')
#     password = browser.find_element(By.ID, 'password')
#     password.send_keys('newpassword')
#     log_btn = browser.find_element(By.ID, 'log-btn')
#     log_btn.click()
#
#     browser.implicitly_wait(10)
#     browser.find_element(By.XPATH, '//img[@src ="/static/media/subscribers.650d9e21.svg"]').click()
#     browser.find_element(By.XPATH, '//span[@class ="menu-item__label"]').click()
#     browser.find_element(By.XPATH, '//div[@class ="basic-button__text"]').click()
#     browser.implicitly_wait(10)
#     add_phone = '+71112223344'
#     browser.find_element(By.ID, 'phoneNumber').send_keys(add_phone)
#     browser.find_element(By.XPATH, '//img[@src ="/static/media/save.b0b34915.svg"]').click()
#     time.sleep(1)
#     phone = browser.find_element(By.XPATH, '//span[@ref ="eCellValue"]')
#     print(phone.text)
#     if phone.text == add_phone:
#         print("Телефонный номер добавлен" + '\n')










