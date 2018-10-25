# -*- coding=utf8 -*-
from pymongo import MongoClient
from time_recovery import time_recovery
from statistics import mean, median
import datetime
# T = time_recovery()
# aa = T.timestamp_datetime(1540212316536)
import pprint

username = "prod_glowworm"
password = "Rf3WjnGo7@!12MY8XVYod3JvkQidxo"
host = "dds-uf61b0cb7d8b0ab433270.mongodb.rds.aliyuncs.com"
port = "3717"
url = 'mongodb://%s:%s@%s:%s' % (username, password, host, port)
client = MongoClient('10.61.100.166', 27017)  # 连接到MongoDB
db = client.data_platform  # 连接到具体的数据库
T = time_recovery()
collection = db.statistics
# print(datetime(2018,10,22))
# exit()
# aaa = collection.find({"start_time":{'$gte':datetime(2018,10,22)}})


all_last_day_date = []  # 前一天的所有数据放到一个空列表里。
import time

last_day = str(datetime.date.today() - datetime.timedelta(days=1))
today = str(datetime.date.today())
ts = time.strptime(last_day, "%Y-%m-%d")
ts1 = time.strptime(today, "%Y-%m-%d")
tt = int(time.mktime(ts)) * 1000
tt1 = int(time.mktime(ts1)) * 1000
print("today %s ->%s lastday %s -> %s")%(today,tt,last_day,tt1)
exit()
# print(tt,tt1)
# collection.find({"start_time":{'$gte':tt,'lt':tt1}})
# aaa  = collection.find().count()
# print(aaa)
# exit()
# aaa = collection.find({"start_time":{'$gte':tt,'$lt':tt1}}).count()
# print(aaa)
#
# exit()
for i in collection.find({"start_time": {'$gte': tt, '$lt': tt1}}):  # 循环拿到上一天的数据
    for k, v in i.items():
        print(k, v)
        if k == 'start_time':
            all_last_day_date.append(i)
            # start_day_time = T.timestamp_datetime(v)
            #
            # last_day =  str(datetime.date.today() - datetime.timedelta(days=1))
            # print(last_day,start_day_time)
            # # last_day_unix = T.datetime
            # if start_day_time == last_day:
            #     all_last_day_date.append(i)
        else:
            continue

# print('当天pv 为%s'%(len(all_last_day_date)))
all_user = set()
all_sessonid = set()
all_ip = set()

for i in all_last_day_date:
    all_user.add(i['uuid'])
    all_sessonid.add(i['sessionID'])
print('当天独立访客数为%s' % (len(all_user)))
print('当天访问次数为%s' % (len(all_sessonid)))

a = 0
bb = {}
for ii in all_sessonid:
    bb[ii] = 0

print(bb)

for i in all_last_day_date:
    sessionid_ = i['sessionID']
    lenb = len(i['history_url'])
    if bb[sessionid_] < lenb:
        bb[sessionid_] = lenb
    else:
        continue

print("当天pv %s" % (print(sum(bb.values()))))

single_seesion_max_time = {}
# print('-----'*10)
# for i in all_last_day_date:
#     for ii in all_sessonid:
#         if i['sessionID'] == ii:
#             single_seesion_max_time[ii] = []


bbb = []
for i in all_last_day_date:
    for ii in all_sessonid:
        if i['sessionID'] == ii:
            single_session_time = i['end_time'] - i['start_time']
            single_session_time = single_session_time / 1000  # 转换为秒
            bbb.append(single_session_time)

# print(mean(bbb))
# for k,v in single_seesion_max_time.items():
#     print('sessionid %s 平均访问时长 %s'%(k,max(v)))
