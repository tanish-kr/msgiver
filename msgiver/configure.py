# -*- coding: utf-8 -*-

import os
import yaml


class Configure:
    """
        msgiver configuration class
    """

    CONF_FILE_PATH = os.path.join(os.environ.get("HOME"), ".msgiver.yml")

    def __init__(self):
        self.__conf = None
        if os.path.exists(self.CONF_FILE_PATH):
            self.__conf = yaml.load(open(self.CONF_FILE_PATH).read())

    def all(self):
        return self.__conf

    @classmethod
    def generate(self, args):
        pass

    def slack(self):
        if self.__conf is None:
            return {'token': os.environ.get("SLACK_TOKEN")}
        else:
            return self.__conf['slack']
