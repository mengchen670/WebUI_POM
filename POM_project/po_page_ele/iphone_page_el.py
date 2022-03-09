#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 19:23
# @Author  : MC
# @FileName: iphone_page_el.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

URL = '?s=/index/goods/index/id/2.html'
# 套餐
SUITE = (By.XPATH, '//li[@data-value="套餐一"]')
# 颜色
COLOR = (By.XPATH, '//li[@data-value="金色"]')
# 容量
CAPACITY = (By.XPATH, '//li[@data-value="128G"]')
# 加入购物车按钮
ADD_CART = (By.XPATH, '//button[@title="加入购物车"]')
# 数量输入
NUMBER = (By.XPATH, '//input[@type="number"]')