import allure_commons
import pytest
from appium.options.android import UiAutomator2Options
from selene import browser, support
from appium import webdriver
from allure import step
import config
from wikipedia_tests import utils


@pytest.fixture(scope='function')
def bstack():

    options = UiAutomator2Options().load_capabilities(
        {
            "platformName": "android",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            "app": "bs://0ff93e27c635bc80292dc1158547a219944fb184",
            "appWaitActivity": 'org.wikipedia.*',
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                "userName": config.username,
                "accessKey": config.access_key,
            },
        }
    )

    with step('Создать драйвер'):
        browser.config.driver = webdriver.Remote(
            "http://hub.browserstack.com/wd/hub", options=options
        )

    browser.config.timeout = config.timeout

    session_id = browser.driver.session_id

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    utils.allure.add_screenshot()
    utils.allure.add_xml()
    utils.allure.add_video(session_id)

    with step('Закрыть браузер'):
        browser.quit()


@pytest.fixture(scope='function')
def local():

    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
    browser.config.base_url = config.base_url

    browser.config.driver_name = config.driver_name
    browser.config.hold_driver_at_exit = config.hold_driver_at_exit
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
    browser.config.timeout = config.timeout
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    utils.allure.add_screenshot()
    utils.allure.add_logs()
    utils.allure.add_html()

    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def set_up_context(request):
    if config.context == 'web':
        request.getfixturevalue('local')
    if config.context == 'bstack':
        request.getfixturevalue('bstack')
    ...
