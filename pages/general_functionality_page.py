import allure
from pages.base_page import BasePage
from locators import Locators
from generate_new_user import register_new_user_and_return_login_password


class GeneralFunctionality(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Click order feed button")
    def click_order_feed(self):
        self.find_element_located_click(Locators.ORDER_FEED_BUTTON)

    @allure.step("Get header text Лента заказов")
    def get_header_text_order_feed(self):
        text = self.find_element_located(Locators.ORDER_FEED_HEADER_TEXT).get_attribute("textContent")
        return text

    @allure.step("Click Constructor button")
    def click_constructor_button(self):
        self.find_element_located_click(Locators.CONSTRUCTOR_BUTTON)

    @allure.step("Get header text Конструктор")
    def get_header_text_constructor(self):
        text = self.find_element_located(Locators.ORDER_CONSTRUCTOR_HEADER_TEXT).text
        return text

    @allure.step("Click on ingredient")
    def click_bun_button(self):
        self.find_element_located_click(Locators.CRATOR_BUN)

    @allure.step("Get text from Bun details pop up")
    def get_bun_text_pop_up(self):
        text = self.find_element_located(Locators.INGREDIENT_DETAILS).text
        return text

    @allure.step("Get Bun name details pop up")
    def get_bun_name_pop_up(self):
        text = self.find_element_located(Locators.INGREDIENT_NAME).text
        return text

    @allure.step("Close ingredient details window")
    def click_close_ingredient_details_button(self):
        self.find_element_located_click(Locators.INGREDIENT_POP_UP_CLOSE)

    @allure.step("Find ingredient details window")
    def find_ingredient_details_window(self):
        details_window = self.element_wait_invisibility(Locators.INGREDIENT_CONTEXT_WINDOW)
        return details_window

    @allure.step("Drag element and drop")
    def drag_element_and_drop(self, source_locator, target_locator):
        source_element = self.find_element_located(source_locator)
        target_element = self.find_element_located(target_locator)
        self.drag_and_drop(self.driver, source_element, target_element)

    @allure.step("Get basket total price")
    def get_basket_total_number(self):
        number = self.find_element_located(Locators.INGREDIENT_TOTAL_NUMBER).text
        return number

    @allure.step("Enter authorization data")
    def make_authorization(self):
        registration_result = register_new_user_and_return_login_password()
        email, password, _ = registration_result
        self.find_element_located(Locators.EMAIL_LOGIN).send_keys(email)
        self.find_element_located(Locators.PASSWORD_LOGIN).send_keys(password)
        self.find_element_located(Locators.PROFILE_BUTTON_ENTER).click()

    @allure.step("Click create order")
    def click_create_order(self):
        self.find_element_located_click(Locators.CREATE_ORDER_BUTTON)

    @allure.step("Get order details")
    def get_order_details(self):
        order = self.find_element_located(Locators.ORDER_CREATED_TEXT).text
        return order

    @allure.step("Click personal account button")
    def click_personal_account_button(self):
        self.find_element_located(Locators.PROFILE_BUTTON).click()

    @allure.step("Wait for click by action chains")
    def wait_and_click_action_chains(self, locator):
        self.wait_for_clickable(locator)
        self.element_to_click(self.driver, locator)
