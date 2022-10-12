import matplotlib.pyplot as plt  # 画图用
import numpy as np
import matplotlib
import operator
import random
import xlrd  # 读Excel数据用
import pandas as pd
import xlwt
from sklearn.datasets import load_wine

sheetname = ['0']


for i in range(1,5000):
    s = ''
    s+='./list'
    s+=str(i)
    s+='.xls'
    sheetname.append(s)


def loadxls(x):
    wine = load_wine()
    file_location = sheetname[x]
    data = xlrd.open_workbook(file_location)
    sheet = data.sheet_by_index(0)
    i = 0
    stu = []  # 存放学生名单
    while i < 90:
        stu.append([])
        stu[i].append(int(sheet.cell_value(i + 1, 1)))
        stu[i].append(sheet.cell_value(i + 1, 2))
        stu[i].append(sheet.cell_value(i + 1, 3))
        stu[i].append(int(sheet.cell_value(i + 1, 4)))
        stu[i].append(int(sheet.cell_value(i + 1, 5)))
        stu[i].append(int(sheet.cell_value(i + 1, 6)))
        stu[i].append(int(sheet.cell_value(i + 1, 7)))
        stu[i].append(int(sheet.cell_value(i + 1, 8)))
        stu[i].append(int(sheet.cell_value(i + 1, 9)))
        stu[i].append(int(sheet.cell_value(i + 1, 10)))
        stu[i].append(int(sheet.cell_value(i + 1, 11)))
        stu[i].append(int(sheet.cell_value(i + 1, 12)))
        stu[i].append(int(sheet.cell_value(i + 1, 13)))
        stu[i].append(int(sheet.cell_value(i + 1, 14)))
        stu[i].append(int(sheet.cell_value(i + 1, 15)))
        stu[i].append(int(sheet.cell_value(i + 1, 16)))
        stu[i].append(int(sheet.cell_value(i + 1, 17)))
        stu[i].append(int(sheet.cell_value(i + 1, 18)))
        stu[i].append(int(sheet.cell_value(i + 1, 19)))
        stu[i].append(int(sheet.cell_value(i + 1, 20)))
        stu[i].append(int(sheet.cell_value(i + 1, 21)))
        stu[i].append(int(sheet.cell_value(i + 1, 22)))
        stu[i].append(int(sheet.cell_value(i + 1, 23)))
        i = i + 1
    return stu


def stu_judge(absence, j):
    cnt = 0
    flag = 0
    if absence[j + 3] == 0:
        cnt = cnt + 1
        flag = 1
    if absence[j + 4] == 0:
        cnt = cnt + 1
        flag = 1
    return (flag, cnt)

def stu_judgecge(absence,j,cnt,trans_count):
    count = 0
    ecount = 0
    flag = 0
    if j + 3 < 23:
        if absence[j + 3] == 0:
            ecount = ecount + 1
            flag = 1
        count += 1
    if j + 4 < 23:
        if absence[j + 4] == 0:
            ecount = ecount + 1
            flag = 1
        count += 1
    if flag==1:
        k = 5
        cnt +=1
        trans_count += 1
        while j + k < 23:
            if absence[j+k]==0:
                ecount += 1
            count +=1
            k += 1
    return cnt,count,ecount,trans_count
def call_once(stu):
    i = 0
    j = 0  # 第j次课
    count = 0
    ecount = 0
    absense = []  # 缺勤名单 用于记录缺勤的学生
    absense_count = 0
    truance = []  # 用于记录缺席80%的课的学生
    truance_count = 0
    cnt=0
    while j < 20:
        j=j+1
        k = i
        i = i + 11
        while k < i and k < 90:
            if stu[k][j + 2] == 0:
                absense.append([])
                absense[absense_count] = stu[k]
                ecount = ecount + 1
                cnt,ccount,ec,truance_count=stu_judgecge(absense[absense_count],j,cnt,truance_count)
                absense_count = absense_count + 1
                ecount += ec
                count += ccount
            k = k + 1
        count = count + 11
        if float(truance_count / k) > float(1.9 / 90):
                break
    return (ecount,count)

sum_count = 0  # 总点名次数
sum_ecount = 0  # 总有效点名次数
for i in range(1,5000):
    stu = []
    stu = loadxls(i)
    se,sc=call_once(stu)
    stu.clear()
    sum_ecount+=se
    sum_count+=sc

print(sum_ecount)
print(sum_count)
E = sum_ecount/sum_count
print('endE=', E)