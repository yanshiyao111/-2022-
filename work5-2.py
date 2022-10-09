import matplotlib.pyplot as plt  #画图用
import numpy as np
import matplotlib
import operator
import random
import xlrd  				#读Excel数据用
import pandas as pd
import xlwt
from sklearn.datasets import load_wine
wine = load_wine()
file_location = "./list20.xls"
data = xlrd.open_workbook(file_location)
sheet = data.sheet_by_index(0)

county = 0
countx = 0
k = 0 #存放第几次点名
stu=[] #存放学生名单
sum = 0 #总共点名次数
count = 0 #总共有效点名次数
count1 = 0 #num1中的人数
num1 = [] #暂时存放预选学生名单
numall = [] #专门点名学生名单
countall = 0 #专门点名学生名单人数
flagcge = 0
out_to = 1
# 0 0 0 0 0
# 0 1 0 0 0
# 0 1 1 0 0
# 0 1 1 1 0
# 0 1 1 1 1
def judge_stu(input_stu):
    global  k
    global  sum
    global  count
    global countall
    global flagcge
    global num1
    global count1
    global countx
    global  county
    global countj
    sum = sum + 4
    i = 0;flag = 0
    while i < 4:
        if input_stu[k+i+3]==0:
            flag = flag + 1
        i = i + 1
    # print(k)
    # print('这次的flag是：')
    # print(flag)
    if flag>=2 :
        numall.append(input_stu)
        countall = countall + 1
    else :
        countx = countx - 1
        county = county + 1
        countj = countj + 1
    flagcge =  1
    count = count + flag



i=0
while i<90:
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
    i=i+1
# 打印学生
# i=0
# while i<91:
#     print(stu[i])
#     i=i+1
countn = 0
countj = count1
countx = 0
while k < 20:
    i = countn*10
    while i < countn*10+10 and i < 90:
        if stu[i][k+3]==0:
            num1.append([])
            num1[count1]=stu[i]
            count1 = count1 + 1
            countx = countx + 1
            count = count + 1
        sum = sum + 1
        i = i + 1
    # print('count01=', count)
    # print('countx=',countx)
    # print('i=',i)
    if i!=90 and float(countx/i) > 6.7/90:
        j = countj
        # print('k=',k,'调试中的count1=',count1)
        # print('调试中的countx=', countx)
        while j < count1:
            judge_stu(num1[j])
            j = j + 1
        if flagcge == 1:
            # print('做了这一步')
            k = k + 4
            # print('k=',k)
            flagcge = 0
        if float(countall/i) > 5.2/90:
            break
    if i==90 :
        j = county
        while j < count1:
            judge_stu(num1[j])
            j = j + 1
        k = k + 4
        break
    k = k + 1
    countn = countn + 1
# print('k=',k)
# print('sum=',sum)
i = 0
while i<countall:
    j=k
    while j<20:
        if numall[i][j+3]==0 :
            count = count + 1
        sum = sum + 1
        j = j + 1
    i = i + 1

# print('黑名单成员有：')
# m=0
# while m<countall:
#     print(numall[m])
#     m = m + 1

print(count)
print(sum)
E = count/sum
print('E=',E)

# print(count1)
# print(countall)

# print('暂存名单有：')
# m = 0
# while m <count1:
#     print(num1[m])
#     m = m + 1