import urls
from locators import Locators
from pages.personal_account_page import PersonalAccount

class TestPersonalAccount:
    def test_click_personal_account_button(self, driver):
        personal_acc = PersonalAccount(driver)
        personal_acc.go_to_site(urls.MAIN_PAGE_URL)
        personal_acc.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        personal_acc.click_personal_account_button()
        assert driver.current_url == urls.LOGIN_PAGE_URL

    def test_order_history_is_presented(self, driver):
        personal_acc = PersonalAccount(driver)
        personal_acc.go_to_site(urls.MAIN_PAGE_URL)
        personal_acc.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        personal_acc.click_personal_account_button()
        personal_acc.make_authorization()
        personal_acc.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        personal_acc.click_personal_account_button()
        personal_acc.wait_for_invisibility_element(Locators.LOADING_HISTORY)
        personal_acc.wait_to_be_clickable(Locators.PERSONAL_ACCOUNT_HISTORY_BUTTON)
        personal_acc.click_order_history_button()
        personal_acc.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        personal_acc.wait_for_visibility(Locators.PERSONAL_ACCOUNT_HISTORY_LIST)
        history_list = personal_acc.find_element_located(Locators.PERSONAL_ACCOUNT_HISTORY_LIST)
        assert history_list.is_displayed(), "Элементы не найдены"

    def test_exit_personal_account(self, driver):
        personal_acc = PersonalAccount(driver)
        personal_acc.go_to_site(urls.MAIN_PAGE_URL)
        personal_acc.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        personal_acc.click_personal_account_button()
        personal_acc.make_authorization()
        personal_acc.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        personal_acc.wait_to_be_clickable(Locators.PROFILE_BUTTON)
        personal_acc.click_personal_account_button()
        personal_acc.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        personal_acc.wait_for_visibility(Locators.EXIT_BUTTON)
        personal_acc.wait_to_be_clickable(Locators.EXIT_BUTTON)
        personal_acc.click_exit_button()
        personal_acc.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        personal_acc.wait_for_visibility(Locators.PROFILE_BUTTON_ENTER)
        assert driver.current_url == urls.LOGIN_PAGE_URL
