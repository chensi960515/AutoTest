# -*- coding: utf-8 -*-
# @Time : 2022/3/16 10:51
# @Author : chensi
# @File : testx.py
# @Project : CVATest
import json

import yaml
import ast
import time
import datetime
from tools import GToken

from tools import read_yaml

ya = read_yaml.GetPages()

from tools import logger
# ya = open("../config/config.yaml", 'r', encoding='UTF-8')
# cfg = ya.read()
# ya.close()
# data = yaml.safe_load(cfg)
# print(type(data))
#
# print(data['server']['testx'])



# request_body = '{"status":0,"message":"成功","responseTime":1647501944322,"host":"192.168.206.106","tag":null,"logKey":"1511ec445d3b4fe59317f1c05dd4aac2","data":{"expires":1647509144320,"token":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjdl9vcGVuYXBpIiwiY3VzdG9tZXJfaWQiOiJVMTAwMDAyNDc4OTIiLCJpYXQiOjE2NDc1MDE5NDQsImV4cCI6MTY0NzUwOTE0NH0.vzZGeSfzlJf6GKdsLVA6JRWe2eAfLuxSFp6yXwA60HI"}}'
# res = json.loads(request_body)
# print(res['data']['token'])

# res = ya.get_data_list('../config/config1.yaml')
# print(res)
#
# ya.dump_dict(res, '../config/config1.yaml')
#
res = GToken()
print(res)

"""
partyList=[
{
       "partyName": "主持人",
       "partyType": "HOST",
       "phoneNumber": "15735187091",
       "partyEmail": "1196696386@qq.com"
}
,
{
       "partyName": "参会人",
       "partyType": "GUEST",
        "phoneNumber": "",
       "partyEmail": "119669@qq.com"
}]

j = 1
z = int(9540042801)
for i in range(1,1000):
    partyList.append({"partyName": "虚拟人"+str(j),"partyType": "HOST","phoneNumber": z,"partyEmail": "xx" + str(j)+"xx@qq.com"})
    j = j+1
    z = z+1

logger.info(partyList)
"""

# print(int(round(time.time() * 1000))+1800000)

MeetId = ['11222','2333333']
print(MeetId[0])
