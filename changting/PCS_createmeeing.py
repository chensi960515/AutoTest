# -*- coding: utf-8 -*-
# @Time : 2022/5/20 17:06
# @Author : chensi
# @File : PCS_createmeeing.py
# @Project : CVATest

import requests
import json
import time
import xlrd


def read_xlrd(excelFile,list_index):
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
    url = "https://apipcs.263.net/api/getToken"

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


def create_Meeting_one(token,times,start_time,party_partyTel_0,party_partyTel_1,callOutType_custom):
    url = "https://apipcs.263.net/api/createMeeting"

    payload_client_one = json.dumps({
        "token": token,
        "userAccount": "cx@net263.com",
        "meetingTitle": "线上接口创建会议,第"+str(times)+"场",
        "startTime": start_time,
        "duration": "120",
        "partyList": [
            {
                "partyName": "顾问A",
                "partyType": "0",
                "countryCode": "",
                "areaCode": "",
                "partyTel": party_partyTel_0,
                "partyEmail": "",
                "isCallOut": "1"
            },
            {
                "partyName": "客户1",
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
        "meetingExplain": "预约倾听会议,类型为"+str(callOutType_custom)
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload_client_one)
    return response.text


def create_Meeting_two(token,times,start_time,party_partyTel_0,party_partyTel_1,party_partyTel_2,callOutType_custom):
    url = "https://apipcs.263.net/api/createMeeting"

    payload_client_two = json.dumps({
        "token": token,
        "userAccount": "cx@net263.com",
        "meetingTitle": "线上接口创建会议,第"+str(times)+"场",
        "startTime": start_time,
        "duration": "120",
        "partyList": [
            {
                "partyName": "顾问B",
                "partyType": "0",
                "countryCode": "",
                "areaCode": "",
                "partyTel": party_partyTel_0,
                "partyEmail": "",
                "isCallOut": "1"
            },
            {
                "partyName": "客户1",
                "partyType": "1",
                "countryCode": "",
                "areaCode": "5678",
                "partyTel": party_partyTel_1,
                "partyEmail": "si.chen@net263.com",
                "isCallOut": "1"
            },
            {
                "partyName": "客户2",
                "partyType": "1",
                "countryCode": "86",
                "partyTel": party_partyTel_2,
                "partyEmail": "test@net263.com",
                "isCallOut": "0"
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
        "meetingExplain": "预约倾听会议,类型为"+str(callOutType_custom)
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload_client_two)
    return response.text




excelFile = "D:\\263\\生产电话1.xlsx"
res_true = read_xlrd(excelFile=excelFile,list_index=0)
res_false = read_xlrd(excelFile=excelFile,list_index=1)


token = get_Token()

for i in range(0,91):
    if i > 0 and i <= 30 :
        create_Meeting_one(token = token , times= i , start_time= 1653307200000 ,party_partyTel_0 = res_true[20+i] ,party_partyTel_1=res_true[120+i] , callOutType_custom= '1')
    elif i > 30 and i<=60 :
        create_Meeting_two(token = token , times= i , start_time= 1653307200000 ,party_partyTel_0 = res_true[20+i] ,party_partyTel_1=res_true[120+i] , party_partyTel_2= res_true[210+i] ,callOutType_custom= '6')
    elif i > 60 :
        create_Meeting_two(token = token , times= i , start_time= 1653307200000 ,party_partyTel_0 = res_true[20+i] ,party_partyTel_1=res_true[120+i]  ,party_partyTel_2= res_false[i], callOutType_custom= '7')
