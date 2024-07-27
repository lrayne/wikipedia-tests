import os
from typing import Literal
import dotenv
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from pydantic_settings import BaseSettings
from wikipedia_tests.utils import file

load_dotenv()


class Config(BaseSettings):

    context: Literal['bstack', 'local_web', 'local_real_device'] = 'local_real_device'

    base_url: str = 'https://www.wikipedia.org'
    driver_name: str = 'chrome'
    hold_driver_at_exit: bool = False

    window_width: int = 1024
    window_height: int = 768

    timeout: float = 3.0

    app: str = 'app-alpha-universal-release.apk'
    deviceName: str = 'Google Pixel 5'
    appWaitActivity: str = 'org.wikipedia.*'

    remote_url: str = 'http://hub.browserstack.com/wd/hub'

    projectName: str = 'Project name'
    buildName: str = 'Build name'
    sessionName: str = 'Session name'

    bstack_userName: str = os.getenv('bstack_username')
    bstack_accessKey: str = os.getenv('bstack_accesskey')


config = Config(_env_file=dotenv.find_dotenv(f'.env.{Config().context}'))


def to_driver_options():
    options = UiAutomator2Options()

    options.set_capability(
        "appWaitActivity",
        config.appWaitActivity,
    )

    if config.context == 'local_real_device':
        options.set_capability("app", file.path(config.app))

    if config.context == 'bstack':
        options.load_capabilities(
            {
                "app": config.app,
                "deviceName": config.deviceName,
                'bstack:options': {
                    "projectName": config.projectName,
                    "buildName": config.buildName,
                    "sessionName": config.sessionName,
                    "userName": config.bstack_userName,
                    "accessKey": config.bstack_accessKey,
                },
            }
        )

    return options
