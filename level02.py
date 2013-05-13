#!/usr/bin/env/python
#coding:utf8
'''
Created on May 2, 2013

@author: killua
@url: http://www.pythonchallenge.com/pc/def/ocr.html
@target: http://www.pythonchallenge.com/pc/def/equality.html

Hint:
查看网页源代码，你就可以看到一堆字符，只要在里面找出rare characters（出现次数最少的字符）就可以了。
'''

import re

data = open('./input/level02.in').read()

res = re.findall(r"[A-Za-z]", data)
print ''.join(res)



