# -*- coding: utf-8 -*-
# @Time : 2022/3/16 16:29
# @Author : chensi
# @File : read_yaml.py
# @Project : CVATest

import yaml
import os
from tools import logger


class GetPages:

    def get_data_list(self, file):
        self.log(file)
        ya = open(file, 'r', encoding='UTF-8')
        cfg = ya.read()
        ya.close()
        data = yaml.safe_load(cfg)
        return data

    def dump_dict(self, file: dict, path):
        try:
            with open(path, "w", encoding="utf-8") as f:
                yaml.dump(file, f, allow_unicode=True)
        except Exception:
            logger.error("写入yaml错误,详细信息为: ", Exception)

    def log(self, file):
        logger.info("开始读取"+file+"文件")
