#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flipexception import ValueError, FlipException


try:
    raise FlipException("Error getting lalala")
except Exception, e:
    print str(e)

try:
    raise ValueError("Error getting value")
except Exception, e:
    print str(e)

try:
    raise ValueError
except ValueError, e:
    print str(e)
