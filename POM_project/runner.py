#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 8:25
# @Author  : MC
# @FileName: runner.py
# @Software: PyCharm
import time

from config.Email import SendEmail
from HTMLTestReportCN import HTMLTestRunner
import unittest
from config.read_config import read

# 测试用例存储文件夹
case_path = read('./config/config.ini', 'UnitTest', 'path')
# 测试用例筛选py文件
pattern = read('./config/config.ini', 'UnitTest', 'pattern')

# 加载测试用例
discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern=pattern)
# runner,HTML测试报告生成
report_dir = './test_reports/'
# 文件名
report_file = report_dir + time.strftime('%Y_%m_%d_%H%M%S') + 'report.html'
with open(report_file, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title='报告', tester='mc')
    runner.run(discover)
# 发送邮件，初始化邮件对象
mail = SendEmail(username='15022399925@163.com',
                 passwd='VGRPTQZIVORBADMW',
                 recv=['670589235@qq.com'],
                 title='自动发送',
                 content='此次测试报告自动发送测试',
                 file=report_file,
                 ssl=True)
# 发送
mail.send_email()

