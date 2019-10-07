#!/usr/bin/env python
# -*- coding: utf-8 -*-

import upsidedown
import sys

try:
    reload  # Python 2.7
except NameError:
    try:
        from importlib import reload  # Python 3.4+
    except ImportError:
        from imp import reload  # Python 3.0 - 3.3

if sys.version_info[0] == 2:
    sys.setdefaultencoding("utf-8")

__version__ = 0.5

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
