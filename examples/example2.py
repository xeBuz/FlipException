#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flipexception import FlipValueError, FlipException


try:
    raise FlipException("Error getting lalala")
except Exception, e:
    print str(e)

try:
    raise FlipValueError("Error getting value")
except Exception, e:
    print str(e)

try:
    raise FlipValueError
except Exception, e:
    print str(e)
