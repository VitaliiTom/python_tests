from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


# базовый page object класс, в который вынесена общая логика для всех наследуемых page object классов
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # дождаться появления элемента и скролить до него
    def wait_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        return element

    # сравниваем текст передаваемого элемента с ожидаемым
    def element_have(self, locator, text, time=10):
        return WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element(locator, text))

    def switch_to_next_page(self):
        return self.driver.window_handles[1]

    def switch_to_previous_page(self):
        self.driver.close()
        return self.driver.window_handles[0]


