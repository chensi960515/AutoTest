# -*- coding: utf-8 -*-
# @Time : 2022/5/20 17:06
# @Author : chensi
# @File : PCS_createmeeing.py
# @Project : CVATest

import requests
import json
import time
import xlrd



list_meetingId = []


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

def save_meetingID(x):
    with open('meetingID.txt', 'a', encoding='utf-8') as f:
        f.write(str(x))
        f.write("\n")
    with open('meetingID.txt', 'r', encoding='utf-8') as f:
        x = f.read()

def save_hostPasscode(z):
    with open('hostPasscode.txt', 'a', encoding='utf-8') as f:
        f.write(str(z))
        f.write("\n")
    with open('hostPasscode.txt', 'r', encoding='utf-8') as f:
        x = f.read()

s = requests.Session()

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


def create_Meeting_one(token, times, start_time, party_partyTel_0, party_partyTel_1, callOutType_custom):
    # =================================生产==================================
    # url = "https://apipcs.263.net/api/createMeeting"

    #=================================测试==================================
    url = "https://apipcstest.263.net/api/createMeeting"

    payload_client_one = json.dumps({
        "token": token,
        # =================================生产==================================
        #"userAccount": "cx@net263.com",

        #=================================测试==================================
        "userAccount": "xu.chen1@net263.com",
        "meetingTitle": "第0" + str(times) + "场" + str(party_partyTel_0),
        "startTime": start_time,
        "duration": "120",
        "partyList": [
            {
                "partyName": party_partyTel_0,
                "partyType": "0",
                "countryCode": "",
                "areaCode": "",
                "partyTel": party_partyTel_0,
                "partyEmail": "",
                "isCallOut": "1"
            },
            {
                "partyName": party_partyTel_1,
                "partyType": "1",
                "countryCode": "",
                "areaCode": "5678",
                "partyTel": party_partyTel_1,
                "partyEmail": "si.chen@net263.com",
                "isCallOut": "1"
            }
        ],
        "contactList": [
            {
                "contactName": "紧急联络人列表",
                "contactTelephone": "16621292683",
                "contactEmail": "test@net263.com"
            }
        ],
        "callOutType": callOutType_custom,
        "isRecord": "1",
        "joinType": 1,
        "meetingExplain": "预约倾听会议,类型为" + str(callOutType_custom)
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload_client_one)
    res = json.loads(response.text)
    now_meetingId = res['data']['meetingId']
    save_meetingID(now_meetingId)
    now_hostPasscode = res['data']['hostPasscode']
    save_hostPasscode(now_hostPasscode)


def create_Meeting_two(token, times, start_time, party_partyTel_0,party_partyTel_1 , party_partyTel_2 , callOutType_custom):

    # =================================生产==================================
    #url = "https://apipcs.263.net/api/createMeeting"

    # =================================测试==================================
    url = "https://apipcstest.263.net/api/createMeeting"
    payload_client_two = json.dumps({
        "token": token,
        #=================================生产==================================
        #"userAccount": "cx@net263.com",

        #=================================测试==================================
        "userAccount": "xu.chen1@net263.com",
        "meetingTitle": "第0" + str(times) + "场" + str(party_partyTel_0),
        "startTime": start_time,
        "duration": "120",
        "partyList": [
            {
                "partyName": party_partyTel_0,
                "partyType": "0",
                "countryCode": "",
                "areaCode": "",
                "partyTel": party_partyTel_0,
                "partyEmail": "",
                "isCallOut": "1"
            },
            {
                "partyName": party_partyTel_1,
                "partyType": "1",
                "countryCode": "",
                "areaCode": "5678",
                "partyTel": party_partyTel_1,
                "partyEmail": "si.chen@net263.com",
                "isCallOut": "1"
            },
            {
                "partyName": party_partyTel_2,
                "partyType": "1",
                "countryCode": "86",
                "partyTel": party_partyTel_2,
                "partyEmail": "test@net263.com",
                "isCallOut": "1"
            }
        ],
        "contactList": [
            {
                "contactName": "紧急联络人列表",
                "contactTelephone": "16621292683",
                "contactEmail": "test@net263.com"
            }
        ],
        "callOutType": callOutType_custom,
        "isRecord": "1",
        "joinType": 1,
        "meetingExplain": "预约倾听会议,类型为" + str(callOutType_custom)
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload_client_two)
    res = json.loads(response.text)
#    print(res)
    now_meetingId = res['data']['meetingId']
    save_meetingID(now_meetingId)
    now_hostPasscode = res['data']['hostPasscode']
    save_hostPasscode(now_hostPasscode)


excelFile = "D:\\263\\测试虚拟账号.xlsx"
res_guwen = read_xlrd(excelFile=excelFile, list_index=0)
res_user1 = read_xlrd(excelFile=excelFile, list_index=1)
res_user2 = read_xlrd(excelFile=excelFile, list_index=2)
res_user3 = read_xlrd(excelFile=excelFile, list_index=3)
res_false = read_xlrd(excelFile=excelFile, list_index=4)


token = get_Token()

for i in range(0, 9) :
    if i > 0 and i <= 2:
        create_Meeting_one(token=token, times=i, start_time=1653906600000, party_partyTel_0=res_guwen[i],
                           party_partyTel_1=res_user1[i], callOutType_custom='1')
    elif i > 2 and i <= 4:

        create_Meeting_two(token=token, times=i, start_time=1653906600000, party_partyTel_0=res_guwen[i],
                           party_partyTel_1=res_user1[i], party_partyTel_2=res_user2[i-2], callOutType_custom='6')
    elif i > 4 and i <= 6:
        create_Meeting_two(token=token, times=i, start_time=1653906600000, party_partyTel_0=res_guwen[i],
                           party_partyTel_1=res_user1[i], party_partyTel_2=res_false[i - 4], callOutType_custom='7')
    elif i > 6:
        create_Meeting_two(token=token, times=i, start_time=1653906600000, party_partyTel_0=res_guwen[i],
                           party_partyTel_1=res_user1[i], party_partyTel_2=res_user3[i-6], callOutType_custom='5')



