#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 17:53
# @Author  : MC
# @FileName: ChromeOptions.py
# @Software: PyCharm

from selenium import webdriver

'''
Chrome 配置类，用来配置Chrome浏览器的启动初始化配置
参数: headless:无头模式,默认不开启,开启无头模式需要设置该参数为True
      local :加载本地缓存,默认不加载,加载本地缓存需要设置该参数为True
'''
class ChromeOption:
    # 设置配置
    def option_set(self, headless=False, local=False):
        options = webdriver.ChromeOptions()
        # 默认启动的driver窗体最大化
        options.add_argument('start-maximized')
        # 去掉提示正在执行自动化的警告条：没啥用，仅限于强迫症患者以及部分特别的系统。
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 隐身模式。。
        # options.add_argument('incognito')
        # 添加去掉密码弹窗管理
        prefs = {}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        options.add_experimental_option("prefs", prefs)
        # 添加无头指令：需输入参数，headless=True 可以使用，默认不使用。
        if headless:
            options.add_argument('--headless')
        # 加载本地缓存：需输入参数，local=True 可以使用，默认不加载缓存
        if local:
            options.add_argument(r'--user-data-dir=C:\Users\86150\AppData\Local\Google\Chrome\User Data')
        return options
