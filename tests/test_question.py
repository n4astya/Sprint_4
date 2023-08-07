from pages.question_page import PageMain
from locators.locators_question import QuestionLocators as Q
import pytest
import allure


class TestMainPage:
    @allure.title('Переход на страницу Дзен через кнопку "Яндекс"')
    def test_go_to_dzen(self, driver):

        main_page = PageMain(driver)

        main_page.opening_page('https://qa-scooter.praktikum-services.ru/')

        main_page.click_button_dzen_page()
        main_page.wait_for_element(Q.find)
        assert driver.current_url =='https://dzen.ru/?yredirect=true'

    @allure.title('Переход на главную страницу через кнопку "Самокат"')
    def test_go_to_main_page(self, driver):
        main_page = PageMain(driver)

        main_page.opening_page('https://qa-scooter.praktikum-services.ru/')

        main_page.click_button(Q.up_button)
        main_page.click_scooter_button()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'


class TestQuestion:
    @allure.title('Проверка возможности увидеть ответы на вопросы')
    @allure.description('На странице ищем вопрос, кликаем на него и проверяем, что открывается ответ на вопрос')
    @pytest.mark.parametrize('num, answers', [
                                                ['0', 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
                                                ['1',
                                                 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
                                                ['2',
                                                 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
                                                ['3', 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
                                                ['4', 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
                                                ['5',
                                                 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
                                                ['6', 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
                                                ['7', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
                                            ])
    def test_get_answer(self, driver, num, answers):
        main_page = PageMain(driver)

        main_page.opening_page('https://qa-scooter.praktikum-services.ru/')

        main_page.scroll()
        main_page.click_question(num)
        main_page.check_click_question(num, answers)
