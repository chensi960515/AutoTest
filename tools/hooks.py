# -*- coding: utf-8 -*-
# @Time : 2022/3/15 11:43
# @Author : chensi
# @File : hooks.py
# @Project : CVATest

import json
import time


def get_current_highest():
    """获取当前时间戳"""
    return int(time.time())


def sum_data(a, b):
    """计算函数"""
    return a + b


def set_token(token: str):
    """设置token，直接返回字典"""
    return {"Authorization": token}
