# -*- coding: utf-8 -*-
# @Time : 2022/3/15 11:38
# @Author : chensi
# @File : client_pack.py.py
# @Project : CVATest
import json
from typing import Any
import yaml
import requests
from pathlib import Path
from requests import Session
from tools import allure_step, allure_title, logger, allure_step_no
from tools.data_process import DataProcess


class Transmission:
    PARAMS: str = "params"
    DATA: str = "data"
    JSON: str = "json"


class ClientPack(Session):

    def __init__(self):
        self.session = requests.Session()
        config_path = f"{str(Path(__file__).parent.parent)}/config/config.yaml"
        try:
            ya = open(config_path, 'r', encoding='UTF-8')
            cfg = ya.read()
            ya.close()
            ya_dict = yaml.safe_load(cfg)
            self.host = ya_dict['server']['test']
            self.headers = ya_dict['request_headers']
        except Exception as e:
            logger.error("读取config文件出错,具体信息为", e)
            raise

    def send_request(self, method, uri, parms_type='json', data=None, **kwargs):
        method = method.upper()
        parms_type = parms_type.upper()
        host = self.host
        headers = self.headers

        if isinstance(data, str):
            try:
                data = json.load(data)
            except Exception:
                data = eval(data)

        try:
            if method == 'GET':
                response = self.session.request(headers=headers, method=method, url=host + uri, params=data, **kwargs)
            elif method == 'POST':
                if parms_type == 'FORM':  # 判断是否是表单数据,传递data
                    response = self.session.request(headers=headers, method=method, url=host + uri,
                                                    data=json.dumps(data), **kwargs)
                elif parms_type == 'JSON':  # 判断是否传递applications/json , 若符合,直接传递json参数
                    response = self.session.request(headers=headers, method=method, url=host + uri, json=data, **kwargs)
                else:  # 若需要传递其他类型数据,例如文件,调用下面内容
                    response = self.session.request(headers=headers, method=method, url=host + uri, **kwargs)
            else:
                # put,delete 方法目前未补充
                raise ValueError('request method "{}" error ! please check'.format(method))
            response_data = dict()
            response_data['response_code'] = int(response.status_code)
            response_data['response_time'] = response.elapsed.total_seconds()
            response_data['response_body'] = response.text
            logger.info("请求完成" + host + uri)
            return response_data
        except Exception as e:
            logger.error("请求异常：" + str(e) + ",url:" + host + uri)
            raise

    def __call__(self, method, uri, params_type='form', data=None, **kwargs):
        host = self.host
        headers = self.headers
        return self.send_request(headers=headers, method=method, url=host + uri, params_type=params_type, data=data,
                                 **kwargs)

    def close_session(self):
        self.session.close()
        try:
            del self.session.cookies['JESSIONID']
        except Exception:
            pass

    def action(self, case: list, env: str = "dev") -> Any:
        """处理case数据，转换成可用数据发送请求
        :param case: 读取出来的每一行用例内容，可进行解包
        :param env: 环境名称 默认使用config.yaml server下的 dev 后面的基准地址
        return: 响应结果， 预期结果
        """
        (
            _,
            case_title,
            header,
            path,
            method,
            parametric_key,
            file_obj,
            data,
            extra,
            sql,
            expect,
        ) = case
        logger.debug(
            f"用例进行处理前数据: \n 接口路径: {path} \n 请求参数: {data} \n  提取参数: {extra} \n 后置sql: {sql} \n 预期结果: {expect} \n "
        )
        # allure报告 用例标题
        allure_title(case_title)
        # 处理url、header、data、file、的前置方法
        url = DataProcess.handle_path(path, env)
        header = DataProcess.handle_header(header)
        data = DataProcess.handle_data(data)
        allure_step("请求数据", data)
        file = DataProcess.handler_files(file_obj)
        # 发送请求
        response = self._request(url, method, parametric_key, header, data, file)
        # 提取参数
        DataProcess.handle_extra(extra, response)
        return response, expect, sql

    def _request(
            self, url, method, parametric_key, header=None, data=None, file=None
    ) -> dict:
        """
        :param method: 请求方法
        :param url: 请求url
        :param parametric_key: 入参关键字， params(查询参数类型，明文传输，一般在url?参数名=参数值), data(一般用于form表单类型参数)
        json(一般用于json类型请求参数)
        :param data: 参数数据，默认等于None
        :param file: 文件对象
        :param header: 请求头
        :return: 返回res对象
        """

        if parametric_key == Transmission.PARAMS:
            extra_args = {Transmission.PARAMS: data}
        elif parametric_key == Transmission.DATA:
            extra_args = {Transmission.DATA: data}
        elif parametric_key == Transmission.JSON:
            extra_args = {Transmission.JSON: data}
        else:
            raise ValueError("可选关键字为params, json, data")

        res = self.request(
            method=method, url=url, files=file, headers=header, **extra_args
        )
        response = res.json()
        logger.info(
            f"\n最终请求地址:{res.url}\n请求方法:{method}\n请求头:{header}\n请求参数:{data}\n上传文件:{file}\n响应数据:{response}"
        )
        allure_step_no(f"响应耗时(s): {res.elapsed.total_seconds()}")
        allure_step("响应结果", response)
        return response
