import allure
from pages.base_page import BasePage
from locators import Locators


class RestorePass(BasePage):
    email = 'superemail@why.com'
    password = '123456'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Click personal account")
    def click_personal_account_button(self):
        self.find_element_located(Locators.PROFILE_BUTTON).click()

    @allure.step("Click restore password button")
    def click_restore_pass_button(self):
        self.find_element_located(Locators.RESTORE_PASS_BUTTON).click()

    @allure.step("Enter the email")
    def enter_email(self):
        email = self.find_element_located(Locators.RESTORE_PASS_INPUT_FIELD).send_keys(self.email)
        return email

    @allure.step("Click the confirm button for redirection to new pass page")
    def click_confirm_button(self):
        self.find_element_located(Locators.RESTORE_PASS_CONFIRM_BUTTON_END).click()

    @allure.step("Get element")
    def get_element(self):
        restore_page_name = self.find_element_located(Locators.RESTORE_PASS_HEADER_WORD)
        return restore_page_name

    @allure.step("Enter new password")
    def enter_new_password(self):
        new_pass = self.find_element_located(Locators.RESTORE_PASS_INPUT_NEW_PASS_FIELD).send_keys(self.password)
        return new_pass

    @allure.step("Get elements attribute")
    def get_elements_attribute(self, locator):
        element_attribute = self.find_element_located(locator).get_attribute('type')
        return element_attribute

    @allure.step("Click password visibility button")
    def click_pass_visibility_button(self):
        self.find_element_located(Locators.RESTORE_PASS_VISIBILITY).click()
