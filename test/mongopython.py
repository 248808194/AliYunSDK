# -*- coding=utf8 -*-
from pymongo import MongoClient
from time_recovery import time_recovery
from statistics import mean, median
import datetime
# T = time_recovery()
# aa = T.timestamp_datetime(1540212316536)
import pprint
client  = MongoClient('10.61.100.166',27017) #连接到MongoDB
db = client.data_platform #连接到具体的数据库
T = time_recovery()
collection = db.statistics



all_last_day_date = [] #前一天的所有数据放到一个空列表里。

for i in collection.find(): #循环拿到上一天的数据
    for k,v in i.items():
        if k == 'start_time':
            start_day_time = T.timestamp_datetime(v)
            last_day =  str(datetime.date.today() - datetime.timedelta(days=1))
            if start_day_time == last_day:
                all_last_day_date.append(i)
        else:
            continue
# print('当天pv 为%s'%(len(all_last_day_date)))
all_user = set()
all_sessonid = set()
all_ip = set()

for i in all_last_day_date:
    all_user.add(i['uuid'])
    all_sessonid.add(i['sessionID'])
print('当天独立访客数为%s'%(len(all_user)))
print('当天访问次数为%s'%(len(all_sessonid)))

a=0
bb=[]
for i in all_last_day_date:
    for ii in all_sessonid:
        if ii == i['sessionID']:
            b=len(i['history_url'])
            if b > a:
                a=b
            else:
                continue
        bb.append(a)

# print(bb)
print("当天pv %s"%(sum(bb)))

single_seesion_max_time = {}
# print('-----'*10)
# for i in all_last_day_date:
#     for ii in all_sessonid:
#         if i['sessionID'] == ii:
#             single_seesion_max_time[ii] = []


bbb =[]
for i in all_last_day_date:
    for ii in all_sessonid:
        if i['sessionID'] == ii:
            single_session_time = i['end_time'] - i['start_time']
            single_session_time = single_session_time / 1000 #转换为秒
            bbb.append(single_session_time)

print(mean(bbb))
# for k,v in single_seesion_max_time.items():
#     print('sessionid %s 平均访问时长 %s'%(k,max(v)))


