import allure
from pages.base_page import BasePage
from locators import Locators


class PersonalAccount(BasePage):
    email = 'superemail@why.com'
    password = '123456'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Enter authorization data")
    def make_authorization(self):
        self.find_element_located(Locators.EMAIL_LOGIN).send_keys(self.email)
        self.find_element_located(Locators.PASSWORD_LOGIN).send_keys(self.password)
        self.find_element_located(Locators.PROFILE_BUTTON_ENTER).click()
    @allure.step("Click personal account button")
    def click_personal_account_button(self):
        self.find_element_located(Locators.PROFILE_BUTTON).click()

    @allure.step("Click order history")
    def click_order_history_button(self):
        self.scroll_and_click_element(Locators.PERSONAL_ACCOUNT_HISTORY_BUTTON)

    @allure.step("Exit from personal account")
    def click_exit_button(self):
        self.wait_for_visibility(Locators.EXIT_BUTTON)
        self.find_element_located(Locators.EXIT_BUTTON).click()