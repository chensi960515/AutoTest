# -*- coding: utf-8 -*-
# @Time : 2022/7/19 10:40
# @Author : chensi
# @File : readJson.py
# @Project : CVATest


import json


def read_json_file(json_file):
    """
        读取json文件数据

    :param json_file: json文件地址
    :return:
    """
    with open(json_file, 'r', encoding='utf-8') as jf:
        return json.load(jf)


def write_json_file(json_file, obj):
    """
        obj对象写入 json文件
    :param json_file: json文件地址
    :param obj:  需要写入的obj数据对象
    :return:
    """
    with open(json_file, 'w', encoding='utf-8') as jf:
        # 真正的中文需要指定ensure_ascii=False,否则json.dump序列化中文是ASCII字符码; indent 规定缩进
        json.dump(obj, jf, ensure_ascii=False, indent=4)
