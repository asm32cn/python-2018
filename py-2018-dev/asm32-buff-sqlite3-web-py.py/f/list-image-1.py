#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
#

import re

with open('2018-03-12-08-34-57.html', 'r') as fi:
	_content = fi.read()

_list = re.findall('<img .*?>', _content)

for i in _list:
	print i
