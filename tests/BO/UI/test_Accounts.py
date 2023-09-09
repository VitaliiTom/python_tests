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
        path = os.path.dirname(os.path.abspath('main'))
        chrome_driver = path + r"\chromedriver.exe"
        print(path)
        url = r"https://mkittest-admin.alarislabs.com"
        print(chrome_driver)
        options = Options()
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_driver)
        self.browser.maximize_window()
        self.browser.get(url)
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.ID, 'username').send_keys('backoffice-manager')
        self.browser.find_element(By.ID, 'password').send_keys('newpassword!')
        self.browser.find_element(By.ID, 'log-btn').click()

    def test_add_account(self, setupandauth):
        Accaunts_array = [src.pages.locators.bo_Accounts_Account, src.pages.locators.bo_Accounts_Description, src.pages.locators.bo_Accounts_Incredit,
                          src.pages.locators.bo_Accounts_Company_name, src.pages.locators.bo_Accounts_Tax_ID, src.pages.locators.bo_Accounts_Legal_address,
                          src.pages.locators.bo_Accounts_Invoicing_address,
                          src.pages.locators.bo_Accounts_Bank_name, src.pages.locators.bo_Accounts_Bank_address,
                          src.pages.locators.bo_Accounts_Bank_account_number, src.pages.locators.bo_Accounts_SWIFT_code]
        try:
            #self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_header_icon).click()
            time.sleep(1)
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_Accounts_Accaunt).click()
            self.browser.find_element(By.CSS_SELECTOR, 'span[class*="iT1WN"]').click()
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_Partners_AddPartners_Country).click()
            self.browser.find_element(By.CSS_SELECTOR,'div[class="dropdown-field__content__overlay"] button[name*="country"]').click()
            time.sleep(1)
            self.browser.find_element(By.XPATH, src.pages.locators.bo_Accounts_AddAccount_Currency).click()
            self.browser.find_element(By.CSS_SELECTOR,'div[class="dropdown-field__content__overlay"] button[name*="country"]').click()
            for i in range(len(Accaunts_array)):
                self.browser.find_element(By.CSS_SELECTOR, Accaunts_array[i]).click()
                self.browser.find_element(By.CSS_SELECTOR, Accaunts_array[i]).send_keys(src.pages.locators.release_version)
            #self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_button_save).click()
        finally:
            self.browser.close()
            self.browser.quit()

    def test_add_account_error(self, setupandauth):
        Accaunts_array = [src.pages.locators.bo_Accounts_Account, src.pages.locators.bo_Accounts_Description,
                          src.pages.locators.bo_Accounts_Incredit,
                                  src.pages.locators.bo_Accounts_Company_name, src.pages.locators.bo_Accounts_Tax_ID,
                                  src.pages.locators.bo_Accounts_Legal_address,
                                  src.pages.locators.bo_Accounts_Invoicing_address,
                                  src.pages.locators.bo_Accounts_Bank_name, src.pages.locators.bo_Accounts_Bank_address,
                                  src.pages.locators.bo_Accounts_Bank_account_number,
                                  src.pages.locators.bo_Accounts_SWIFT_code]
        try:
            result = '//div[text()="You should select a currency"]'
            time.sleep(2)
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_Accounts_Accaunt).click()
            self.browser.find_element(By.CSS_SELECTOR, 'span[class*="iT1WN"]').click()
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_Partners_AddPartners_Country).click()
            self.browser.find_element(By.CSS_SELECTOR, 'div[class="dropdown-field__content__overlay"] button[name*="country"]').click()
            time.sleep(2)
            for i in range(len(Accaunts_array)):
                self.browser.find_element(By.CSS_SELECTOR, Accaunts_array[i]).click()
                self.browser.find_element(By.CSS_SELECTOR, Accaunts_array[i]).send_keys(
                    src.pages.locators.release_version)
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_button_save).click()
            assert result == src.pages.locators.bo_Accounts_result
        finally:
            self.browser.close()
            self.browser.quit()

    def test_edit_account(self, setupandauth):
        Accaunts_array = [src.pages.locators.bo_Accounts_Account, src.pages.locators.bo_Accounts_Description,
                          src.pages.locators.bo_Accounts_Incredit,
                          src.pages.locators.bo_Accounts_Company_name, src.pages.locators.bo_Accounts_Tax_ID,
                          src.pages.locators.bo_Accounts_Legal_address,
                          src.pages.locators.bo_Accounts_Invoicing_address,
                          src.pages.locators.bo_Accounts_Bank_name, src.pages.locators.bo_Accounts_Bank_address,
                          src.pages.locators.bo_Accounts_Bank_account_number,
                          src.pages.locators.bo_Accounts_SWIFT_code]
        try:
            time.sleep(2)
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_Accounts_Accaunt).click()
            time.sleep(1)
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_first_record).click()
            self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_EditButton).click()


            # self.browser.find_element(By.CSS_SELECTOR, 'span[class*="iT1WN"]').click()
            # self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_Partners_AddPartners_Country).click()
            # self.browser.find_element(By.CSS_SELECTOR,
            #                           'div[class="dropdown-field__content__overlay"] button[name*="country"]').click()
            # time.sleep(2)
            # for i in range(len(Accaunts_array)):
            #     self.browser.find_element(By.CSS_SELECTOR, Accaunts_array[i]).click()
            #     self.browser.find_element(By.CSS_SELECTOR, Accaunts_array[i]).send_keys(
            #         src.pages.locators.release_version)
            # self.browser.find_element(By.CSS_SELECTOR, src.pages.locators.bo_button_save).click()

        finally:
            # self.browser.close()
            # self.browser.quit()
            pass

















