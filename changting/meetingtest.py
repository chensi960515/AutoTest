# -*- coding: utf-8 -*-
# @Time : 2022/5/20 14:42
# @Author : chensi
# @File : meetingtest.py
# @Project : CVATest

import requests
import json
import time
import xlrd


def read_xlrd(excelFile, list_index):
    data = xlrd.open_workbook(excelFile)
    table1 = data.sheet_by_index(list_index)
    dataFile = []
    res = []

    for rowNum in range(table1.nrows):
        dataFile.append(table1.row_values(rowNum))

    for i in dataFile:
        if len(i[0]) > 0:
            res.append(i[0])

    return res


def get_Token():
    #  url = "https://meetapitest.263.net/meet/sec/api/getToken"       #测试API
    url = "https://meetapi.263.net/meet/sec/api/getToken"

    payload = json.dumps({
        "customerId": "U11001346548",
        "secret": "WiOroBTHdM1U6wwukO9Y7EzD927nVrhZ"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    res = json.loads(response.text)
    new_token = res['data']['token']
    return new_token


def create_Meeting(token, time_number, start_time,  phoneNumber_host, phoneNumber_guset):
    url = "https://meetapi.263.net/meet/sec/api/createMeeting"

    payload = json.dumps({
        "userAccount": "cxtest1@net263.com",
        "meetingCode": "线上预约畅听会议,第" + str(time_number) + "场",
        "token": token,
        "meetingTitle": "线上测试预约会议" + str(time.time()),
        "startTime": start_time,  # 毫秒单位
        "durationMinute": 120,
        "speaker": "主讲人test",
        "vip": "嘉宾test",
        "partyList": [
            {
                "partyName": phoneNumber_host,
                "partyType": "HOST",
                "phoneNumber": phoneNumber_host,
                "partyEmail": "263TestUser1@net263.com"
            },
            {
                "partyName": phoneNumber_guset,
                "partyType": "GUEST",
                "phoneNumber": phoneNumber_guset,
                "partyEmail": "263TestUser2@net263.com"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


excelFile = "F:\\263\\生产电话2.xlsx"
res_true = read_xlrd(excelFile=excelFile, list_index=0)

token = get_Token()

for i in range(1, 21):
    create_Meeting(token=token, time_number=i, start_time=1653416100000,  phoneNumber_host=res_true[i], phoneNumber_guset=res_true[20 + i])
