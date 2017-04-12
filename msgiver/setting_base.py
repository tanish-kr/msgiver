# -*- coding: utf-8 -*-

import six
from abc import ABCMeta, abstractmethod


@six.add_metaclass(ABCMeta)
class SettingBase(object):

    @abstractmethod
    def generate(self, args):
        """
            Generate setting file
            :param dict args: setting parameter
            :raises ParseError:
        """
        pass
