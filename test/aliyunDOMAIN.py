# -*- coding:-utf8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
from aliyunsdkalidns.request.v20150109 import DescribeDomainsRequest,DescribeDomainRecordsRequest,UpdateDomainRecordRequest,AddDomainRecordRequest,DeleteDomainRecordRequest,SetDomainRecordStatusRequest
import json,urllib,re
import sys
import urllib2
import json

url = 'http://example.com/...'
values = {"q":{"has_problems": "yes"}}
data = json.dumps(values)
req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
response = urllib2.urlopen(req)
result = response.read()
print result
class DOMAIN():

    def __init__(self):
        """
        初始化数据
        传入 securityid ，securitykey region_id （地区id）
        初始化clinent
        """
        self.securityid="LTAI0uACaz2xLGMP"
        self.securitykey = "BMxBETTkXgZI1kEYTewYSpQx5bUblK"
        self.region_id = "cn-shenzhen"
        self.client = AcsClient(self.securityid,self.securitykey,self.region_id)

    def list_domain(self):
        """
        打印出当前账户域名
        :return:域名列表
        return 拿到后需要for
        DNSListJson['Domains']['Domain']
        """
        DomainList = DescribeDomainsRequest.DescribeDomainsRequest()
        DomainList.set_accept_format('json')
        DNSListJson = json.loads(self.client.do_action_with_exception(DomainList))
        DNSLIST = DNSListJson['Domains']['Domain']
        return DNSLIST

    def Add_NewDomain(self):
        pass

    def DelDomain(self):
        pass

    def ChangeDomain(self):
        pass




# a = DOMAIN().list_domain()
# print a

