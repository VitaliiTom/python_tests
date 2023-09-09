import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from sys import platform
import src.pages.locators

import time


class TestBo():
    browser = ''
    @pytest.fixture(scope='function')
    def setupandauth(self):
        if platform == "linux" or platform == "linux2":
            print(platform)
            chrome_driver = "/home/test/auto-tests/chromedriver"
        elif platform == "win32":
            path = os.path.dirname(os.path.abspath('test_Partners.py'))
            chrome_driver = path + r"\chromedriver.exe"
        url = r"https://mkittest-admin.alarislabs.com"
        options = Options()
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_driver)
        self.browser.maximize_window()
        self.browser.get(url)
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.ID, 'username').send_keys('backoffice-manager')
        self.browser.find_element(By.ID, 'password').send_keys('newpassword!')
        self.browser.find_element(By.ID, 'log-btn').click()
    def test_add_Agreement(self, setupandauth):
        try:
            #self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_header_icon).click()
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_Agreements_Agreement).click()
            self.browser.find_element(By.CSS_SELECTOR, 'span[class*="iT1WN"]').click()

            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_Agreements_Agreement).send_keys(src.pages.locators.realis_version)

            self.browser.find_element(By.CSS_SELECTOR, 'input[name="brandName"]').send_keys(src.pages.locators.realis_version)
            self.browser.find_element(By.CSS_SELECTOR, 'input[name="website"]').send_keys(src.pages.locators.realis_version)
            self.browser.find_element(By.CSS_SELECTOR, 'input[name="phoneNumber"]').send_keys(src.pages.locators.realis_version)
            #Выбор страны из дропдауна
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_Partners_AddPartners_Country).click()
            self.browser.find_element(By.CSS_SELECTOR, 'div[class="dropdown-field__content__overlay"] button[name*="country"]').click()
            #
            self.browser.find_element(By.CSS_SELECTOR, 'textarea[id="address"]').send_keys(src.pages.locators.realis_version)
            self.browser.find_element(By.CSS_SELECTOR, 'textarea[id="comments"]').send_keys(src.pages.locators.realis_version)
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_button_save).click()
        finally:
            pass
            # self.browser.close()
            # self.browser.quit()

    def test_add_edit(self, setupandauth):
        try:
            time.sleep(5)
            self.browser.find_element(By.CSS_SELECTOR,'div[class*="sidebar__item__hidden sidebar__item__expanded"] a[href="/"]').click()
            # self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_header_icon).click()
            time.sleep(5)
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_first_record).click()
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_EditButton).click()

           # self.browser.find_element(By.CSS_SELECTOR, 'input[name="name"]').send_keys(src.pages.locators.realis_version)

        finally:
            pass
            # self.browser.close()
            # self.browser.quit()

















