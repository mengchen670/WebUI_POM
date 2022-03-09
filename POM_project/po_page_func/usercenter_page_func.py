#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 21:08
# @Author  : MC
# @FileName: usercenter_page_func.py
# @Software: PyCharm
from base_page.base_page import BasePage
from po_page_ele.usercenter_page_el import *
from config.read_config import read

'''
用户中心页面，操作行为
'''


class UsercenterPage(BasePage):
    url = read('./config/config.ini', 'Test', 'url') + URL

    # 更换头像操作
    def change_pic(self, pic_path):
        # 进入页面
        self.visit(self.url)
        # 点击修改头像
        self.click(CHANGE_PIC)
        # 输入(上传)修改的头像
        self.input_add(INPUT_PIC, pic_path)
        # 点击保存
        self.click(CONFIRM)
        # 判断是否成功
        return self.assert_wait(SUCCESS)
