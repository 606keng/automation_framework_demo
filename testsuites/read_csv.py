#coding=utf-8
import csv

#读取csv文件
dates = csv.reader(open("user.csv", "r"))

for date in dates:
    print date
    print date[0]

