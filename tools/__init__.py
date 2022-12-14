# -*- coding: utf-8 -*-
# @Time : 2022/3/15 11:37
# @Author : chensi
# @File : __init__.py.py
# @Project : CVATest

import re
from string import Template
from typing import Any

import sys
import allure
import time
import json
from jsonpath import jsonpath
from loguru import logger
from tools import read_yaml
from tools.hooks import *

ya = read_yaml.GetPages()

# logger.add(sink="../logs/{time:YYYYMMDD}.log", format=" {time:YYYY-MM-DD at HH:mm:ss}| {level} | {function}|{message}",
#            rotation="24h")
logger.add(sink="../logs/{time:YYYYMMDD}.log",
           format=" <green>{time:YYYY-MM-DD at HH:mm:ss}</green> | {level} | {function} |<level>{message}</level>",
           rotation="24h", backtrace=True, diagnose=True)


def GToken():
    try:
        res = ya.get_data_list('../config/token.yaml')
        expires = res['expires']
        now = int(round(time.time() * 1000))
        logger.info("每一个用例文件会创建一次这个方法的对象")
        if now < expires:
            token = res['token']
            return token
        else:
            logger.error("Token已失效,需新获取token")
            raise
    except Exception:
        logger.error("获取token失败", Exception)


def exec_func(func: str) -> str:
    """执行函数(exec可以执行Python代码)
    :params func 字符的形式调用函数
    : return 返回的将是个str类型的结果
    """
    # 得到一个局部的变量字典，来修正exec函数中的变量，在其他函数内部使用不到的问题
    loc = locals()
    exec(f"result = {func}")
    return str(loc['result'])


def extractor(obj: dict, expr: str = '.') -> Any:
    """
    根据表达式提取字典中的value，表达式, . 提取字典所有内容， $.case 提取一级字典case， $.case.data 提取case字典下的data
    :param obj :json/dict类型数据
    :param expr: 表达式, . 提取字典所有内容， $.case 提取一级字典case， $.case.data 提取case字典下的data
    $.0.1 提取字典中的第一个列表中的第二个的值
    """
    # try:
    #     result = jsonpath(obj, expr)[0]
    # except Exception as e:
    #     logger.error(f'{expr} - 提取不到内容，丢给你一个错误！{e}')
    #     result = expr
    # return result
    pass


def rep_expr(content: str, data: dict) -> str:
    """从请求参数的字符串中，使用正则的方法找出合适的字符串内容并进行替换
    :param content: 原始的字符串内容
    :param data: 提取的参数变量池
    return content： 替换表达式后的字符串
    """
    content = Template(content).safe_substitute(data)
    for func in re.findall('\\${(.*?)}', content):
        try:
            content = content.replace('${%s}' % func, exec_func(func))
        except Exception as e:
            logger.error(e)
    return content


def convert_json(dict_str: str) -> dict:
    """
    :param dict_str: 长得像字典的字符串
    return json格式的内容
    """
    try:
        if 'None' in dict_str:
            dict_str = dict_str.replace('None', 'null')
        elif 'True' in dict_str:
            dict_str = dict_str.replace('True', 'true')
        elif 'False' in dict_str:
            dict_str = dict_str.replace('False', 'false')
        dict_str = json.loads(dict_str)
    except Exception as e:
        if 'null' in dict_str:
            dict_str = dict_str.replace('null', 'None')
        elif 'true' in dict_str:
            dict_str = dict_str.replace('true', 'True')
        elif 'false' in dict_str:
            dict_str = dict_str.replace('false', 'False')
        dict_str = eval(dict_str)
        logger.error(e)
    return dict_str


def allure_title(title: str) -> None:
    """allure中显示的用例标题"""
    allure.dynamic.title(title)


def allure_step(step: str, var: str) -> None:
    """
    :param step: 步骤及附件名称
    :param var: 附件内容
    """
    with allure.step(step):
        allure.attach(
            json.dumps(
                var,
                ensure_ascii=False,
                indent=4),
            step,
            allure.attachment_type.JSON)


def allure_step_no(step: str):
    """
    无附件的操作步骤
    :param step: 步骤名称
    :return:
    """
    with allure.step(step):
        pass
