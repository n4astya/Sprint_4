from pages.order_page import Order as O
import allure


class TestRun:
    @allure.title('Проверка возможности сделать заказ')  # декораторы
    @allure.description('Нажимаем на кнопку "Заказать", заполняем поля и проверяем, что заказ создан')
    def test_get_order_first(self, driver):
        # перешли на страницу тестового приложения
        driver.get('https://qa-scooter.praktikum-services.ru/')

        order_page = O()

        order_page.click_button_order(driver)
        order_page.set_name(driver, 'Анастасия')
        order_page.set_surname(driver, 'Кук')
        order_page.set_address(driver, 'Москва')
        order_page.click_metro(driver)
        order_page.set_phone(driver, '89660546789')
        order_page.click_button_further(driver)
        order_page.click_date(driver)
        order_page.click_rental_period(driver)
        order_page.click_color(driver)
        order_page.click_button_order2(driver)
        order_page.click_yes_button(driver)
        order_page.check_order(driver)

    @allure.title('Проверка возможности сделать заказ')  # декораторы
    @allure.description('Нажимаем на кнопку "Заказать", заполняем поля и проверяем, что заказ создан')
    def test_get_order_second(self, driver):
        # перешли на страницу тестового приложения
        driver.get('https://qa-scooter.praktikum-services.ru/')

        order_page = O()

        order_page.click_button_order3(driver)
        order_page.set_name(driver, 'Валерий')
        order_page.set_surname(driver, 'Белый')
        order_page.set_address(driver, 'Муром')
        order_page.click_metro(driver)
        order_page.set_phone(driver, '89660546123')
        order_page.click_button_further(driver)
        order_page.click_date2(driver)
        order_page.click_rental_period(driver)
        order_page.click_color2(driver)
        order_page.click_button_order2(driver)
        order_page.click_yes_button(driver)
        order_page.check_order(driver)
