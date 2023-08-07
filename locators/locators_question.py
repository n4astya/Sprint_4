from selenium.webdriver.common.by import By


class QuestionLocators:
    MY_LOCATOR_question = (By.XPATH, '//*[@id="accordion__heading-{}"]')
    MY_LOCATOR_answer = (By.XPATH, '//*[@id="accordion__panel-{}"]')
    question = (By.XPATH, '//*[@id="accordion__heading-7"]')
    scooter = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')
    yandex_dzen = (By.XPATH, '//img[@alt="Yandex"]')
    up_button = (By.XPATH, "//button[@class = 'Button_Button__ra12g']")
    find = (By.XPATH, "//input[@class='arrow__input mini-suggest__input']")
