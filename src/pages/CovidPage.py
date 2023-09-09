from selenium.webdriver.common.by import By

from src.pages.BasePage import BasePage

LOCATOR_INN_FILED = (By.XPATH, "//*[@id=\"query\"]")
LOCATOR_SEARCH_BUTTON = (By.XPATH, "//*[@id=\"sectionQuery\"]/div/div[1]/div[3]/button")
LOCATOR_MEASURE_BUTTON = (By.XPATH, "//*[@id=\"sectionAll\"]/div/div/div[1]/a")
LOCATOR_PROLONGATION_REPORT_BUTTON = (By.XPATH, "//*[@id=\"sectionAll\"]/div/div/div[2]/a")
LOCATOR_PROLONGATION_DOCS_BUTTON = (By.XPATH, "/html/body/div[1]/div[3]/div/form/div[2]/div/div/div[3]")
LOCATOR_PAUSE_PENALTIES_BUTTON = (By.XPATH, "//*[@id=\"sectionAll\"]/div/div/div[4]/a")


# page object страницы https://service.nalog.ru/covid19/
# возвращает необхимые для элементы для сценариев
class CovidPage(BasePage):

    def open(self):
        self.driver.get("https://service.nalog.ru/covid19/")
        return self

    # ввести текст в поле по символьно и нажать на кнопку поиска.
    # при обычном использовании send_keys столкнулся с проблемой, что вставляется не вся строка
    # возможно из-за большой скорости селениума
    def search_by_inn(self, inn):
        [self.wait_element(LOCATOR_INN_FILED).send_keys(x) for x in inn]
        self.wait_element(LOCATOR_SEARCH_BUTTON).click()
        return self

    def go_to_check_measure(self):
        self.wait_element(LOCATOR_MEASURE_BUTTON).click()

    def go_to_prolongation_report(self):
        self.wait_element(LOCATOR_PROLONGATION_REPORT_BUTTON).click()

    def go_to_prolongation_docs(self):
        self.wait_element(LOCATOR_PROLONGATION_DOCS_BUTTON).click()

    def go_to_pause_penalties(self):
        self.wait_element(LOCATOR_PAUSE_PENALTIES_BUTTON).click()
