from flask.helpers import get_debug_flag
from my_page.app import create_app
from my_page.settings import ProdConfig

CONFIG = ProdConfig

app = create_app(CONFIG)