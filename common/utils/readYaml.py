# -*- coding: utf-8 -*-
# @Time : 2022/7/19 9:38
# @Author : chensi
# @File : readYaml.py
# @Project : CVATest

import yaml
from ruamel import yaml


def read_yaml_data(yaml_file):
    """
        读取yaml文件数据

    :param yaml_file:   yaml文件地址
    :return:
    """
    with open(yaml_file, 'r', encoding='utf-8') as yf:
        return yaml.load(yf, Loader=yaml.SafeLoader)


def write_yaml_data(yaml_file, obj):
    """
        obj写入 yaml文件

    :param obj:  需要写入的obj数据
    :param yaml_file: yaml文件地址
    :return:
    """
    with open(yaml_file, 'w', encoding='utf-8') as yf:
        yaml.dump(obj, yf, Dumper=yaml.RoundTripDumper, allow_unicode=True)
