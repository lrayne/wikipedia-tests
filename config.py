import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('USERNAME')
access_key = os.getenv('ACCESS_KEY')

context = os.getenv('context', 'web')

base_url = os.getenv('base_url', 'https://www.wikipedia.org')
driver_name = os.getenv('driver_name', 'chrome')
hold_driver_at_exit = os.getenv('hold_driver_at_exit', 'false').lower() == 'true'

window_width = os.getenv('window_width', '1024')
window_height = os.getenv('window_height', '768')
timeout = float(os.getenv('timeout', '3.0'))
