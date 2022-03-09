#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 18:56
# @Author  : MC
# @FileName: base_page.py 
# @Software: PyCharm
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

'''
BasePage类，用于封装所有页面基础操作，方便页面对象调用
'''


class BasePage:
    # 初始化浏览器
    def __init__(self, driver):
        self.driver = driver

    # 访问一个URL
    def visit(self, url):
        self.driver.get(url)

    # 定位元素
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 点击操作
    def click(self, loc):
        self.locator(loc).click()

    # 输入文本操作_不清空
    def input_add(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 输入文本操作清空
    def input(self, loc, txt):
        self.locator(loc).clear()
        self.locator(loc).send_keys(txt)

    # 强制等待
    def sleep(self, time_):
        sleep(time_)

    # 显式等待断言
    def assert_wait(self, loc):
        try:
            WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locator(loc), message='等待失败')
            return True
        except:
            return False

    # 文本断言
    def assert_text(self, loc, expect):
        try:
            assert expect in self.locator(loc).text
            return True
        except:
            return False
