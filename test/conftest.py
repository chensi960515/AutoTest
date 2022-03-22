#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: conftest.py.py
@time: 2022/3/22  20:51
"""

from api.client import Client
from api import step_pack
from tools import read_yaml
from tools import logger
import pytest


client = Client()
ya =  read_yaml.GetPages()


@pytest.fixture(scope='session')
def get_token():
    try:
        data = '{"customerId": "U10000247892","secret": "abc123bcd"}'
        response = client.send_request('POST', '/cvoa/openapi/token', parms_type='json', data=data)
        res = json.loads(response['response_body'])
        token = res['data']['token']

        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])

        expires = res['data']['expires']
        yy = ya.get_data_list('../config/token.yaml')
        logger.info(token)
        yy['token'] = token
        yy['expires'] = expires
        ya.dump_dict(yy, '../config/token.yaml')
        return  response
    except :
        logger.error("初始化token失败!!!")
