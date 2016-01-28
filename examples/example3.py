#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flipexception import FlipValueError, FlipException

try:
    raise FlipException("Error getting lalala")
except Exception as e:
    print(e)

try:
    raise FlipValueError("Error getting value")
except Exception as e:
    print(e)

try:
    raise FlipValueError
except Exception as e:
    print(e)
