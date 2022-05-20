# -*- coding: utf-8 -*-
# @Time : 2022/5/20 17:06
# @Author : chensi
# @File : PCS_createmeeing.py
# @Project : CVATest

import requests
import json
import time


def get_Token():
    url = "https://apipcstest.263.net/api/getToken"

    payload = json.dumps({
        "customerId": "U10000247885",
        "secret": "123456"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    res = json.loads(response.text)
    new_token = res['data']['token']
    return new_token


token = get_Token()


def create_Meeting():
    url = "https://apipcstest.263.net/api/createMeeting"

    payload = json.dumps({
        "token": "bdce13021f854dffab93566536702d06",
        "tag": "ejhk9t23O1o4",
        "userAccount": "xu.chen1@net263.com",
        "meetingTitle": "验证接口创建会议33333",
        "startTime": "",
        "duration": "100",
        "partyList": [
            {
                "partyName": "顾问1",
                "partyType": "0",
                "countryCode": "",
                "areaCode": "",
                "partyTel": "13716803858",
                "partyEmail": "",
                "isCallOut": "1"
            },
            {
                "partyName": "客户1",
                "partyType": "1",
                "countryCode": "",
                "areaCode": "5678",
                "partyTel": "15101583292",
                "partyEmail": "cuili.yin@net263.com",
                "isCallOut": "1"
            },
            {
                "partyName": "客户2",
                "partyType": "1",
                "countryCode": "86",
                "partyTel": "19924060263",
                "partyEmail": "cuili.yin@net263.com",
                "isCallOut": "0"
            },
            {
                "partyName": "客户1",
                "partyType": "1",
                "countryCode": "",
                "areaCode": "5678",
                "partyTel": "18401454963",
                "partyEmail": "cuili.yin@net263.com",
                "isCallOut": "0"
            }
        ],
        "contactList": [
            {
                "contactName": "测试",
                "contactTelephone": "17782320290",
                "contactEmail": "119669@net263.com"
            }
        ],
        "callOutType": "5",
        "isRecord": "1",
        "joinType": 1,
        "meetingExplain": "接口预约第6测试"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

