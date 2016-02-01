#!/usr/bin/env python
# -*- coding: utf-8 -*-

import upsidedown
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

__version__ = 0.3


class FlipException(Exception):

    @staticmethod
    def flip_text(message=None):
        if not message:
            message = "┻━┻"
        else:
            message = upsidedown.transform(message)

        return unicode("(╯°□°）╯︵ " + message)

    def __init__(self, message=None):
        message = self.flip_text(message)
        super(Exception, self).__init__(message)


class ValueError(FlipException, ValueError):
    def __init__(self, message=None):
        super(ValueError, self).__init__(message)


class BaseException(FlipException, BaseException):
    def __init__(self, message=None):
        super(BaseException, self).__init__(message)


class StandardError(FlipException, StandardError):
    def __init__(self, message=None):
        super(StandardError, self).__init__(message)
