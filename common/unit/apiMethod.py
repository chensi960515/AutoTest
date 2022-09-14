# -*- coding: utf-8 -*-
# @Time : 2022/7/19 16:03
# @Author : chensi
# @File : apiMethod.py
# @Project : CVATest

""" 接口基础方法 """

import os
import json
import logging
import random
import requests
import simplejson
from requests_toolbelt import MultipartEncoder
from config import API_CONFIG, PROJECT_NAME
from common.utils.readYaml import write_yaml_data, read_yaml_data


def get(headers, address, data, timeout=8, cookies=None):
    """
    get请求
    :param headers:
    :param address:
    :param data:
    :param timeout:
    :param cookies:
    :return:
    """

    response = requests.get(headers=headers, url=address, params=data, timeout=timeout, cookies=cookies, verify=False)
    if response.status_code == 301:
        response = requests.get(url=response.headers["location"], verify=False)

    try:
        return response.status_code, response.json()
    except json.decoder.JSONDecodeError:
        return response.status_code, None
    except simplejson.error.JSONDecodeError:
        return response.status_code, None
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise


def post(headers, address, mime_type, timeout=8, data=None, files=None, params=None, cookies=None):
    """
    post请求,具体的请求体内部进行处理分类
    :param headers:
    :param address:
    :param mime_type:   请求参数格式  根据此参数对请求体进行区分
    :param timeout:
    :param data:
    :param files:   form-data请求方式需要使用files参数
    :param params:
    :param cookies:
    :return:
    """

    # 判断请求参数类型
    if 'form_data' in mime_type:
        for key in files:
            value = files[key]
            # 判断参数值是否为文件,如果是文件则替换为二进制
            if '/' in value:
                files[key] = (os.path.basename(value)), open((value, 'rb'))
        enc = MultipartEncoder(
            fields=files,
            boundary='-------------------' + str(random.randint(1e28, 1e29 - 1))
        )

        headers['Content-Type'] = enc.content.type
        response = requests.post(url=address, data=enc, headers=headers, timeout=timeout, coookies=cookies,
                                 params=params, verify=False)
    elif 'application/json' in mime_type:
        response = requests.post(url=address, headers=headers, timeout=timeout, cookies=cookies, files=files,
                                 params=params, verify=False)
    else:
        response = requests.post(url=address, json=data, headers=headers, timeout=timeout, files=files, params=params,
                                 cookies=cookies, verify=False)

    try:
        if response.status_code != 200:
            return response.status_code, response.text
        else:
            return response.status_code, response.json()
    except json.decoder.JSONDecodeError:
        return response.status_code, None
    except simplejson.errors.JSONDecodeError:
        return response.status_code, None
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise


def put(headers, address, mime_type, timeout, data=None, files=None, params=None, cookies=None):
    """

    :param headers:
    :param address:
    :param mime_type:  请求参数格式（form_data,raw）
    :param timeout:
    :param data:
    :param files:
    :param params:
    :param cookies:
    :return:
    """
    if mime_type == 'raw':
        data = json.dumps(data)
    elif mime_type == 'application/json':
        data = json.dumps(data)
    response = requests.put(url=address,
                            data=data,
                            headers=headers,
                            timeout=timeout,
                            files=files,
                            cookies=cookies,
                            verify=False)
    try:
        return response.status_code, response.json()
    except json.decoder.JSONDecodeError:
        return response.status_code, None
    except simplejson.errors.JSONDecodeError:
        return response.status_code, None
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise


def delete(headers, address, data, timeout=8, cookies=None):
    """
    delete请求
    :param headers: 请求头
    :param address: 请求地址
    :param data: 请求参数
    :param timeout: 超时时间
    :param cookies:
    :return:
    """
    response = requests.delete(url=address,
                               params=data,
                               headers=headers,
                               timeout=timeout,
                               cookies=cookies,
                               verify=False)
    try:
        return response.status_code, response.json()
    except json.decoder.JSONDecodeError:
        return response.status_code, None
    except simplejson.errors.JSONDecodeError:
        return response.status_code, None
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise


def save_cookie(headers, address, mine_type, time_out=8, data=None, files=None, cookies=None):
    """
    保存cookie信息
    :param headers: 请求头
    :param address: 请求地址
    :param mine_type: 请求类型,用于区分参数格式(form_data,raw)
    :param time_out: 超时时间
    :param data:  请求参数
    :param files: 文件路径
    :param cookies:
    :return:
    """

    if 'data' in mine_type:
        response = requests.post(url=address, data=data, headers=headers, timeout=time_out, files=files, cookies=cookies, verify=False)
    else:
        response = requests.post(url=address, json=data, headers=headers, timeout=time_out, files=files, cookies=cookies, verify=False)

    try:
        cookies = response.cookies.get_dict()
        # 读取api配置并且写入最新的cookie信息
        aconfig = read_yaml_data(API_CONFIG)
        aconfig[PROJECT_NAME]['cookies'] = cookies
        write_yaml_data(API_CONFIG, aconfig)
        logging.debug("cookies已保存,结果为: {}".format(cookies))
    except json.decoder.JSONDecodeError:
        return response.status_code, None
    except simplejson.errors.JSONDecodeError:
        return response.status_code, None
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise