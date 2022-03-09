#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 21:15
# @Author  : MC
# @FileName: case01.py
# @Software: PyCharm
import unittest

from ddt import ddt, file_data
from selenium import webdriver

from config.ChromeOptions import ChromeOption
from po_page_func.usercenter_page_func import UsercenterPage
from po_page_func.changeinfo_page_func import ChangeinfoPage
from po_page_func.login_page_func import LoginPage


@ddt
class TestCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(options=ChromeOption().option_set())
        cls.Login = LoginPage(cls.driver)
        cls.Changeinfo = ChangeinfoPage(cls.driver)
        cls.Usercenter = UsercenterPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 登录
    @file_data('../data/user.yaml')
    def test_01_login(self, username, password):
        self.Login.login(username, password)

    # 修改个人信息
    @file_data('../data/userinfo.yaml')
    def test_02_change(self, nickname, birth, sex):
        real = self.Changeinfo.change(nickname, birth, sex)
        # 断言
        self.assertTrue(real, msg='断言失败')
    # 修改头像
    @file_data('../data/picture.yaml')
    def test_03_picture(self, file):
        real = self.Usercenter.change_pic(file)
        self.assertTrue(real, msg='断言失败')


if __name__ == '__main__':
    unittest.main()
