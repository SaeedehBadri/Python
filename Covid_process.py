# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 22:15:51 2021

@author: saeedeh
"""
#A1
import csv
from matplotlib import pyplot
filename = "Characteristics.csv" 
all_data = []
with open(filename, 'r') as f:
    line = csv.reader(f)
    for i in line:
        all_data.append(i)
header = all_data[2]
data = all_data[3:1649]
data_age = {}
for i in data:
    if i[0] == 'Age' and i[2] == 'Sex':
        if i[1] not in data_age.keys():
            data_age.setdefault(i[1],int(i[4]))
        else: 
            data_age[i[1]] = data_age[i[1]] + int(i[4])
#A2
age_list = []
for i in data_age.keys():
    if i != 'Overall':
        age_list = age_list + data_age[i]*[i]
pyplot.hist(age_list)
pyplot.show()
#A3
data_month_age = {}
for i in data:
    if i[0] == 'Month' and i[2] == 'Age':
        if i[1] not in data_month_age.keys():
            data_month_age.setdefault(i[1],{i[3]:float(i[5])})
        else:
            if i[3] not in data_month_age[i[1]].keys():
                data_month_age[i[1]].setdefault(i[3],float(i[5]))
month_age_list1 = []
month_list1 = []
selected_age1 = '18-49 yr'
for i in data_month_age.keys():
    month_list1.append(i)
    for j in data_month_age[i].keys():
        if j == selected_age1:
            month_age_list1.append(data_month_age[i][j])
month_age_list2 = []
month_list2 = []
selected_age2 = '50-64 yr'
for i in data_month_age.keys():
    month_list2.append(i)
    for j in data_month_age[i].keys():
        if j == selected_age2:
            month_age_list2.append(data_month_age[i][j])

pyplot.plot(month_list1, month_age_list1, month_list2, month_age_list2)
pyplot.legend((selected_age1, selected_age2),
           loc='upper center')
new_x = [j for i,j in enumerate(month_list1) if i%3 == 0]
pyplot.xticks(new_x)
pyplot.show()