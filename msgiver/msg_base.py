# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class MsgBase(metaclass=ABCMeta):

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
