# -*- coding: utf-8 -*-
# @Time : 2022/5/20 14:42
# @Author : chensi
# @File : meetingtest.py
# @Project : CVATest

import requests
import json
import time



def get_Token():
        url = "https://meetapitest.263.net/meet/sec/api/getToken"

        payload = json.dumps({
          "customerId": "U10000247885",
          "secret": "123456"
        })
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        res = json.loads(response.text)
        new_token  = res['data']['token']
        return new_token

token = get_Token()

def create_Meeting():
        url = "https://meetapitest.263.net/meet/sec/api/createMeeting"

        payload = json.dumps({
                "userAccount": "xu.chen1@net263.com",
                "meetingCode": "test"+str(time.time()),
                "token": token,
                "meetingTitle": "测试预约会议"+str(time.time()),
                "startTime": 1653209013000,    #毫秒单位
                "durationMinute": 120,
                "speaker": "主讲人222",
                "vip": "嘉宾222",
                "partyList": [
                        {
                                "partyName": "主持人",
                                "partyType": "HOST",
                                "phoneNumber": "16621292683",
                                "partyEmail": "263TestUser1@net263.com"
                        },
                        {
                                "partyName": "测试用户01",
                                "partyType": "GUEST",
                                "phoneNumber": "13823531653",
                                "partyEmail": "263TestUser2@net263.com"
                        }
                ]
        })
        headers = {
                'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

print(create_Meeting())