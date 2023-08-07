import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_button(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Открыть страницу')
    def opening_page(self, url):
        self.driver.get(url)

    def input_info(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))

    def scroll_page(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
