# -*- coding:utf-8 -*-
import os

pathIsm = "/mnt/d/co/p6/mips/res.txt"   # 将res.txt前的路径改为你搭建的cpu的工程路径
pathMars = "log.txt"

ise_log = []
mars_log = []

with open(pathMars, "r") as file:
    str = file.readline()
    while str is not None and str != "":
        if str[0] == "@":
            mars_log.append(str)
        str = file.readline()

with open(pathIsm, "r") as file:
    str = file.readline()
    while str is not None and str != "":
        for i in range(len(str)):
            if str[i] == "@":
                ise_log.append(str[i:])
                break
        str = file.readline()

length = min(len(mars_log), len(ise_log))

def cmp(i):
    fail=1
    if ise_log[i] == mars_log[i]:
        fail=0
    if mars_log[i][11] == '*' and i>0 and ise_log[i] == mars_log[i-1]:
        fail=0
    if ise_log[i][11] == '*' and i<length-1 and ise_log[i] == mars_log[i+1]:
        fail=0
    return fail

with open("compare.txt", "w") as file:
    flag = 0
    for i in range(length - 1):
        fail=cmp(i)
        if fail:
            print("We expect %s, but we got %s" % (mars_log[i], ise_log[i]))
            file.write("We expect %s, but we got %s\n" % (mars_log[i], ise_log[i]))
            flag = 1

    if flag == 0:
        file.write("valid logNum:%d\nwe find no bug in this epoch!" % length)

