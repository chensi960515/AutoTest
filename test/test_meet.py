# -*- coding: utf-8 -*-
# @Time : 2022/3/21 15:45
# @Author : chensi
# @File : test_meet.py
# @Project : CVATest


import json
import pytest
import allure
import time
from api import client, step_pack
from tools import logger
from tools import read_yaml
from tools import GToken

client = client.Client()
ya = read_yaml.GetPages()

token = GToken()


@allure.feature('会议接口')
class TestUser:
    @allure.story("预约会议正向请求接口")
    @allure.severity("blocker")
    @allure.title("预约会议-只填写必填参数")
    @allure.description('预约会议接口验证-/cvoa/openapi/reserveMeet')
    @allure.description('userId: 100003718219,username: test-auto ,passwd : net263')
    def test_reserveMeet_0(self):
        cus = int(time.time())
        data = {
            "userId": "100003718219",
            "token": token
        }
        response = client.send_request('POST', '/cvoa/openapi/reserveMeet', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])

    @allure.story("预约会议正向请求接口")
    @allure.severity("blocker")
    @allure.title("预约会议-填写所有参数")
    def test_reserveMeet_1(self):
        cus = int(time.time())
        data = {
            "userId": "100003718219",
            "token": token
        }
        response = client.send_request('POST', '/cvoa/openapi/reserveMeet', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])
