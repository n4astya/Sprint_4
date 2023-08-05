from selenium.webdriver.common.by import By


class QuestionLocators:
    MY_LOCATOR_question = (By.XPATH, '//*[@id="accordion__heading-{}"]')
    MY_LOCATOR_answer = (By.XPATH, '//*[@id="accordion__panel-{}"]')
    question = (By.XPATH, '//*[@id="accordion__heading-7"]')
