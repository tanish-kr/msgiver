# -*- coding: utf-8 -*-

import six
import sys
import os
from unittest import TestCase
from unittest.mock import patch
from msgiver.configure import Configure
Configure.CONF_FILE_PATH = "._test_msgiver.yml"

class TestSlack(TestCase):

    @classmethod
    def tearDownClass(self):
        os.remove(Configure.CONF_FILE_PATH)

    def test_load_config(self):
        pass

    def test_generate_config(self):
        configure = Configure()
        with patch.object(configure, "_Configure__input_slack", return_value={ "token": "aaa", "channel": "bbbb", "bot_icon": "" }) as method:
            # six.print_(configure.generate())
            self.assertIsNotNone(configure.generate())
            method.assert_called_once_with()
            configure = Configure()
            self.assertIsNotNone(configure.all())
            self.assertIsNotNone(configure.slack())

if __name__ == '__main__':
    unittest.main()
