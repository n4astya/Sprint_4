from pages.question_page import PageMain as P
from locators.locators_question import MainPageLocators as L
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
import allure


class TestRun:
    @allure.title('Проверка возможности увидеть ответы на вопросы')  # декораторы
    @allure.description('На странице ищем вопрос, кликаем на него и проверяем, что открывается ответ на вопрос')
    @pytest.mark.parametrize('num', ['0', '1', '2', '3', '4', '5', '6', '7'])
    def test_get_answer(self, driver, num):

        driver.get('https://qa-scooter.praktikum-services.ru/')

        main_page = P()
        element = driver.find_element(*L.question_live_after_MKAD)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(L.question_live_after_MKAD))

        main_page.click_question(driver, num)
        main_page.check_click_question(driver, num)

