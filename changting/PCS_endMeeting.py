# -*- coding: utf-8 -*-
# @Time : 2022/5/30 15:35
# @Author : chensi
# @File : PCS_endMeeting.py
# @Project : CVATest

"""
    只针对 已经开启的倾听会议
    执行结束会议

"""


import requests

cookie = 'SESSION=OGU5MWNhOTUtYzE1MC00ZmZjLWI3YjUtOTFlYTEyNGQxZTRl; languageCC=zh; i18next=zh; pus=642a6e0a-4005-461f-aeaf-370fef2b016b'

test_url = "https://pcstest.263.net/meetingRoom/endMeeting/"

list_hostPasscode = []

def get_hostPasscode():
    with open('hostPasscode.txt', 'r', encoding='utf-8') as f:
        for x in f:
            list_hostPasscode.append(x[0:9])


def end_meeting(hostPasscode):
    url = test_url + str(hostPasscode)

    headers = {
        'Cookie': cookie
    }

    response = requests.request("POST", url, headers=headers)
    print(url)
    print(response.text)

get_hostPasscode()
for i in range(len(list_hostPasscode)):
    end_meeting(list_hostPasscode[i])