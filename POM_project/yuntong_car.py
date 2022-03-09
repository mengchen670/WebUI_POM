#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 21:27
# @Author  : MC
# @FileName: yuntong_car.py
# @Software: PyCharm
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://dev.zhanghao.auto.winsenseos.cn/authpage/login")
driver.find_element("xpath", "//div[text()='手机登录']").click()
driver.find_element("id", 'phone').send_keys("13402050043")
driver.find_element("id", 'verification_code').send_keys("000000")
driver.find_element('xpath', '//button[@type="submit"]').click()

