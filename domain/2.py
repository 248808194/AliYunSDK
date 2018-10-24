#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from core import make_signature
from conf.config import *
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json


class Domain():

    def __init__(self,action_name,domain_name):
        self.domain_name = domain_name
        self.action_name = action_name
        self.client = AcsClient(access_key_id, access_key_secret, parameters['RegionId'])
        self.request = CommonRequest()
        self.request.set_accept_format('json')
        self.request.set_domain('alidns.aliyuncs.com')
        self.request.set_method('POST')
        self.request.set_version('2015-01-09')
        self.request.set_action_name(self.action_name)


    def add_domain(self,record,ipaddr,type="a"):
        """
        添加域名函数
        :param record: 域名前缀
        :param ipaddr: 服务器ip
        :param signature:  唯一签名
        :param type: 类型 A，CNAME,MX 等
        :return: 失败return False 成功 return 相应字符串
        """

        if self.action_name == "AddDomainRecord":
            signature = make_signature.MAKE_SIGNATURE().compute_signature()
            self.request.add_query_param('DomainName', self.domain_name)
            self.request.add_query_param('RR', record)
            self.request.add_query_param('Type', type)
            self.request.add_query_param('Value', ipaddr)
            self.request.add_query_param('Signature', signature)
            try:
                response = self.client.do_action_with_exception(self.request)
            except Exception as e:
                print e
                return False
            return response

    def DescribeDomainRecords(self,RR): #查询具体域名ID，状态
        signature = make_signature.MAKE_SIGNATURE().compute_signature()
        self.request.add_query_param('Signature', signature)
        self.request.add_query_param('DomainName',self.domain_name)
        self.request.add_query_param('RRKeyWord', RR)
        try:
            response = self.client.do_action_with_exception(self.request)
        except Exception as e:
            print e
            return False
        detail_dict = json.loads(response)['DomainRecords']['Record'][0]
        return detail_dict

    def Search_domain(self):
        pass

    def Change_domain(self):
        pass

    def Del_Domain(self):
        pass

# a=Domain('DescribeDomainRecords','renliwo.com').DescribeDomainRecords('zttests')
a=Domain('AddDomainRecord','wowoohr.net').add_domain('glowworm-uat','106.14.117.167')
# print a['RecordId']
# for k,v in a.items():
#     print "%s<----->%s"%(k,v)










