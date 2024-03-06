from locators import Locators
from pages.general_functionality_page import GeneralFunctionality

class TestGeneralFunctionality:
    def test_click_order_feed(self, driver):
        general_func = GeneralFunctionality(driver)
        general_func.go_to_site('https://stellarburgers.nomoreparties.site/')
        general_func.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        general_func.click_order_feed()
        order_feed_text = general_func.get_header_text_order_feed()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/feed'
        assert order_feed_text == "Лента заказов"

    def test_click_constructor(self, driver):
        general_func = GeneralFunctionality(driver)
        general_func.go_to_site('https://stellarburgers.nomoreparties.site/')
        general_func.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        general_func.wait_and_click_action_chains(Locators.ORDER_FEED_BUTTON)
        general_func.click_order_feed()
        general_func.click_constructor_button()
        constructor_header_text = general_func.get_header_text_constructor()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert constructor_header_text == "Соберите бургер"

    def test_open_ingredient_details(self, driver):
        general_func = GeneralFunctionality(driver)
        general_func.go_to_site('https://stellarburgers.nomoreparties.site/')
        general_func.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        general_func.wait_and_click_action_chains(Locators.CRATOR_BUN)
        bun_details = general_func.get_bun_text_pop_up()
        bun_name = general_func.get_bun_name_pop_up()
        assert bun_details == 'Детали ингредиента'
        assert bun_name == 'Краторная булка N-200i'

    def test_close_ingredient_details(self, driver):
        general_func = GeneralFunctionality(driver)
        general_func.go_to_site('https://stellarburgers.nomoreparties.site/')
        general_func.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        general_func.click_bun_button()
        general_func.click_close_ingredient_details_button()
        bun_details_window = general_func.find_ingredient_details_window()
        assert not bun_details_window.is_displayed()

    def test_add_bun_to_order(self, driver):
        general_func = GeneralFunctionality(driver)
        general_func.go_to_site('https://stellarburgers.nomoreparties.site/')
        general_func.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        general_func.drag_element_and_drop(Locators.CRATOR_BUN, Locators.TARGET_BASKET)
        total_sum = general_func.get_basket_total_number()
        assert total_sum != 0, "Счетчик булок не изменился"


    def test_order_create(self, driver):
        general_func = GeneralFunctionality(driver)
        general_func.go_to_site('https://stellarburgers.nomoreparties.site/')
        general_func.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        general_func.click_personal_account_button()
        general_func.make_authorization()
        general_func.drag_element_and_drop(Locators.CRATOR_BUN, Locators.TARGET_BASKET)
        general_func.click_create_order()
        general_func.wait_for_visibility(Locators.ORDER_CONTAINER)
        order_details = general_func.get_order_details()
        assert order_details == "идентификатор заказа", "Заказ не оформлен"