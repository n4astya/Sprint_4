from selenium.webdriver.common.by import By
from locators.locators_question import QuestionLocators as Q
from pages.base_page import BasePage
import allure


class PageMain(BasePage):

    @allure.step('Спускаемся до вопросов и ответов')
    def scroll(self):
        self.scroll_page(Q.question)
        self.wait_for_element(Q.question)

    @allure.step('Нажимаем на вопрос')
    def click_question(self, num):
        method, locator = Q.MY_LOCATOR_question
        locator = locator.format(num)
        self.driver.find_element(method, locator).click()

    @allure.step('Получаем ответ на вопрос')
    def check_click_question(self, num, answers):
        method, locator = Q.MY_LOCATOR_answer
        locator = locator.format(num)
        assert answers == self.driver.find_element(method, locator).text
