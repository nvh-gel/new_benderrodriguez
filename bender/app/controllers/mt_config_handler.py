""" Config handler module  """
from app.models.mt_config import MTConfig


CONFIG = None


def get_config():
    """ Return static config, if not exist, get new config """
    global CONFIG
    if not CONFIG:
        CONFIG = MTConfig().get_config()
    return CONFIG
