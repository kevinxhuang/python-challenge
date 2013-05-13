#!/usr/bin/env/python
#coding:utf8
'''
Created on May 13, 2013

@author: killua
@url: http://www.pythonchallenge.com/pc/def/peak.html
@target: 

Hint:
    在网页源码中有着这么一段话
    <peakhell src="banner.p">
    <!-- peak hell sounds familiar ? -->
    </peakhell>
    这里包含有两个信息：数据文件banner.p以及pickle模块
    pickle是Python的序列化模块，提供PYTHON对象的序列化与反序列化
'''

import urllib
import pickle 

def read_page(url):
    text = urllib.urlopen(url)
    return text

def deserialization(text):
    return pickle.loads(text)
    
if __name__ == '__main__':
    text = open('./input/level05.in').read()
    lists = deserialization(text)
    print lists
    