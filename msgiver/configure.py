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
            with open(self.CONF_FILE_PATH) as config_file:
                self.__conf = yaml.load(config_file.read())

    def all(self):
        return self.__conf

    def slack(self):
        if self.__conf is None:
            return {'token': os.environ.get("SLACK_TOKEN")}
        else:
            return self.__conf['slack']

    def generate(self):
        config_data = {}
        config_data["slack"] = self.__input_slack()
        with open(self.CONF_FILE_PATH, "w") as config_file:
            yaml.dump(config_data, config_file, default_flow_style=False)

        return config_data

    def __input_slack(self):
        while True:
            token = input("Please type for Slack api token. [required] : ")
            if not token:
                continue
            else:
                break

        default_chanel = input("Please type for default channel. [not required] : ")
        bot_icon = input("Please type for image url. [not required] : ")
        return { "token": token, "channel": default_chanel, "bot_icon": bot_icon }
