#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"

import EasyDialogs

response = EasyDialogs.AskString('What is your favorite color?', default='blue')
print 'RESPONSE:', response