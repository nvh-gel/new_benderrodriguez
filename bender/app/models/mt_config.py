""" Configuration data model """
import yaml


class MTConfig(object):
    """ Config class to store bender configuration """
    _git_url = ""
    _config = {}

    def get_config(self):
        """ Return bender config
        if not set, init one from file """
        if not self._config:
            self.get_config_from_file()
        return self._config

    def get_config_from_file(self):
        """ Return config from file
        if there is no available file, get from git """
        try:
            with open('config.dev.yml', 'r') as config_file:
                self._config = yaml.load(config_file)
            with open('config.classification.yml', 'r') as classification_file:
                classification = yaml.load(classification_file)
            self._config['classification'] = classification['classification']
        except FileNotFoundError:
            self.get_config_from_git()

    def get_config_from_git(self):
        self._config = {}

    def get_config_section(self, config_name):
        return self.get_config()[config_name]
