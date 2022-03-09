#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 19:34
# @Author  : MC
# @FileName: read_config.py
# @Software: PyCharm
from configparser import ConfigParser


def read(file, section, option):
    conf = ConfigParser()
    conf.read(file)
    return conf.get(section, option)


if __name__ == '__main__':
    x = read('./config.ini','Test','url')
    print(x)