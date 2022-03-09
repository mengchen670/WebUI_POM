#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 19:12
# @Author  : MC
# @FileName: login_page_func.py
# @Software: PyCharm
'''
登录页面，
'''
from selenium import webdriver

from base_page.base_page import BasePage
from po_page_ele.login_page_el import *
from config.read_config import read


class LoginPage(BasePage):
    url = read('./config/config.ini', 'Test', 'url') + URL

    def login(self, username, password):
        self.visit(self.url)
        self.input(USERNAME, username)
        self.input(PASSWORD, password)
        self.click(BUTTON)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    user = 'mc670589235'
    pwd = '670589235mc'
    lg = LoginPage(driver)
    lg.login(user, pwd)
