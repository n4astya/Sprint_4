from pages.order_page import Order
from locators.locators_order import OrderLocators as O
import allure


class TestOrder:
    @allure.title('Проверка возможности сделать заказ')
    @allure.description('Нажимаем на кнопку "Заказать", заполняем поля и проверяем, что заказ создан')
    def test_get_order_first(self, driver):

        order_page = Order(driver)

        order_page.opening_page('https://qa-scooter.praktikum-services.ru/')

        order_page.click_button_order()
        order_page.set_name('Анастасия')
        order_page.set_surname('Кук')
        order_page.set_address('Москва')
        order_page.click_metro()
        order_page.set_phone('89660546789')
        order_page.click_button_further()
        order_page.click_date()
        order_page.click_rental_period()
        order_page.click_color()
        order_page.click_button_order2()
        order_page.click_yes_button()
        assert 'Заказ оформлен' in order_page.driver.find_element(*O.order_made).text

    @allure.title('Проверка возможности сделать заказ')
    @allure.description('Нажимаем на кнопку "Заказать", заполняем поля и проверяем, что заказ создан')
    def test_get_order_second(self, driver):

        order_page = Order(driver)

        order_page.opening_page('https://qa-scooter.praktikum-services.ru/')

        order_page.click_button_order3()
        order_page.set_name('Валерий')
        order_page.set_surname('Белый')
        order_page.set_address('Муром')
        order_page.click_metro()
        order_page.set_phone('89660546123')
        order_page.click_button_further()
        order_page.click_date2()
        order_page.click_rental_period()
        order_page.click_color2()
        order_page.click_button_order2()
        order_page.click_yes_button()
        assert 'Заказ оформлен' in order_page.driver.find_element(*O.order_made).text
