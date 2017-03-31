# -*- coding: utf-8 -*-

import six
import unittest
import sys
from msgiver.slack import Slack

class TestSlack(unittest.TestCase):

    def test_sample(self):
        # print(dir(Slack))
        # print(sys.path)
        self.assertEqual(True, True)

    def test_new_instance(self):
        slack = Slack()
        self.assertIsInstance(slack, Slack)

    def test_get_config(self):
        slack = Slack()
        six.print_(slack.config())

    def test_post_message(self):
        from datetime import datetime
        slack = Slack({ "pretty": 1 })
        config = slack.config()
        res = slack.post("Hello, Now time = %s " % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        six.print_(res)
        self.assertTrue(res["ok"])
        self.assertEqual(res["channel"], config["channel"])


if __name__ == '__main__':
    unittest.main()
