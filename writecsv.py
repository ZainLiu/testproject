# !/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import os
# 获取ｊｓｏｎ数据
import json

with open('json.txt', 'r') as f:
    rows = json.load(f)

# 创建文件对象
a = os.path.exists('data.csv')
f = open('data.csv', 'a',newline='')
# 通过文件创建csv对象py
csv_write = csv.writer(f)

# writerow: 按行写入，　writerows: 是批量写入
# 写入数据 取列表的第一行字典，用字典的ｋｅｙ值做为头行数据
if not a:
    csv_write.writerow(rows[0].keys())

# 循环里面的字典，将value作为数据写入进去
for row in rows:
    csv_write.writerow(row.values())

# 关闭打开的文件
f.close()