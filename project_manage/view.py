#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import commands
import datetime
import json
import traceback
from django.http import HttpResponse
from django.shortcuts import render_to_response
from utils.deal_live_plat_util import PlatUtil
import sys
sys.setdefaultencoding("utf-8")
__author__ = 'Monkey.D.xiao'

def index(req):
    now = datetime.datetime.now()
    return render_to_response('index.html',{'current_date':now})

def deploy(req):
    try:
        deploy_type = req.POST['deploy_type']
        platUtil = PlatUtil()
        if(deploy_type == '1'):
            result = platUtil.deal_live()
        elif(deploy_type == '2'):
            result = platUtil.deal_netty()
    except:
        platUtil.logger.error('===========deploy error===========')
        traceback.print_exc()
    return HttpResponse(json.dumps({'ret_code':'0','data':result}))