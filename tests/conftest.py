import allure
import allure_commons
import pytest
from selene import browser, support
from appium import webdriver
from allure import step
from wikipedia_tests import utils
import settings


@pytest.fixture(scope='function', autouse=True)
def set_up_management():

    with allure.step('Init session'):

        browser.config._wait_decorator = support._logging.wait_with(
            context=allure_commons._allure.StepContext
        )

        if settings.config.context == 'local_web':
            browser.config.base_url = settings.config.base_url
            browser.config.window_width = settings.config.window_width
            browser.config.window_height = settings.config.window_height
            browser.config.driver_name = settings.config.driver_name
            browser.config.hold_driver_at_exit = settings.config.hold_driver_at_exit
            browser.config.timeout = settings.config.timeout

        if settings.config.context == 'local_real_device':
            browser.config.driver = webdriver.Remote(
                settings.config.remote_url, options=settings.to_driver_options()
            )

        if settings.config.context == 'bstack':

            browser.config.driver = webdriver.Remote(
                settings.config.remote_url, options=settings.to_driver_options()
            )
            session_id = browser.driver.session_id

    yield

    utils.allure.add_screenshot()

    if settings.config.context == 'web':
        utils.allure.add_logs()
        utils.allure.add_html()

    if settings.config.context == 'bstack':
        utils.allure.add_xml()
        utils.allure.add_video(session_id)

    if settings.config.context == 'real_device':
        utils.allure.add_xml()

    with step('Tear down session'):
        browser.quit()
