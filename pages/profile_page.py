"""
Page Object для страницы профиля Stellar Burgers
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage:
    """Класс для работы со страницей профиля"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def wait_for_page_load(self):
        """Ожидает загрузки страницы профиля"""
        self.wait.until(EC.presence_of_element_located(ProfilePageLocators.PAGE_TITLE))
    
    def click_logout_button(self):
        """Кликает на кнопку 'Выход'"""
        logout_button = self.wait.until(EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON))
        logout_button.click()
    
    def click_constructor_button(self):
        """Кликает на кнопку 'Конструктор'"""
        constructor_button = self.wait.until(EC.element_to_be_clickable(ProfilePageLocators.CONSTRUCTOR_BUTTON))
        constructor_button.click()
    
    def click_logo(self):
        """Кликает на логотип Stellar Burgers"""
        logo = self.wait.until(EC.element_to_be_clickable(ProfilePageLocators.LOGO))
        logo.click()
    
    def get_user_email(self):
        """Получает email пользователя из поля ввода"""
        try:
            email_input = self.wait.until(EC.presence_of_element_located(ProfilePageLocators.EMAIL_INPUT))
            return email_input.get_attribute('value')
        except:
            return None
