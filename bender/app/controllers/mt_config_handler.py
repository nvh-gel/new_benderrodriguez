""" Config handler module  """
from app.models.mt_config import MTConfig


class MTConfigHandler(object):
    """ Handle Bender Config """
    _config = None

    def get_config(self):
        """ Return static config, if not exist, get new config """
        if not self._config:
            self._config = MTConfig().get_config()
        return self._config

    def get_config_section(self, section=None):
        """ Return config section, if not exist, init one and get anew """
        if not self._config:
            self._config = MTConfig().get_config()
        return self._config[section]

    def get_encrypted_config(self):
        """ Return config with encrypted private fields """
        if not self._config:
            self._config = MTConfig().get_config()
        encrypted = self._config
