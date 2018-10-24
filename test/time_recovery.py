# coding=utf-8
# File Name：     time_recovery
# Author :       zhoutao
# date：          2018/10/23    14:15

import time
import datetime
class time_recovery():

    def timestamp_datetime(self,value):
        format = '%Y-%m-%d' #format格式
        value = value / 1000 #传入的是毫秒级，需要 转换为秒级
        value = time.localtime(value)
        # value为传入的值为时间戳(整形)，如：1332888820
        ## 经过localtime转换后变成
        ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
        # 最后再经过strftime函数转换为正常日期格式。
        dt = time.strftime(format, value) #格式化时间为 %Y-%m-%d
        return dt

    def datetime_timestamp(self,dt):
        # dt为字符串
        # 中间过程，一般都需要将字符串转化为时间数组
        time.strptime(dt, '%Y-%m-%d %H:%M:%S.%f')
        ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
        # 将"2012-03-28 06:53:40"转化为时间戳
        s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S.%f'))
        return int(s)

# T = time_recovery()
# T.timestamp_datetime(1540212316536)
# if __name__ == '__main__':
#     T = time_recovery()
#     # d = T.datetime_timestamp('2012-03-28 06:53:40')
#     # print(d)
#     s = T.timestamp_datetime(1540212316536)
#     print(s)