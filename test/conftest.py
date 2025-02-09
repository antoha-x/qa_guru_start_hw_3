import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def config_browser():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://duckduckgo.com'
    yield
    browser.quit()
