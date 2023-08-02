from selenium.webdriver.common.by import By


class PageMain:

    MY_LOCATOR_question = By.XPATH, '//*[@id="accordion__heading-{}"]'
    MY_LOCATOR_answer = By.XPATH, '//*[@id="accordion__panel-{}"]'

    def click_question(self, driver, num):
        method, locator = self.MY_LOCATOR_question
        locator = locator.format(num)
        driver.find_element(method, locator).click()

    def check_click_question(self, driver, num):
        method, locator = self.MY_LOCATOR_answer
        locator = locator.format(num)
        driver.find_element(method, locator).click()


