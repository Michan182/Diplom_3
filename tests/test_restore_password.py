from locators import Locators
from pages.restore_pass_page import RestorePass

class TestRestorePass:
    def test_restore_pass_button_new_page(self, driver):
        restore_pass = RestorePass(driver)
        restore_pass.go_to_site('https://stellarburgers.nomoreparties.site/')
        restore_pass.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        restore_pass.click_personal_account_button()
        restore_pass.click_restore_pass_button()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/forgot-password'

    def test_restore_pass_enter_pass_and_click_restore(self, driver):
        restore_pass = RestorePass(driver)
        restore_pass.go_to_site('https://stellarburgers.nomoreparties.site/')
        restore_pass.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        restore_pass.click_personal_account_button()
        restore_pass.click_restore_pass_button()
        restore_pass.enter_email()
        restore_pass.click_confirm_button()
        restore_page_name = restore_pass.get_element()
        assert restore_page_name.is_displayed(), "Данного текста нет на странице"
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/forgot-password'

    def test_restore_pass_visible_pass(self, driver):
        restore_pass = RestorePass(driver)
        restore_pass.go_to_site('https://stellarburgers.nomoreparties.site/')
        restore_pass.wait_for_invisibility_element(Locators.PRELOADER_ANIMATION)
        restore_pass.click_personal_account_button()
        restore_pass.click_restore_pass_button()
        restore_pass.enter_email()
        restore_pass.click_confirm_button()
        restore_pass.enter_new_password()
        element_before_click = restore_pass.get_elements_attribute(Locators.RESTORE_PASS_UNVISIBLE)
        restore_pass.click_pass_visibility_button()
        element_after_click = restore_pass.get_elements_attribute(Locators.RESTORE_PASS_UNVISIBLE)
        assert element_before_click != element_after_click, "Подсветка не применилась"