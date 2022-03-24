#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: conftest.py
@time: 2022/3/23  0:18
"""

import os
import pytest
from tools import logger
from tools import GToken

@pytest.fixture(scope='session')
def get_token():
    token = GToken()
    return token


def pytest_sessionfinish(session):
    """测试完成自动生成并打开allure报告"""
    if session.config.getoption('allure_report_dir'):
        try:
            # 判断allure在环境路径中，通常意味着可以直接执行
            if [i for i in os.getenv('path').split(';') if os.path.exists(i) and 'allure' in os.listdir(i)]:
                # 默认生成报告路径为: ./allure-report
                os.system(f"allure generate -c {session.config.getoption('allure_report_dir')}")
                os.system(f"allure open allure-report")
            else:
                logger.warn('allure不在环境变量中，无法直接生成html报告！')
        except Exception as e:
            logger.warn(e)