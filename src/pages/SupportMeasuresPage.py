from selenium.webdriver.common.by import By

from src.pages.BasePage import BasePage

LOCATOR_CHECK_FIELD = (By.XPATH, "/html/body/form/div[3]/div[1]/div[4]/div[2]/div/div/div/div[2]/div/div[9]/div[2]")
LOCATOR_REPORT_FIELD = (By.XPATH, "/html/body/form/div[3]/div[1]/div[4]/div[2]/div/div/div/div[2]/div/div[12]/div[2]")
LOCATOR_DOCS_FIELD = (By.XPATH, "/html/body/form/div[3]/div[1]/div[4]/div[2]/div/div/div/div[2]/div/div[13]/div[2]")
LOCATOR_PAUSE_FIELD = (By.XPATH, "/html/body/form/div[3]/div[1]/div[4]/div[2]/div/div/div/div[2]/div/div[14]/div[2]")


# page object страницы https://www.nalog.ru/rn77/business-support-2020/#t11
# возвращает необходимые для сценариев элементы
class SupportMeasuresPage(BasePage):

    def switch_to_covid_page(self):
        self.driver.switch_to.window(self.switch_to_previous_page())
        return self

    def switch_to_measured_page(self):
        self.driver.switch_to.window(self.switch_to_next_page())
        return self

    # сравнить текст в элементе с ожидаемым текстом
    def check_info_block(self):
        self \
            .element_have(LOCATOR_CHECK_FIELD, "Водный налог")
        return self

    def report_info_block(self):
        self \
            .element_have(LOCATOR_REPORT_FIELD, "Журналы учета полученных и выставленных счетов-фактур")
        return self

    def docs_info_block(self):
        self \
            .element_have(LOCATOR_DOCS_FIELD, "Документы или информация по требованиям")
        return self

    def pause_info_block(self):
        self \
            .element_have(LOCATOR_PAUSE_FIELD, "До 1 июля 2020 года для бизнеса не будут применяться меры взыскания задолженности.")
        return self


