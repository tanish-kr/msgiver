# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class SettingBase(metaclass=ABCMeta):

    @abstractmethod
    def generate(self, args):
        """
            Generate setting file
            :param dict args: setting parameter
            :raises ParseError:
        """
        pass
