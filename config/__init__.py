# -*- coding: utf-8 -*-
# @Time : 2022/3/15 11:36
# @Author : chensi
# @File : __init__.py.py
# @Project : CVATest

import os
from common.utils.readYaml import read_yaml_data

# 获取主目录路径
ROOT_DIR = str(os.path.reaplath(__file__)).split('config')[0].replace('\\', '/')

# 获取配置文件路径
API_CONFIG = ROOT_DIR + 'config/apiConfig.yaml'
RUN_CONFIG = ROOT_DIR + 'config/runConfig.yaml'
# DB_CONFIG =


# 获取运行配置信息
RC = read_yaml_data(RUN_CONFIG)
INTERVAL = RC['interval']
PROJECT_NAME = RC['project_name']

# 测试数据目录(test.yaml)
DATA_DIR = ROOT_DIR + PROJECT_NAME + '/page'
# 测试脚本目录(test.py)
PAGE_DIR = ROOT_DIR + PROJECT_NAME + '/testcase'
# 测试报告目录(xml|html)
REPORT_DIR = ROOT_DIR + PROJECT_NAME + '/report'
