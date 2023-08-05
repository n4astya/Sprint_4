from selenium.webdriver.common.by import By


class OrderLocators:
    order_button = (By.XPATH, '//button[text()="Заказать"]')  # Кнопка Зкаказать
    name = (By.XPATH, '//input[@placeholder="* Имя"]')  # Поле Имя
    surname = (By.XPATH, '//input[@placeholder="* Фамилия"]')  # Поле Фамилия
    address = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')  # Поле Адрес
    metro = (By.XPATH, '//input[@placeholder="* Станция метро"]')  # Поле Метро
    station = (By.XPATH, '//div[contains(@class, "select-search__select")]/ul/li')  # Станция Бульвар Рокоссовского
    phone = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')  # Поле Телефон
    further_button = (By.XPATH, '//button[text()="Далее"]')  # Кнопка Далее
    date = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')  # Поле даты привоза
    rental_period = (By.XPATH, '//div[@Class="Dropdown-placeholder"]')  # Поле Срок аренды
    period = (By.XPATH, '//div[@Class="Dropdown-menu"]/div')
    color = (By.XPATH, '//*[@id="black"]')  # Поле Цвет самоката
    order_button2 = (By.XPATH, '//div[contains(@class, "Order_Buttons")]//button[text()="Заказать"]')  # Кнопка Зкаказать
    yes_button = (By.XPATH, '//button[text()="Да"]')  # Кнопка Да
    status_button = (By.XPATH, '//button[text()="Посмотреть статус"]')  # Кнопка Посмотреть статус
    order_button3 = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]//button[text()="Заказать"]')
    color2 = (By.XPATH, '//*[@id="grey"]')  # Поле Цвет самоката
    title = (By.XPATH, '//div[contains(@class, "Order_Header")]')  # Про аренду
    order_made = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')

