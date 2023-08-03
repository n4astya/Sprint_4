from pages.question_page import PageMain as P
import pytest
import allure


class TestRun:
    @allure.title('Проверка возможности увидеть ответы на вопросы')
    @allure.description('На странице ищем вопрос, кликаем на него и проверяем, что открывается ответ на вопрос')
    @pytest.mark.parametrize('num', ['0', '1', '2', '3', '4', '5', '6', '7'])
    def test_get_answer(self, driver, num):

        driver.get('https://qa-scooter.praktikum-services.ru/')

        main_page = P()

        main_page.scroll(driver)
        main_page.click_question(driver, num)
        main_page.check_click_question(driver, num)
