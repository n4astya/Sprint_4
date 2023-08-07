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

    @allure.step('Нажимаем на лого "Самокат" для перехода на главную страницу')
    def click_scooter_button(self):
        self.scroll_page(Q.scooter)
        self.click_button(Q.scooter)

    @allure.step('Нажимаем на лого "Яндекс" для перехода на главную страницу Дзен')
    def click_button_dzen_page(self):
        self.scroll_page(Q.yandex_dzen)
        self.click_button(Q.yandex_dzen)
