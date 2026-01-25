"""
Page Object для главной страницы Stellar Burgers
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators


class MainPage:
    """Класс для работы с главной страницей"""
    
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/"
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        """Открывает главную страницу"""
        self.driver.get(self.base_url)
        self.wait_for_page_load()
    
    def wait_for_page_load(self):
        """Ожидает загрузки главной страницы"""
        self.wait.until(EC.presence_of_element_located(MainPageLocators.PAGE_TITLE))
    
    def click_login_button(self):
        """Кликает на кнопку 'Войти в аккаунт'"""
        login_button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON))
        login_button.click()
    
    def click_personal_account_button(self):
        """Кликает на кнопку 'Личный кабинет'"""
        account_button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        account_button.click()
    
    def click_constructor_button(self):
        """Кликает на кнопку 'Конструктор'"""
        constructor_button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON))
        constructor_button.click()
    
    def click_logo(self):
        """Кликает на логотип Stellar Burgers"""
        logo = self.wait.until(EC.element_to_be_clickable(MainPageLocators.LOGO))
        logo.click()
    
    def click_buns_section(self):
        """Кликает на раздел 'Булки' в конструкторе"""
        buns_section = self.wait.until(EC.element_to_be_clickable(MainPageLocators.BUNS_SECTION))
        buns_section.click()
    
    def click_sauces_section(self):
        """Кликает на раздел 'Соусы' в конструкторе"""
        sauces_section = self.wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION))
        sauces_section.click()
    
    def click_fillings_section(self):
        """Кликает на раздел 'Начинки' в конструкторе"""
        fillings_section = self.wait.until(EC.element_to_be_clickable(MainPageLocators.FILLINGS_SECTION))
        fillings_section.click()
    
    def is_buns_section_active(self):
        """Проверяет, активен ли раздел 'Булки'"""
        try:
            active_section = self.wait.until(EC.presence_of_element_located(MainPageLocators.ACTIVE_SECTION))
            return "Булки" in active_section.text
        except:
            return False
    
    def is_sauces_section_active(self):
        """Проверяет, активен ли раздел 'Соусы'"""
        try:
            active_section = self.wait.until(EC.presence_of_element_located(MainPageLocators.ACTIVE_SECTION))
            return "Соусы" in active_section.text
        except:
            return False
    
    def is_fillings_section_active(self):
        """Проверяет, активен ли раздел 'Начинки'"""
        try:
            active_section = self.wait.until(EC.presence_of_element_located(MainPageLocators.ACTIVE_SECTION))
            return "Начинки" in active_section.text
        except:
            return False
