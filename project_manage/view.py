#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import commands
import datetime
import json
import traceback
from django.http import HttpResponse
from django.shortcuts import render_to_response
from project_manage.utils.crawl_util import CrawlUtil
from utils.deal_live_plat_util import PlatUtil
import sys
import project_manage.utils.config as config
sys.setdefaultencoding("utf-8")
__author__ = 'Monkey.D.xiao'


def index(req):
    if req.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = req.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = req.META['REMOTE_ADDR']
    platUtil = PlatUtil()
    platUtil.logger.debug('ip --> %s' % ip)
    now = datetime.datetime.now()
    if(ip in ''.join(config.manager_ip)):
        show_type = 'admin'
    elif(ip in ''.join(config.sdk_ip)):
        show_type = 'sdk'
    elif(ip in ''.join(config.bi_ip)):
        show_type = 'bi'
    else:
        show_type = 'unkonwn'
    return render_to_response('index.html', {'show_type': show_type})

def show_call_live(req):
    return render_to_response('gs_callback.html')


def deploy(req):
    try:
        deploy_type = req.POST['deploy_type']
        platUtil = PlatUtil()
        if (deploy_type == '1'):
            result = platUtil.deal_live()
        elif (deploy_type == '2'):
            result = platUtil.deal_netty()
        elif (deploy_type == '3'):
            result = platUtil.deal_bi_motan()
        elif (deploy_type == '4'):
            result = platUtil.deal_bi_admin()
    except:
        platUtil.logger.error('===========deploy error===========')
        traceback.print_exc()
    return HttpResponse(json.dumps({'ret_code': '0', 'data': result}))

def call_live(req):
    try:
        deploy_type = req.POST['deploy_type']
        role_id = req.POST['role_id']
        item_id = req.POST['item_id']
        item_name = req.POST['item_name']
        appid = req.POST['appid']
        platUtil = PlatUtil()
        if (deploy_type == '1'):

            to_md5_str = str(appid+item_id+role_id+"&"+config.sign_key)
            signature = platUtil.getMd5Data(to_md5_str)
            platUtil.logger.debug('to_md5_str--->'+to_md5_str)
            platUtil.logger.debug('signature--->'+signature)
            values = {
                "role_id":role_id,
                "item_id":item_id,
                "item_name":item_name,
                "appid":appid,
                "signature":signature
            }

            crawlUtil = CrawlUtil()
            result = crawlUtil.crawl_https_text_data(config.grant_item_callback, values);
        else:
            result = '未知操作类型'
    except:
        platUtil.logger.error('===========call_live error===========')
        traceback.print_exc()
        result = '===========call_live error==========='
    return HttpResponse(json.dumps({'ret_code': '0', 'data': result}))