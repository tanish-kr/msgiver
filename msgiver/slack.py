# -*- coding: utf-8 -*-

import os
import json
import yaml
from six.moves import http_client
from six.moves.urllib import parse
from msgiver.msg_base import MsgBase
from msgiver.setting_base import SettingBase


class Slack(MsgBase, SettingBase):

    ENV_SLACK_TOKEN = "MSGIVER_SLACK_TOKEN"
    ENV_SLACK_CHANNEL = "MSGIVER_SLACK_DEFAULT_CHANNEL"

    def __init__(self, options=None):
        super(Slack, self).__init__()
        self.__options = options

    def post(self, message):
        self.connect()
        __config = self.config()
        __config["text"] = message
        __config.update(self.__options)

        if not __config["token"] or not __config["channel"]:
            raise ValueError("Failed, Check your setting files.")

        params = parse.urlencode(__config)
        headers = { "Content-type": "application/x-www-form-urlencoded; charset=utf-8",
                "Accept": "text/plain" }

        self.__connect.request("POST", "/api/chat.postMessage", params, headers=headers)
        response = self.__connect.getresponse()
        raw_data = response.read().decode("UTF-8")

        if raw_data:
            data = json.loads(raw_data)
            self.__connect.close()
            return data
        else:
            return None


    def connect(self):
        try:
            self.__connect = http_client.HTTPSConnection("slack.com")
            return self.__connect
        except Exception as e:
            raise ConnectionError("Failed connection.")


    def config(self):
        setting_file_path = os.path.join(os.environ.get("HOME"), ".msgiver.yml")
        # file or env
        if os.path.exists(setting_file_path):
            with open(setting_file_path) as setting_file:
                try:
                    setting_data = yaml.load(setting_file)
                    self.__token = setting_data["slack"]["token"]
                    self.__channel = setting_data["slack"]["channel"]
                except Exception as e:
                    raise IOError("Failed open setting file.")
        else:
            self.__token = os.environ.get(self.ENV_SLACK_TOKEN)
            self.__channel = os.environ.get(self.ENV_SLACK_CHANNEL)

        return { "token": self.__token, "channel": self.__channel }

    def generate(self, args):
        token = input("Please type for Slack api token. : ")
        default_chanel = input("Please type for default channel. : ")

        pass
