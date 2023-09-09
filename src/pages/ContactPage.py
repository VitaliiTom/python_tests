from selenium.webdriver.common.by import By

from src.pages.BasePage import BasePage
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

login_btn = (By.ID, 'log-btn')

class ContactPage(BasePage):
    def setup(self):
        path = os.path.dirname(os.path.abspath('test_Dashboard.py'))
        chrome_driver = path + r"\chromedriver.exe"
        # chrome_driver = "/usr/local/bin/chromedriver"
        url = r"https://mkittest.alarislabs.com"
        options = Options()
        options.add_argument('--headless')
        browser = webdriver.Chrome(chrome_driver)
        browser.get(url)
        browser.implicitly_wait(10)
        return browser

    def open(self):
        self.driver.get("https://service.nalog.ru/covid19/")
        return self

    def go_to_login(self):
        self.wait_element(login_btn).click()