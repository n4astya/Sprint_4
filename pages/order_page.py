from locators.locators_order import OrderLocators as O
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Order:
    def click_button_order(self, driver):
        driver.find_element(*O.order_button).click()

    def set_name(self, driver, name):
        driver.find_element(*O.name).send_keys(name)

    def set_surname(self, driver, surname):
        driver.find_element(*O.surname).send_keys(surname)

    def set_address(self, driver, address):
        driver.find_element(*O.address).send_keys(address)

    def click_metro(self, driver):
        driver.find_element(*O.metro).click()
        driver.find_element(*O.station).click()

    def set_phone(self, driver, phone):
        driver.find_element(*O.phone).send_keys(phone)

    def click_button_further(self, driver):
        driver.find_element(*O.further_button).click()

    def click_date(self, driver):
        driver.find_element(*O.date).click()
        driver.find_element(*O.date_6).click()

    def click_rental_period(self, driver):
        driver.find_element(*O.rental_period).click()
        driver.find_element(*O.period).click()

    def click_color(self, driver):
        driver.find_element(*O.color).click()

    def click_button_order2(self, driver):
        driver.find_element(*O.order_button2).click()

    def click_yes_button(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(O.yes_button))
        driver.find_element(*O.yes_button).click()

    def check_order(self, driver):
        assert WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(O.status_button))

    def click_button_order3(self, driver):
        element = driver.find_element(*O.order_button3)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(O.order_button3))
        driver.find_element(*O.order_button3).click()

    def click_color2(self, driver):
        driver.find_element(*O.color2).click()

    def click_date2(self, driver):
        driver.find_element(*O.date).click()
        driver.find_element(*O.date_10).click()
