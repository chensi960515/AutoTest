#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: conftest.py
@time: 2022/3/23  0:18
"""

import pytest
from tools import GToken

@pytest.fixture(scope='session')
def get_token():
    token = GToken()
    return token