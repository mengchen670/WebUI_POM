#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 19:10
# @Author  : MC
# @FileName: login_page_el.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

URL = '?s=/index/user/logininfo.html'
# 用户名
USERNAME = (By.NAME, 'accounts')
# 密码框
PASSWORD = (By.NAME, 'pwd')
# 登录按钮
BUTTON = (By.XPATH, '//button[text()="登录"]')
