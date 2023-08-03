from locators.locators_order import OrderLocators as O
from pages.base_page import BasePage
import allure


class Order(BasePage):

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_button_order(self):
        self.click_button(O.order_button)

    @allure.step('Вводим имя')
    def set_name(self, name):
        self.input_info(O.name, name)

    @allure.step('Вводим фамилию')
    def set_surname(self, surname):
        self.input_info(O.surname, surname)

    @allure.step('Вводим адрес')
    def set_address(self, address):
        self.input_info(O.address, address)

    @allure.step('Вибираем станцию метро')
    def click_metro(self):
        self.click_button(O.metro)
        self.click_button(O.station)

    @allure.step('Вводим номер телефона')
    def set_phone(self, phone):
        self.input_info(O.phone, phone)

    @allure.step('Нажимаем на кнопку "Далее"')
    def click_button_further(self):
        self.click_button(O.further_button)

    @allure.step('Вибираем дату доставки')
    def click_date(self):
        self.click_button(O.date)
        self.click_button(O.date_6)

    @allure.step('Вибираем период использования самоката')
    def click_rental_period(self):
        self.click_button(O.rental_period)
        self.click_button(O.period)

    @allure.step('Вибираем цвет самоката')
    def click_color(self):
        self.click_button(O.color)

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_button_order2(self):
        self.click_button(O.order_button2)

    @allure.step('Подтверждаем оформление заказа')
    def click_yes_button(self):
        self.wait_for_element(O.yes_button)
        self.click_button(O.yes_button)

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_button_order3(self):
        element = self.driver.find_element(*O.order_button3)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_for_element(O.order_button3)
        self.click_button(O.order_button3)

    @allure.step('Вибираем цвет самоката')
    def click_color2(self):
        self.click_button(O.color2)

    @allure.step('Вибираем дату доставки')
    def click_date2(self):
        self.click_button(O.date)
        self.click_button(O.date_10)
