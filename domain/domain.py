# -*- coding:utf-8 -*-
import json
import  time
from conf.config import *

from core.make_signature import MAKE_SIGNATURE
make_signature = MAKE_SIGNATURE()

server_address = 'https://domain.aliyuncs.com'
user_params = {'Action': 'QueryDomainList', 'PageNum':1, "PageSize":1,'DomainName':'zhourui.me' }

def compose_url(user_params,parameters):
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time()))


    for key in user_params.keys():
        print 'key is %s'%(key)
        parameters[key] = user_params[key]
    signature = make_signature.compute_signature(parameters, access_key_secret)
    parameters['Signature'] = signature
    print "finally parameters is %s"%(parameters)
    url = server_address + "/?" + urllib.urlencode(parameters) #拼接最终api访问的url
    print "parameters is %s"%(parameters)
    print "url is %s"%(url)
    return url

def make_request(user_params, quiet=False):
    url = compose_url(user_params,parameters)
    request = urllib2.Request(url)
    try:
        conn = urllib2.urlopen(request)
        response = conn.read()
        print "response is %s"%(response)
    except urllib2.HTTPError, e:
        # print(e.read().strip())
        raise SystemExit(e)
    try:
        obj = json.loads(response)
        if quiet:
            return obj
    except ValueError, e:
        raise SystemExit(e)
    json.dump(obj, sys.stdout, sort_keys=True, indent=3) #输出
    # sys.stdout.write('\n')

# print sys.stdin.encoding
make_request(user_params)