# -*- coding: utf-8 -*-

import os
import yaml
from six.moves import input


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
        slack_conf = self.slack()
        while True:
            token = input("Please type for Slack api token. [required] : %s" % slack_conf["token"])
            if not token:
                if slack_conf["token"]:
                    token = slack_conf["token"]
                    break
                else:
                    continue
            else:
                break

        default_chanel = input("Please type for default channel. [not required] : %s" % slack_conf["channel"])
        if not default_chanel and slack_conf["channel"]:
            default_chanel = slack_conf["channel"]

        bot_icon = input("Please type for image url. [not required] : %s" % slack_conf["bot_icon"])
        if not bot_icon and slack_conf["bot_icon"]:
            bot_icon = slack_conf["bot_icon"]

        return { "token": token, "channel": default_chanel, "bot_icon": bot_icon }
