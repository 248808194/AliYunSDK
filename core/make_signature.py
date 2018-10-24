#!/usr/bin/env python
#coding: utf-8
import sys,os
import urllib,urllib2
import base64
import hmac
import hashlib
from hashlib import sha1
import time
import uuid
import json
from  conf.config import *

class MAKE_SIGNATURE():

    def __init__(self):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.timestamp = timestamp
        self.parameters = parameters
        # self.server_address = 'https://domain.aliyuncs.com'
        # self.user_params = {'Action': 'QueryDomainList', 'PageNum':2, "PageSize":1 }

    def percent_encode(self,encodeStr):
        encodeStr = str(encodeStr)
        res = urllib.quote(encodeStr.decode('utf8').encode('utf8'), '')
        res = res.replace('+', '%20')
        res = res.replace('*', '%2A')
        res = res.replace('%7E', '~')
        return res

    def compute_signature(self):
        # access_key_secret = self.access_key_secret
        # parameters = self.parameters
        sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])
        canonicalizedQueryString = ''
        for (k,v) in sortedParameters:
            canonicalizedQueryString += '&' + self.percent_encode(k) + '=' + self.percent_encode(v)
        stringToSign = 'GET&%2F&' + self.percent_encode(canonicalizedQueryString[1:])
        h = hmac.new(access_key_secret + "&", stringToSign, sha1)
        signature = base64.encodestring(h.digest()).strip()
        # print "signature is %s"%(signature)
        return signature


MAKE_SIGNATURE().compute_signature()