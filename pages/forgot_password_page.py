"""
Page Object для страницы восстановления пароля Stellar Burgers
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ForgotPasswordPage:
    """Класс для работы со страницей восстановления пароля"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def wait_for_page_load(self):
        """Ожидает загрузки страницы восстановления пароля"""
        # Ожидаем появления заголовка или любого элемента страницы
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]")))
    
    def click_login_link(self):
        """Кликает на ссылку 'Войти'"""
        login_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Войти')]")))
        login_link.click()
