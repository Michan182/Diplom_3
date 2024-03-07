from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        return self.driver.get(url)

    def find_element_located(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    def find_element_located_click(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}').click()

    def find_elements_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Elements not found in {locator}')

    def scroll_and_click_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                         message=f'Element not found in {locator}')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def get_current_url(self):
        return self.driver.get_current_url()

    def element_wait_invisibility(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator),
                                                         message=f'Elements found in {locator}')
        return element

    def drag_and_drop(self, driver, source_element, target_element):
        actions = ActionChains(driver)
        actions.drag_and_drop(source_element, target_element).perform()

    def wait_for_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def element_to_click(self, driver, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator))
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def wait_for_invisibility_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))

    def wait_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def wait_for_visibility(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except Exception as e:
            raise TimeoutError(f"Элемент {locator} не стал видимым за {timeout} секунд") from e