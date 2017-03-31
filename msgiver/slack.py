# -*- coding: utf-8 -*-

import os
import json
import yaml
import urllib.parse
from six.moves import http_client
from msgiver.msg_base import MsgBase
from msgiver.setting_base import SettingBase


class Slack(MsgBase, SettingBase):

    ENV_SLACK_TOKEN = "MSGIVER_SLACK_TOKEN"
    ENV_SLACK_CHANNEL = "MSGIVER_SLACK_DEFAULT_CHANNEL"

    def __init__(self, options=None):
        super().__init__
        self.__options = options

    def post(self, message):
        self.connect()
        __config = self.config()
        __config["text"] = message
        __config.update(self.__options)
        params = urllib.parse.urlencode(__config)
        headers = { "Content-type": "application/x-www-form-urlencoded; charset=utf-8",
                "Accept": "text/plain" }

        self.__connect.request("POST", "/api/chat.postMessage", params, headers=headers)
        response = self.__connect.getresponse()
        data = json.loads(response.read())
        return data

    def connect(self):
        try:
            self.__connect = http_client.HTTPSConnection("slack.com")
            return self.__connect
        except Exception as e:
            logging.error(e.message)


    def config(self):
        setting_file_path = os.path.join(os.environ.get("HOME"), ".msgiver")
        # file or env
        if os.path.exists(setting_file_path):
            with open(setting_file_path) as setting_file:
                try:
                    logging.info(setting_file)
                except Exception as e:
                    logging.error(e.message)
        else:
            self.__token = os.environ.get(self.ENV_SLACK_TOKEN)
            self.__channel = os.environ.get(self.ENV_SLACK_CHANNEL)

        return { "token": self.__token, "channel": self.__channel }

    def generate(self, args):
        pass
