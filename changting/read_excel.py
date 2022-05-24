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

def read_xlrd(excelFile,list_index):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(list_index)

    dataFile = []
    res = []

    # for rowNcols in range(table.ncols):
    #     for rowNum in range(table.nrows):
    #         dataFile.append(table.row_values(rowNum))

    # for cols in range(table.ncols):
    #     dataFile.append(table.col_values(cols))


    for i in dataFile:
        if len(i[0]) > 0:
            res.append(i[0])

    return res


if __name__ == '__main__':
    excelFile = "F:\\263\\接入号.xlsx"
    res = read_xlrd(excelFile=excelFile,list_index=0)
    res2 =read_xlrd(excelFile=excelFile,list_index=2)
    print(res)
    print(len(res))
    print(res2)
    print(len(res2))