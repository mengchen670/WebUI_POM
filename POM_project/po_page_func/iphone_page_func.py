#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 19:40
# @Author  : MC
# @FileName: iphone_page_func.py
# @Software: PyCharm
from base_page.base_page import BasePage
from po_page_ele.iphone_page_el import *
from config.read_config import read


class IphonePage(BasePage):
    url = read('./config/config.ini', 'Test', 'url') + URL

    def addcart(self):
        self.visit(self.url)
        self.click(SUITE)
        self.sleep(0.5)
        self.click(COLOR)
        self.sleep(0.5)
        self.click(CAPACITY)
        self.click(ADD_CART)
