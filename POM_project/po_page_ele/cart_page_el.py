#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 19:52
# @Author  : MC
# @FileName: cart_page_el.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

URL = '?s=/index/cart/index.html'
# iphone商品
IPHONE = (By.XPATH, '//*[@class="am-container cart-content"]/table/tbody/tr/td/div/div/a')
# 数量
NUMBER = (By.XPATH, '//input[@type="number"]')
# 清空
CLEAN = (By.LINK_TEXT, '清空')
# 确定
CONFIRM = (By.XPATH, '//span[text()="确定"]')
