#!/usr/bin/env/python
#coding:utf8
'''
Created on May 2, 2013

@author: killua
@url:http://www.pythonchallenge.com/pc/def/map.html
@target: @url:http://www.pythonchallenge.com/pc/def/ocr.html

Hint:
    K + 2 = M
    O + 2 = Q
    E + 2 = G
    也就是译码问题，将所有字母的ASC码加2
'''

#version 1
print chr(ord("m") + 2)+chr(ord("a") + 2)+chr(ord("p") + 2)

"""
PS:
字符与ASCII转换
char->ascii ord()
ascii->char chr()
"""

#version 2
print '*' * 20

import string 

s1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
s2 = "map"
t = t=string.maketrans( 'abcdefghijklmnopqrstuvwxyz ', 'cdefghijklmnopqrstuvwxyzab ')
print string.translate(s1,t)
print string.translate(s2, t)
