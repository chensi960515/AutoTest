# -*- coding: utf-8 -*-
# @Time : 2022/3/18 17:11
# @Author : chensi
# @File : step_pack.py
# @Project : CVATest

import allure
import pytest
from tools import logger



@allure.step("step: 验证请求响应code码 ")
def assert_code(except_code: int, response_code):
    '''响应码验证'''
    try:
        assert except_code == response_code
        return True
    except Exception:
        logger.error("请求状态码对比失败,请求状态码为:{0},断言状态码为:{1}".format(response_code, except_code))


@allure.step("step: 验证响应body返回status和message")
def assert_in_body(except_body: str, response_body):
    '''响应体内容验证'''
    try:
        assert except_body in response_body
        return True
    except Exception:
        logger.error("响应body对比失败,响应body为:{0},断言body为:{1}".format(response_body, except_body))


@allure.step("step: 验证响应body返回status和message")
def assert_equal_body(except_body: str, response_body: str):
    '''响应体内容验证'''
    try:
        assert except_body == response_body
        return True
    except Exception:
        logger.error("响应body对比失败,响应body为:{0},断言body为:{1}".format(response_body, except_body))


@allure.step("step: 验证响应body返回status和message")
def assert_time(except_time, response_time):
    '''响应时间验证'''
    try:
        assert except_time >response_time
        return True
    except Exception:
        logger.error("响应时间超时，断言时间:{0},响应时间:{1}".format(except_time, response_time))
