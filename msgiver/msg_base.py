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

            Args:
                message (str): Post message

            Raises:
                InternalServerError:
        """
        pass

    @abstractmethod
    def connect(self, options):
        """
            Connection to API

            Args:
                options (dict): Connection parameters

            Raises:
                ConnectError:
        """
        pass

    @abstractmethod
    def config(self):
        """
            Config for API

            Returns
                dict: Config data
        """
        pass
