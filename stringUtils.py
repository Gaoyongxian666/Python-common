#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version:  1.0
@author:   Jianzhang Zhang, <jianzhang.zhang@foxmail.com>
@file:     synonymyprocess.py
@time:     2016-10-06
@function: 常用的字符串操作方法
"""

import zhuanma


def jiema(string):
	"""
	将字符串转为unicode编码
	param string: 待转码的字符串
	return      : unicode编码的字符串
	"""
	from zhuanma import strdecode
	return strdecode(string)


def filterReturnChar(string):
	"""
	过滤字符串中的"\r"字符
	:param string:
	:return: 过滤了"\r"的字符串
	"""
	return string.replace("\r", "")


def encodeUTF8(string):
	"""
	将字符串转码为UTF-8编码
	:param string:
	:return: UTF-8编码的字符串
	"""
	return jiema(string).encode("utf-8")


def filterCChar(string):
	"""
	过滤出字符串中的汉字
	:param string: 待过滤字符串
	:return: 汉字字符串
	"""
	import re
	hanzi = re.compile(u"[\u4e00-\u9fa5]+", re.U)
	return "".join(re.findall(hanzi, string))
