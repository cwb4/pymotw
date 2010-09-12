#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Escaping escape codes
"""
#end_pymotw_header

from re_test_patterns import test_patterns

test_patterns(r'\d+ \D+ \s+ \S+ \w+ \W+',
              [ r'\\d\+',
                r'\\D\+',
                r'\\s\+',
                r'\\S\+',
                r'\\w\+',
                r'\\W\+',
                ])