# -*- coding: utf-8 -*-
# @Time : 2022/3/21 15:45
# @Author : chensi
# @File : 02_meet_test.py
# @Project : CVATest


import json
import pytest
import allure
import time
from api import client_pack, step_pack
from tools import logger
from tools import read_yaml
from tools import GToken

client = client_pack.ClientPack()
ya = read_yaml.GetPages()

#@pytest.mark.skip(reason="暂未提供删除用户接口,无法进行后置处理,暂跳过该用例")
@allure.feature('会议接口')
class TestMeet():

    @allure.story("预约会议正向请求接口")
    @allure.severity("blocker")
    @allure.title("预约会议-只填写必填参数")
    @allure.description('预约会议接口验证-/cvoa/openapi/reserveMeet')
    @allure.description('userId: 100003718219,username: test-auto ,passwd : net263')
    @pytest.mark.run(order=2)
    def test_reserveMeet_0(self, get_token):
        data = {
            "userId": "100003718219",
            "token": get_token
        }
        response = client.send_request('POST', '/cvoa/openapi/reserveMeet', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])
        res = json.loads(response['response_body'])
        global global_meetId_1
        global_meetId_1 = res['data']['meetId']

    @allure.story("预约会议正向请求接口")
    @allure.severity("blocker")
    @allure.title("预约会议-填写所有参数")
    @pytest.mark.run(order=2)
    def test_reserveMeet_1(self, get_token):
        cus = int(round(time.time() * 1000))
        data = {
            "agenda": "测试议程",
            "duration": 60,
            "enableLive": 1,
            "helperPassword": "123456",
            "livePassword": "333333",
            "liveStartTime": (cus+600000),
            "meetLock": 1,
            "meetNumber": "会议编号"+ str(cus + 600000),
            "participantList": [
                {
                    "account": "",
                    "userId": ""
                }
            ],
            "startTime": (cus+600000),
            "remindTime": 1,
            "title": "测试预约会议创建",
            "userId": "100003718219",
            "token": get_token
        }
        response = client.send_request('POST', '/cvoa/openapi/reserveMeet', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])
        res = json.loads(response['response_body'])
        global global_meetId_2 ,MeetLink
        global_meetId_2 = res['data']['meetId']
        MeetLink = res['data']['hostMeetLink']

    @allure.story("预约会议反向请求接口")
    @allure.title("预约会议-填写错误参数(userid不存在)")
    @pytest.mark.run(order=3)
    def test_reserveMeet_1031(self, get_token):
        cus = int(round(time.time() * 1000))
        data = {
            "agenda": "测试议程" ,
            "duration": 60,
            "enableLive": 1,
            "helperPassword": "123456",
            "livePassword": "123456",
            "liveStartTime": cus + 1800000,
            "meetLock": 1,
            "meetNumber": "会议编号 "+ str(cus + 1800000),
            "participantList": [
                {
                    "account": "",
                    "userId": ""
                }
            ],
            "startTime": cus + 1800000,
            "remindTime": 1,
            "title": "测试预约会议创建",
            "userId": 1000032154714,
            "token": get_token
        }
        response = client.send_request('POST', '/cvoa/openapi/reserveMeet', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":1031,"message":"用户账号异常"', response_body=response['response_body'])


    @allure.story("预约会议反向请求接口")
    @allure.title("预约会议-填写错误参数(预约时间为过去时间)")
    @pytest.mark.run(order=3)
    def test_reserveMeet_1024(self, get_token):
        cus = int(round(time.time() * 1000))
        data = {
            "agenda": "测试议程" ,
            "duration": 60,
            "enableLive": 1,
            "helperPassword": "123456",
            "livePassword": "123456",
            "liveStartTime": (cus - 1800000),
            "meetLock": 1,
            "meetNumber": "会议编号"+ str(cus- 1800000 ),
            "participantList": [
                {
                    "account": "",
                    "userId": ""
                }
            ],
            "startTime": (cus - 1800000),
            "remindTime": 1,
            "title": "测试预约会议创建",
            "userId": 100003718219,
            "token": get_token
        }
        response = client.send_request('POST', '/cvoa/openapi/reserveMeet', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":1024,"message":"会议开始时间不能早于当前时间"', response_body=response['response_body'])

    @allure.story("编辑会议正向请求接口")
    @allure.severity("blocker")
    @allure.title("编辑会议-只填写必填参数")
    @pytest.mark.run(order=2)
    @allure.description('预约会议接口验证-/cvoa/openapi/editMeet')
    def test_editMeet_1(self, get_token):
        data = {
            "meetId": global_meetId_1 ,
            "token": get_token
        }
        response = client.send_request('POST', '/cvoa/openapi/editMeet', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])


    @allure.title("编辑会议-修改会议议程")
    @pytest.mark.run(order=2)
    @allure.description('预约会议接口验证-/cvoa/openapi/editMeet')
    def test_editMeet_2(self, get_token):
        data = {
            "agenda": '编辑后的会议议程',
            "meetId": global_meetId_1,
            "token": get_token
        }
        response = client.send_request('POST', '/cvoa/openapi/editMeet', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])


    @allure.title("编辑会议-修改会议开始时间")
    @pytest.mark.run(order=2)
    @allure.description('预约会议接口验证-/cvoa/openapi/editMeet')
    def test_editMeet_1024(self, get_token):
        cus = int(round(time.time() * 1000))
        data = {
            "startTime": (cus - 600000 ),
            "meetId": global_meetId_1,
            "token": get_token
        }
        response = client.send_request('POST', '/cvoa/openapi/editMeet', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":1024,"message":"会议开始时间不能早于当前时间"', response_body=response['response_body'])


    @allure.story("取消会议正向请求接口")
    @allure.title("取消会议-只填写必填参数")
    @pytest.mark.run(order=2)
    @allure.description('取消会议接口验证-/cvoa/openapi/cancelMeet')
    def test_cancelMeet_0(self, get_token):
        data = {
            "meetId": global_meetId_1,
          #  "userId": "100003718219",
            "token": get_token
        }
        response = client.send_request('POST', '/cvoa/openapi/cancelMeet', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])


    @allure.story("加入会议正向请求接口")
    @allure.title("登录用户加入会议-userJoinMeet")
    @pytest.mark.run(order=2)
    @allure.description('预约会议接口验证-/cvoa/openapi/userJoinMeet')
    def test_userJoinMeet_0(self, get_token):
        data = {
            "meetId": global_meetId_2,
            "userId": "100003718219",
            "token": get_token
        }
        response = client.send_request('POST', '/cvoa/openapi/userJoinMeet', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])

    @allure.story("加入会议正向请求接口")
    @allure.title("游客加入会议-guestJoinMeet")
    @pytest.mark.run(order=2)
    @allure.description('预约会议接口验证-/cvoa/openapi/guestJoinMeet')
    def test_guestJoinMeet_0(self, get_token):
        data = {
            "name": "游客加入AAA",
            "meetId": global_meetId_2,
            "token": get_token
        }
        response = client.send_request('POST', '/cvoa/openapi/guestJoinMeet', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])

    @allure.story("加入会议正向请求接口")
    @allure.title("主持人加入会议-hostJoinMeet")
    @pytest.mark.run(order=2)
    @allure.description('预约会议接口验证-/cvoa/openapi/hostJoinMeet')
    def test_hostJoinMeet_0(self, get_token):
        data = {
            "name": "主持人BBB",
            "hostMeetLink": MeetLink,
            "token": get_token
        }
        response = client.send_request('POST', '/cvoa/openapi/hostJoinMeet', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])

    """  
        上述三个加入会议的case,执行成功,返回正常,但是在页面查看效果没有发现有用户进入到会议中   具体的原因未知,是否优化case不确定
    """

    @allure.story("日程单点登录正向请求接口")
    @allure.title("快速登录日程管理-ssoLoginMeet")
    @pytest.mark.run(order=2)
    @allure.description('日程单点登录接口验证-/cvoa/openapi/ssoLoginMeet')
    def test_ssoLoginMeet_0(self, get_token):
        data = {
            "userId": "100003718219",
            "token": get_token
        }
        response = client.send_request('POST', '/cvoa/openapi/ssoLoginMeet', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])


    @allure.story("查询云视会议正向请求接口")
    @allure.title("查询云视会议-queryMeetInfo")
    @pytest.mark.run(order=2)
    @allure.description('查询会议接口验证-/cvoa/openapi/queryMeetInfo')
    def test_queryMeetInfo_0(self, get_token):
        data = {
            "meetId": global_meetId_2,
            "token": get_token
        }
        response = client.send_request('POST', '/cvoa/openapi/queryMeetInfo', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])

    @allure.story("立即开会正向请求接口")
    @allure.title("立即开会-immediateMeetMeet")
    @pytest.mark.run(order=2)
    @allure.description('立即开会接口验证-/cvoa/openapi/immediateMeetMeet')
    def test_immediateMeetMeet_0(self, get_token):
        data = {
            "meetId": global_meetId_2,
            "token": get_token
        }
        response = client.send_request('POST', '/cvoa/openapi/immediateMeetMeet', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])


    @allure.story("取消会议做后置处置")
    @allure.title("取消会议-后置处理")
    @pytest.mark.run(order=3)
    def test_cancelMeet_1(self, get_token):
        data = {
            "meetId": global_meetId_2,
            "token": get_token
        }
        response = client.send_request('POST', '/cvoa/openapi/cancelMeet', parms_type='json', data=data)
        assert step_pack.assert_code(200, response['response_code'])
        assert step_pack.assert_in_body('"status":0,"message":"成功"', response_body=response['response_body'])

