# -*- coding: utf-8 -*-
# @Time : 2022/3/21 10:40
# @Author : chensi
# @File : test_user.py
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


@allure.feature('新增用户')
class TestUser:
    @allure.description('获取addUser接口验证-/cvoa/openapi/addUser')
    @allure.story("新增用户正向请求接口")
    @allure.severity("blocker")
    @allure.title("新增用户")
    @pytest.mark.skip(reason="暂未提供删除用户接口,无法进行后置处理,暂跳过该用例")
#    @pytest.mark.run(order=2)
    def test_addUser_0(self):
        cus = int(time.time())
        data = {
                    "customerId":"U10000247892",
                    "name":"test-cs",
                    "phoneNumber":"",
                    "email":"",
                    "customAccount":"test1112" + str(cus),
                    "loginPassword":"net263",
                    "videoConfPermission":"1",
                    "phoneJoinPermission":"1",
                    "depName":"/test",
                    "isSendEmail":"1",
                    "token":token
                }
        response = client.send_request('POST', '/cvoa/openapi/addUser', parms_type='json', data=data)
        assert step_pack.assert_code(300, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])
