from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene import browser
from allure import step


def test_search_browserstack():

    with step('Найти browserstack'):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")
        ).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
            "BrowserStack"
        )

    with step('Подтвердить результат'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(
            have.size_greater_than_or_equal(0)
        )


def test_search_selenium():

    with step('Найти selenium'):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")
        ).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
            "Selenium (software)"
        )
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
        ).click()

    with step('Подтвердить результат'):
        browser.element((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(
            have.exact_text("Selenium (software)")
        )
