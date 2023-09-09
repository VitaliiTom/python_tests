import pytest
from pytest import raises
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time

def test_dashboard():
#    path = os.path.dirname(os.path.abspath('test_Dashboard.py'))
#    chrome_driver = path + r"\chromedriver.exe"
#    print(chrome_driver)
    chrome_driver = "/usr/local/bin/chromedriver"
    url = r"https://mkittest.alarislabs.com"
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_driver,options=options)
#    #browser.maximize_window()

    browser.get(url)
    #query_window = browser.find_element(By.CLASS_NAME, 'control-label')
    # wait = WebDriverWait(browser, 15, 15)
    # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'form-control')))
    browser.implicitly_wait(10)
    user = browser.find_element(By.ID, 'username')
    user.send_keys('mkit')
    password = browser.find_element(By.ID, 'password')
    password.send_keys('newpassword')
    log_btn = browser.find_element(By.ID, 'log-btn')
    log_btn.click()

    #browser.implicitly_wait(10)
    #browser.find_element(By.CLASS_NAME, 'dashboard__top')
    #if browser.find_element(By.CLASS_NAME, 'dashboard__top__title'):
    #browser.find_element(By.CLASS_NAME, 'basic-button__text')
    if browser.find_element(By.CLASS_NAME, 'dashboard__top'):
        print("Успешное отображение главной страницы" + '\n')

    #assert login.is_displayed()





