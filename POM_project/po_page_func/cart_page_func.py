#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 20:01
# @Author  : MC
# @FileName: cart_page_func.py
# @Software: PyCharm
from selenium import webdriver

from base_page.base_page import BasePage
from po_page_ele.cart_page_el import *
from config.read_config import read
from po_page_func.login_page_func import LoginPage


class CartPage(BasePage):
    url = read('./config/config.ini', 'Test', 'url') + URL

    def cart_info(self):
        self.visit(self.url)
        return self.assert_text(IPHONE, 'iPhone')

    def clean_cart(self):
        self.visit(self.url)
        self.click(CLEAN)
        self.click(CONFIRM)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    user = 'mc670589235'
    pwd = '670589235mc'
    lg = LoginPage(driver)
    lg.login(user, pwd)
    car = CartPage(driver)
    print(car.cart_info())
