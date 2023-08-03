from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class PageMain(BasePage):

    MY_LOCATOR_question = By.XPATH, '//*[@id="accordion__heading-{}"]'
    MY_LOCATOR_answer = By.XPATH, '//*[@id="accordion__panel-{}"]'

    @allure.step('Спускаемся до вопросов и ответов')
    def scroll(self):
        element = self.driver.find_element(By.XPATH, '//*[@id="accordion__heading-7"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_for_element((By.XPATH, '//*[@id="accordion__heading-7"]'))

    @allure.step('Нажимаем на вопрос')
    def click_question(self, num):
        method, locator = self.MY_LOCATOR_question
        locator = locator.format(num)
        self.driver.find_element(method, locator).click()

    @allure.step('Получаем ответ на вопрос')
    def check_click_question(self, num, answers):
        method, locator = self.MY_LOCATOR_answer
        locator = locator.format(num)
        assert answers == self.driver.find_element(method, locator).text
