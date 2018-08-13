#coding=utf-8

#以只读方式打开user.txt文件
user = open("user.txt", 'r')
#读取txt文件所有行
lines = user.readlines()
user.close()

for line in lines:
    #split()函数，以“,”分割，[0]取逗号左边，[1]取逗号右边
    username = line.split(",")[0]
    passwd = line.split(",")[1]
    print username, passwd