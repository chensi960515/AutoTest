# -*- coding: utf-8 -*-
# @Time : 2022/5/30 17:44
# @Author : chensi
# @File : PCS_cancelMeeting.py
# @Project : CVATest

"""
    只针对未开启或者已经过期的倾听会议
    取消会议

"""
import requests
import json


list_meetingId = []
url_v = "https://apipcstest.263.net/api/cancelMeeting"

userAccount = "xu.chen1@net263.com"


def get_Token():
    #=================================生产==================================
    #url = "https://apipcs.263.net/api/getToken"

    #=================================测试==================================
    url = "https://apipcstest.263.net/api/getToken"

    payload = json.dumps({
        # =================================生产==================================
        # "customerId": "U11001346548",
        # "secret": "WiOroBTHdM1U6wwukO9Y7EzD927nVrhZ"

        #=================================测试==================================
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

def get_meetingId():
    with open('meetingID.txt', 'r', encoding='utf-8') as f:
        for x in f:
            list_meetingId.append(x[0:4])

def delete_Meeting(meetingId):
    url = url_v

    payload = json.dumps({
        "token": token,
        "userAccount": userAccount,
        "meetingId": meetingId
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

token = get_Token()
get_meetingId()

for i in range(len(list_meetingId)):
    delete_Meeting(list_meetingId[i])
    print(list_meetingId[i])