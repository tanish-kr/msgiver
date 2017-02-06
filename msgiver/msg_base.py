# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class MsgBase(metaclass=ABCMeta):

    @abstractmethod
    def post(self, message):
        pass

    @abstractmethod
    def connect(self, options):
        pass
