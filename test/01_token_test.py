# -*- coding: utf-8 -*-
# @Time : 2022/3/16 18:22
# @Author : chensi
# @File : 01_token_test.py
# @Project : CVATest
import json

import allure
import pytest
from api import client_pack, step_pack
from tools import logger
from tools import read_yaml

client = client_pack.ClientPack()
ya = read_yaml.GetPages()



@allure.feature('token接口测试')
class TestToken:
    @allure.link('https://docs.pytest.org/en/latest', name='pytest帮助文档')
    @allure.issue('http://baidu.com', name='点击我跳转百度')
    @allure.testcase(
        'http://192.168.188.211:8083/zyplayer-doc-manage/doc-wiki#/page/show?pageId=195',
        name='点击我跳转WIKI说明')
    @allure.description('获取Token接口验证-/cvoa/openapi/token')
    @allure.story("正向请求接口")
    @allure.severity("blocker")
    @allure.title("获取token并存储后续使用")
    @pytest.mark.run(order=1)
    def test_token_0(self):
        data = '{"customerId": "U10000247892","secret": "abc123bcd"}'
        response = client.send_request('POST', '/cvoa/openapi/token', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])
        logger.info(response)

        # token存储
        res = json.loads(response['response_body'])
        token = res['data']['token']
        expires = res['data']['expires']
        yy = ya.get_data_list('../config/token.yaml')
        logger.info(token)
        yy['token'] = token
        yy['expires'] = expires
        ya.dump_dict(yy, '../config/token.yaml')


        # @allure.story("反向用例的story")
    # @allure.title("customerId不存在,status = 1008")
    # def test_token_1008(self):
    #     data = '{"customerId": "U100002478921","secret": "abc123bcd"}'
    #     response = client.send_request('POST', '/cvoa/openapi/token', parms_type='json', data=data)
    #     assert response['response_code'] == 200
    #     assert '"status":1008,"message":"客户配置异常"' in response['response_body']
    #     logger.info(response['response_body'])
    #
    # @allure.story("反向用例的story")
    # @allure.title("secret错误2,status = 1005")
    # def test_token_1005(self):
    #     data = '{"customerId": "U10000247892","secret": "abc123bcd11"}'
    #     response = client.send_request('POST', '/cvoa/openapi/token', parms_type='json', data=data)
    #     assert response['response_code'] == 200
    #     assert '"status":1005,"message":"secret错误"' in response['response_body']
    #     logger.info(response['response_body'])

    @allure.story("反向用例的story")
    @allure.title("请求参数为空,status = 1004")
    @pytest.mark.run(order=3)
    def test_token_1004(self):
        data = '{"customerId": "","secret": ""}'
        response = client.send_request('POST', '/cvoa/openapi/token', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":1004,"message":"请求参数验证错误"', response['response_body'])

    @allure.story("反向用例的story")
    @allure.title("密码错误,status = 1005")
    @pytest.mark.run(order=3)
    def test_token_1005(self):
        data='{"customerId": "U10000247892","secret": "abc123bcd11"}'
        response = client.send_request('POST', '/cvoa/openapi/token', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":1005,"message":"secret错误"', response['response_body'])

    @allure.story("反向用例的story")
    @allure.title("企业客户ID错误,status = 1008")
    @pytest.mark.run(order=3)
    def test_token_1008(self):
        data = '{"customerId": "U100002478921","secret": "abc123bcd"}'
        response = client.send_request('POST', '/cvoa/openapi/token', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":1008,"message":"客户配置异常"', response['response_body'])

