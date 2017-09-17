import yaml


class MTConfig(object):
    _git_url = ""
    _config = {}

    def get_config(self):
        if not self._config:
            self.get_config_from_file()
        return self._config

    def get_config_from_file(self):
        try:
            with open('config.dev.yml', 'r') as config_file:
                self._config = yaml.load(config_file)
        except FileNotFoundError:
            self.get_config_from_git()

    def get_config_from_git(self):
        self._config = {}

    def get_config_section(self, config_name):
        return self.get_config()[config_name]
