#!/usr/bin/env python
# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: run.py

@time: 2018/4/9 14:11

@desc:

'''
from scrapy import cmdline


name = 'doubanSpider'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())