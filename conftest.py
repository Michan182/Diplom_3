import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = Options()
        options.add_argument("--start-maximized")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)
    elif request.param == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    driver.get('https://stellarburgers.nomoreparties.site/')

    yield driver

    driver.quit()
