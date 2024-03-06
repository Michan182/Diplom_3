import allure
from pages.base_page import BasePage
from locators import Locators
from generate_new_user import register_new_user_and_return_login_password
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class FeedOrder(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Click order feed button")
    def click_order_feed(self):
        self.find_element_located_click(Locators.ORDER_FEED_BUTTON)

    @allure.step("Click top order in feed")
    def click_top_order_in_feed(self):
        self.find_element_located_click(Locators.TOP_ORDER_IN_FEED)

    @allure.step("Find order feed details displayed")
    def get_order_details_displayed(self):
        details_window = self.find_element_located(Locators.ORDER_DETAILS_WINDOW_FEED)
        return details_window

    @allure.step("Click personal account button")
    def click_personal_account_button(self):
        self.find_element_located(Locators.PROFILE_BUTTON).click()

    @allure.step("Enter authorization data")
    def make_authorization(self):
        registration_result = register_new_user_and_return_login_password()
        email, password, _ = registration_result
        self.find_element_located(Locators.EMAIL_LOGIN).send_keys(email)
        self.find_element_located(Locators.PASSWORD_LOGIN).send_keys(password)
        self.find_element_located(Locators.PROFILE_BUTTON_ENTER).click()

    @allure.step("Drag element and drop")
    def drag_element_and_drop(self, source_locator, target_locator):
        source_element = self.find_element_located(source_locator)
        target_element = self.find_element_located(target_locator)
        self.drag_and_drop(self.driver, source_element, target_element)

    @allure.step("Click create order")
    def click_create_order(self):
        self.find_element_located_click(Locators.CREATE_ORDER_BUTTON)

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.CLOSE_ORDER))

    @allure.step("Click close order")
    def click_close_order(self):
        self.find_element_located_click(Locators.CLOSE_ORDER)

    @allure.step("Get order number in feed")
    def get_order_numbers_in_feed(self):
        order_elements = self.find_elements_located(Locators.ORDER_FEED_NUMBER)
        order_numbers = [element.text for element in order_elements]
        return order_numbers


    @allure.step("Get order number from history")
    def get_order_number_from_history(self):
        order_number = self.find_element_located(Locators.ORDER_NUMBER_HISTORY).text
        return order_number

    @allure.step("Get all time orders number")
    def get_all_time_orders_number(self):
        # Ждем, пока элемент станет видимым на странице
        all_time_orders = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.ALL_TIME_ORDERS_NUMBER)
        )
        return all_time_orders.text

    @allure.step("Click Constructor button")
    def click_constructor_button(self):
        self.find_element_located_click(Locators.CONSTRUCTOR_BUTTON)

    @allure.step("Wait for Feed clickable")
    def wait_for_feed_clickable(self):
        self.wait_for_clickable(Locators.ORDER_FEED_BUTTON)

    @allure.step("Get today orders number")
    def get_today_orders_number(self):
        # Ждем, пока элемент станет видимым на странице
        today_orders = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.TODAY_ORDERS_NUMBER)
        )
        return today_orders.text

    @allure.step("Wait for Order in progress")
    def wait_for_order_in_progress(self):
        self.wait_for_clickable(Locators.ORDER_IN_PROGRESS)

    @allure.step("Get order number in progress")
    def get_order_number_in_progress(self):
        order_in_progress = self.find_element_located(Locators.ORDER_IN_PROGRESS)
        return order_in_progress

    def click_order_history_button_1(self):
        locator = Locators.PERSONAL_ACCOUNT_HISTORY_BUTTON
        # Добавим ожидание, чтобы убедиться, что элемент видим и не перекрыт
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        # Добавим ожидание, чтобы убедиться, что элемент кликабелен
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

        # Используем JavaScript для выполнения клика
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Click Order Feed Button")
    def click_order_feed1(self):
        locator = Locators.ORDER_FEED_BUTTON
        # Добавим ожидание, чтобы убедиться, что элемент видим и не перекрыт
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        # Добавим ожидание, чтобы убедиться, что элемент кликабелен
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

        # Используем JavaScript для выполнения клика
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)