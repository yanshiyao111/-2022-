import matplotlib.pyplot as plt  # 画图用
import numpy as np
import matplotlib
import operator
import random
import xlrd  # 读Excel数据用
import pandas as pd
import xlwt
from sklearn.datasets import load_wine;

for iasd in range(1, 6):


    wine = load_wine()



    file_location = "database.xls"
    data = xlrd.open_workbook(file_location)
    sheet = data.sheet_by_index(0)
    # 引入文件


    i = 0
    stu = []
    # print(sheet.cell_value(i+2,1))
    while i < 90:
        stu.append([])
        sno = int(sheet.cell_value(i + 2, 0))
        stu[i].append(sno)
        stu[i].append(sheet.cell_value(i + 2, 1))
        stu[i].append(sheet.cell_value(i + 2, 2))
        i = i + 1
    # i=0
    # while i<91:
    #     print(stu[i])
    #     i=i+1
    # 打印学生列表
    # 将文件中的信息录入对象

    Frequent = random.randint(5, 8)
    # print("Frequent的值为：")
    # print(Frequent)
    # Ocassion = random.randint(0,3)
    # 设置frequent和ocassion随机数

    # i=0
    # while i<91:
    #     print(stu[i])
    #     i=i+1
    # 打印学生列表


    i = 0
    num1 = []
    num2 = []
    num3 = []
    while i < (Frequent):
        temp = random.randint(0, 89)
        x = 0
        while x < i:
            if (num1[x] == temp):
                break
            x = x + 1
        if (x < i):
            continue
        num1.append(temp)
        # print(num[i])
        i = i + 1

    # while i<Frequent:
    #     temp=random.randint(0,90)
    #     x=0
    #     while x<i:
    #         if(num1[x]==temp):
    #             break
    #         x=x+1
    #     if(x<i):
    #         continue
    #     num1.append(temp)
    #     # print(num[i])
    #     i=i+1
    # 找出frequent学生学生


    i = 0
    # while i<Frequent:
    #     print(num1[i])
    #     i=i+1
    # 打印被选为frequent的学生


    i = 0
    while i < 20:
        j = 0
        Ocassion = random.randint(0, 3)
        # print(f'{i}Ocassion的值为：')
        # print(Ocassion)
        while j < Ocassion:
            temp = random.randint(0, 89)
            # print(f'{i}:{j}:{temp}')
            x = 0;
            count = 0
            while x < Frequent:
                if (num1[x] == temp):
                    break
                x = x + 1
                count = count + 1
            x = 0
            while x < j:
                if (num2[x] == temp):
                    break
                x = x + 1
                count = count + 1
            if (count < Frequent + j):
                continue
            num2.append(temp)
            # print(num2)
            j = j + 1
        x = 0;
        y = 0
        while x < Frequent:
            stu[num1[x]].append(0)
            x = x + 1
        # 这个后面要改过，加入概率缺课
        while y < Ocassion:
            stu[num2[y]].append(0)
            y = y + 1

        k = 0
        while k < 90:
            x = 0;
            y = 0;
            flag = 0;
            while x < Frequent:
                if (k != num1[x]):
                    flag = flag + 1
                x = x + 1
            while y < Ocassion:
                if (k != num2[y]):
                    flag = flag + 1
                y = y + 1
            if (flag == Frequent + Ocassion):
                stu[k].append(1)
            k = k + 1

        m = 0
        for m in reversed(range(len(num2))):
            del num2[m]
        i = i + 1

    i = 0
    while i < Frequent:

        j = 0
        while j < 4:
            temp = random.randint(3, 22)
            count = 0
            x = 0
            while x < j:
                if (num3[x] == temp):
                    break
                x = x + 1
                count = count + 1
            if (count < j):
                continue
            num3.append(temp)
            stu[num1[i]][temp] = 1
            j = j + 1
        m = 0
        for m in reversed(range(len(num3))):
            del num3[m]
        i = i + 1

    # 修改经常缺课同学的数据，满足随机四次到课
    i = 0
    while i < 90:
        print(stu[i])
        i = i + 1
    #     # # 打印学生
    #
    #
    # x=0
    # y=0
    # print("以下是经常缺课的学生")
    # while x<Frequent:
    #     print(stu[num1[x]])
    #     x=x+1
    # print("以下是该堂课缺课的学生")
    # while y<Ocassion:
    #     print(stu[num2[y]])
    #     y=y+1

    # 选择Ocassion的学生


    # k=0
    # while k<Ocassion:
    #     print(num2[k])
    #     k=k+1
    # 查看Ocassion的学生
    if __name__ == '__main__':
            s=''
            s += 'list'
            s += str(iasd)
            s += '.xls'
            dataframe = pd.DataFrame(stu)
            print(dataframe)
            dataframe.to_excel(s)
