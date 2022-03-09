#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 20:55
# @Author  : MC
# @FileName: changeinfo_page_func.py
# @Software: PyCharm

from base_page.base_page import BasePage
from po_page_ele.changeinfo_page_el import *
from config.read_config import read


class ChangeinfoPage(BasePage):
    url = read('./config/config.ini', 'Test', 'url') + URL

    def change(self, nickname, birth, sex):
        self.visit(self.url)
        self.input(NICKNAME, nickname)
        self.input(BIRTHDAY, birth)
        if sex == '男':
            self.click(SEX_MALE)
        if sex == '女':
            self.click(SEX_FEMALE)
        if sex == '保密':
            self.click(SEX_NONE)
        self.click(SAVE)
        return self.assert_wait(SUCCESS)