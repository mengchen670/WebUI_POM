#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 21:01
# @Author  : MC
# @FileName: usercenter_page_el.py
# @Software: PyCharm
'''
用户中心页面元素
'''
from selenium.webdriver.common.by import By

URL = '?s=/index/user/index.html'
# 修改头像
CHANGE_PIC = (By.LINK_TEXT, '修改头像')
# 上传头像
INPUT_PIC = (By.NAME, 'file')
# 确认按钮
CONFIRM = (By.XPATH, '//button[text()="确认"]')
# 修改成功提示框
SUCCESS = (By.XPATH, '//p[text()="上传成功"]')