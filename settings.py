import os
from typing import Literal, Optional
import dotenv
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from pydantic_settings import BaseSettings
from wikipedia_tests.utils import file

load_dotenv()


class Config(BaseSettings):

    context: Literal['bstack', 'local_web', 'local_real_device', 'local_emulator'] = (
        'local_real_device'
    )

    base_url: str = 'https://www.wikipedia.org'

    timeout: float = 3.0

    app: str = 'app-alpha-universal-release.apk'
    deviceName: str = 'Google Pixel 5'
    udid: Optional[str] = None
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

    if config.context == 'local_real_device' or config.context == 'local_emulator':
        options.set_capability("app", file.path(config.app))
        options.set_capability("deviceName", config.deviceName)
        options.set_capability("udid", config.udid)

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
