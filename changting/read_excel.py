#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: read_excel.py
@time: 2022/5/22  16:37
"""
#
# import xlrd
#
# excel_path = "C:\\Users\\FLCL\\Documents\\263EM\\si.chen@net263.com\\receive_file\\接入号.xlsx"


import xlrd

def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    res = []

    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

    for i in dataFile:
        res.append(i[0])

    return res


if __name__ == '__main__':
    excelFile = "F:\\263\\虚拟电话.xlsx"
    res = read_xlrd(excelFile=excelFile)
    print(read_xlrd(excelFile))