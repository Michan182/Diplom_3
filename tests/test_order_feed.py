from locators import Locators
from pages.order_feed_page import FeedOrder


class TestFeedOrder:
    def test_order_details_is_displayed(self, driver):
        feed_order = FeedOrder(driver)
        feed_order.go_to_site('https://stellarburgers.nomoreparties.site/')
        feed_order.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        feed_order.click_order_feed()
        feed_order.click_top_order_in_feed()
        details_window = feed_order.get_order_details_displayed()
        assert details_window.is_displayed(), "Окно с деталями заказа не отображается"

    def test_order_in_history_displayed_in_feed(self, driver):
        feed_order = FeedOrder(driver)
        feed_order.go_to_site('https://stellarburgers.nomoreparties.site/')
        feed_order.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        feed_order.click_personal_account_button()
        feed_order.make_authorization()
        feed_order.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        feed_order.drag_element_and_drop(Locators.CRATOR_BUN, Locators.TARGET_BASKET)
        feed_order.click_create_order()
        feed_order.click_close_order()
        feed_order.wait_for_invisibility_element(Locators.CLOSE_ORDER)
        feed_order.click_personal_account_button()
        feed_order.wait_for_invisibility_element(Locators.MODAL_OVERLAY)
        feed_order.click_order_history_button_1()
        order_number_history = feed_order.get_order_number_from_history()
        feed_order.click_order_feed1()
        order_number_in_feed = feed_order.get_order_numbers_in_feed()
        assert order_number_history in order_number_in_feed

    def test_count_all_time_orders_changed(self, driver):
        feed_order = FeedOrder(driver)
        feed_order.go_to_site('https://stellarburgers.nomoreparties.site/')
        feed_order.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        feed_order.click_personal_account_button()
        feed_order.make_authorization()
        feed_order.wait_for_feed_clickable()
        feed_order.click_order_feed()
        old_orders_number = feed_order.get_all_time_orders_number()
        feed_order.click_constructor_button()
        feed_order.drag_element_and_drop(Locators.CRATOR_BUN, Locators.TARGET_BASKET)
        feed_order.click_create_order()
        feed_order.click_close_order()
        feed_order.click_order_feed()
        new_orders_number = feed_order.get_all_time_orders_number()
        assert old_orders_number < new_orders_number, "Количество заказов не поменялось"

    def test_count_today_orders_changed(self, driver):
        feed_order = FeedOrder(driver)
        feed_order.go_to_site('https://stellarburgers.nomoreparties.site/')
        feed_order.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        feed_order.click_personal_account_button()
        feed_order.make_authorization()
        feed_order.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        feed_order.wait_for_feed_clickable()
        feed_order.click_order_feed()
        old_orders_today_number = feed_order.get_today_orders_number()
        feed_order.click_constructor_button()
        feed_order.drag_element_and_drop(Locators.CRATOR_BUN, Locators.TARGET_BASKET)
        feed_order.click_create_order()
        feed_order.click_close_order()
        feed_order.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        feed_order.click_order_feed()
        feed_order.wait_for_invisibility_element(Locators.LOADING_HISTORY)
        new_orders_today_number = feed_order.get_today_orders_number()
        assert old_orders_today_number < new_orders_today_number, "Количество заказов не поменялось"

    def test_order_in_progress(self, driver):
        feed_order = FeedOrder(driver)
        feed_order.go_to_site('https://stellarburgers.nomoreparties.site/')
        feed_order.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        feed_order.click_personal_account_button()
        feed_order.make_authorization()
        feed_order.drag_element_and_drop(Locators.CRATOR_BUN, Locators.TARGET_BASKET)
        feed_order.click_create_order()
        feed_order.click_close_order()
        feed_order.click_order_feed()
        feed_order.wait_for_order_in_progress()
        order_in_progress = feed_order.get_order_number_in_progress()
        assert order_in_progress.is_displayed()
