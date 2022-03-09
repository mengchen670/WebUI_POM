#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 20:38
# @Author  : MC
# @FileName: changeinfo_page_el.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

URL = '?s=/index/personal/saveinfo.html'
# 昵称
NICKNAME = (By.NAME, 'nickname')
# 性别:男
SEX_MALE = (By.XPATH, '//label[text()=" 男			"]/span/i[2]')
# 性别:女
SEX_FEMALE = (By.XPATH, '//label[text()=" 女			"]/span/i[2]')
# 性别:保密
SEX_NONE = (By.XPATH, '//label[text()=" 保密			"]/span/i[2]')
# 生日
BIRTHDAY = (By.NAME, 'birthday')
# 保存按钮
SAVE = (By.XPATH, '//button[text()="保存"]')
# 成功提示
SUCCESS = (By.XPATH, '//p[text()="编辑成功"]')
