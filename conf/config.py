#!/usr/bin/env python
#coding: utf-8

import time
import uuid
access_key_id = 'LTAIOgTV3xSHMLuh'
access_key_secret = '123'
timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time()))
parameters = {
    'Format': 'JSON',
    'Version': '2018-01-29',
    'AccessKeyId': access_key_id,
    'SignatureVersion': '1.0',
    'SignatureMethod': 'HMAC-SHA1',
    'SignatureNonce': str(uuid.uuid1()),  # 基于时间戳生成唯一的UUID
    'RegionId': 'cn-hangzhou',
    'Timestamp': timestamp
}
