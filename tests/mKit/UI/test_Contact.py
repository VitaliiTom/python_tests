import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from sys import platform


import src.pages.locators


class TestmKit():
    browser = ''

    @pytest.fixture(scope='function')
    def setupandauth(self):
        if platform == "linux" or platform == "linux2":
            print(platform)
            chrome_driver = "/home/test/auto-tests/chromedriver"
        elif platform == "win32":
            path = os.path.dirname(os.path.abspath('test_Contact.py'))
            chrome_driver = path + r"\chromedriver.exe"
        url = r"https://mkittest.alarislabs.com"
        options = Options()
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_driver)
        self.browser.maximize_window()
        self.browser.get(url)
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.ID, 'username').send_keys('mkit')
        self.browser.find_element(By.ID, 'password').send_keys('newpassword')
        self.browser.find_element(By.ID, 'log-btn').click()


    def test_add_contact(self, setupandauth):
        try:
            self.browser.implicitly_wait(10)
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_page).click()
            self.browser.find_element(By.XPATH, '//span[@class ="menu-item__label"]').click()
            self.browser.find_element(By.XPATH, '//div[@class ="basic-button__text"]').click()
            self.browser.implicitly_wait(10)
            self.browser.implicitly_wait(30)
            add_phone = '71112223344'
            self.browser.find_element(By.ID, 'phoneNumber').send_keys(add_phone)
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_save_contact).click()
            time.sleep(1)
            phone = self.browser.find_element(By.XPATH, '//span[@ref ="eCellValue"]')
            print(phone.text)
            self.browser.refresh()
        finally:
            self.browser.close()
            self.browser.quit()

    #Редактирование контакта
    def test_edit_contact(self, setupandauth):
        try:
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_page).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_page2).click()
#            self.browser.find_element(By.XPATH, src.pages.locators.mkit_skip_all).click()
            time.sleep(2)
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_first_record).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_button_edit).click()
            self.browser.find_element(By.XPATH, '//input[@id="phoneNumber"]').click()
            for i in range(11):
                self.browser.find_element(By.XPATH, '//input[@id="phoneNumber"]').send_keys(Keys.BACKSPACE)
            self.browser.find_element(By.XPATH, '//input[@id="phoneNumber"]').send_keys('44332221117')
            self.browser.find_element(By.XPATH, '//div[@class="edit-contact-form__buttons"]//button[@class="basic-button basic-button_accent basic-button_new-style"]').click()
        finally:
            self.browser.close()
            self.browser.quit()


    def test_attribute_manager(self, setupandauth):
        try:
            i = 1
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_page).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_skip_all).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_attribute_manager).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_button_cancel).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_attribute_manager).click()
            #self.browser.find_element(By.XPATH, src.pages.locators.mkit_add_new_attribute).click()
            while i < 6:
                self.browser.find_element(By.XPATH, src.pages.locators.mkit_add_new_attribute).click()
                self.browser.find_element(By.XPATH, src.pages.locators.mkit_new_attribute_value_name).send_keys('test'+str(i))
                self.browser.find_element(By.XPATH, '//button[@class="mkit-dropdown-field__control"]').click()
                self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_dropdown +'['+str(i)+']').click()
                if i == 3:
                    self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_atr_add_value).click()
                    self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_atr_settings).send_keys(str(i))
                time.sleep(2)
                self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_save_attrib).click()
                i += 1
        finally:
            pass
            # self.browser.close()
            # self.browser.quit()

    def test_filter_add(self, setupandauth):
        try:
            tel = '44332221117'
            i = 1
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_page).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_skip_all).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_filter).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_filter_enterMask).send_keys(tel)
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_filter_applay).click()
            time.sleep(2)
            #self.browser.find_element(By.XPATH, src.pages.locators.mkit_filter_enterMask).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_filter_dropdown).send_keys(tel)
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_filter_SaveFilter).click()
        finally:
            self.browser.close()
            self.browser.quit()

    # Удаление контакта
    def test_delete_contact(self, setupandauth):
        try:
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_page).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_skip_all).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_first_record).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_button_edit).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_button_delete).click()
            time.sleep(5)
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_button_delete).click()
        finally:
            self.browser.close()
            self.browser.quit()

    # def test_import_contact(self, setupandauth):
    #     try:
    #         self.browser.implicitly_wait(5)
    #         self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_page).click()
    #         self.browser.find_element(By.XPATH, src.pages.locators.mkit_import_contact).click()
    #         path = os.path.dirname(os.path.abspath('test_Contact.py'))
    #         print(path)
    #         time.sleep(2)
    #         self.browser.find_element(By.XPATH, src.pages.locators.mkit_import_contact_button).click()
    #         time.sleep(10)
    #         self.browser.find_element(By.XPATH, src.pages.locators.mkit_import_contact_button).send_keys(r"D:/1/10к1.txt")
    #     finally:
    #         self.browser.close()
    #         self.browser.quit()
        #D:\Аларис\Лаб\AT\PyTest\tests\mKit\UI\10к1.txt
        # download_file = self.browser.find_element(By.XPATH, src.pages.locators.mkit_import_contact_button)
        # download_file.send_keys(path + r"\10к1.txt")

    def test_optout_word(self, setupandauth):
        try:
            i = 1
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_page).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_Optout_words).click()
            while i < 5:
                self.browser.find_element(By.XPATH, src.pages.locators.mkit_new_optout_words_button).click()
                self.browser.find_element(By.XPATH, src.pages.locators.mkit_Opt_out_word).send_keys('stop')
                self.browser.find_element(By.XPATH, src.pages.locators.mkit_select_channel).click()
                self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_dropdown +'['+str(i)+']').click()
                self.browser.find_element(By.XPATH, src.pages.locators.mkit_Opt_Out_Effective_from).click()
                self.browser.find_element(By.XPATH, src.pages.locators.mkit_Opt_Out_Effective_from_value).click()
                self.browser.find_element(By.XPATH, src.pages.locators.mkit_Opt_Out_Effective_till).click()
                self.browser.find_element(By.XPATH, src.pages.locators.mkit_Opt_Out_Effective_till_value).click()
                self.browser.find_element(By.XPATH, src.pages.locators.mkit_Opt_Out_Word_add).click()
                i += 1
            self.browser.refresh()
        finally:
            self.browser.close()
            self.browser.quit()

    def test_optout_word_cancel(self, setupandauth):
        try:
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_contact_page).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_Optout_words).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_new_optout_words_button).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_Opt_out_word).send_keys('stop')
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_button_cancel).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_Opt_Out_Word_no).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_button_cancel).click()
            self.browser.find_element(By.XPATH, src.pages.locators.mkit_Opt_Out_Word_yes).click()
        finally:
            self.browser.close()
            self.browser.quit()


















