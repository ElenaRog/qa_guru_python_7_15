import os
import pytest

from selene import browser
from selenium import webdriver

from utils import attach

options = webdriver.ChromeOptions()


@pytest.fixture(scope='function', autouse=True)
def browser_opt():
    from dotenv import load_dotenv
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    selenoid_capabilities = {
        'browserName': 'chrome',
        'browserVersion': '100'
    }

    browser.config.base_url = 'https://nexign.com/ru/'
    browser.config.window_height = 1080
    browser.config.window_width = 1920


    options.capabilities.update(selenoid_capabilities)


    browser.config.driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)

    browser.quit()
