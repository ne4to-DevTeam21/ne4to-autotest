from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import BASE_URL


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL

    def navigate_to(self, url):
        """Переход на указанный URL."""
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        """Поиск элемента на странице."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((locator))
        )

    def click(self, locator):
        """Клик по элементу."""
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        """Отправка текста в поле ввода."""
        element = self.find_element(locator)
        element.send_keys(text)