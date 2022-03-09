#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 20:07
# @Author  : MC
# @FileName: case00.py
# @Software: PyCharm
import unittest

from ddt import ddt, file_data
from selenium import webdriver

from config.ChromeOptions import ChromeOption
from po_page_func.cart_page_func import CartPage
from po_page_func.iphone_page_func import IphonePage
from po_page_func.login_page_func import LoginPage


@ddt
class TestCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(options=ChromeOption().option_set())
        cls.Login = LoginPage(cls.driver)
        cls.Iphone = IphonePage(cls.driver)
        cls.Cart = CartPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 登录+添加购物车流程
    @file_data('../data/user.yaml')
    def test_01_add_cart(self, username, password):
        self.Login.login(username, password)
        self.Cart.clean_cart()
        self.Iphone.addcart()
        real = self.Cart.cart_info()
        self.assertTrue(real, msg='断言失败')


if __name__ == '__main__':
    unittest.main()
