# -*- coding: utf-8 -*-

import six
import logging
from abc import ABCMeta, abstractmethod


@six.add_metaclass(ABCMeta)
class MsgBase(object):

    def __init__(self):
        logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d%H:%M:%S')

    @abstractmethod
    def post(self, message):
        """
            Post a message
            :param str message: Post message
            :raises InternalServerError:
        """
        pass

    @abstractmethod
    def connect(self, options):
        """
            Connection to API
            :param dict options: Connection parameters
            :raises ConnectError:
        """
        pass

    @abstractmethod
    def config(self):
        """
            Config for API
            :return dict: Config data
        """
        pass
