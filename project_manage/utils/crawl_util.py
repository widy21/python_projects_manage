#!/usr/bin/env python
# _*_ coding: utf-8 _*_

#页面爬取工具类

__author__ = 'Monkey.D.xiao'
import requests

class CrawlUtil(object):
    def __init__(self):
        self.s = requests.session()

    def login(self,login_url,login_data):
        res = self.s.post(login_url,login_data)
        return res.status_code

    def crawl_json_data(self,crawl_url,post_data):
        res = self.s.post(crawl_url,post_data)
        # print res.text
        # print res.json()
        return res.json()

    def crawl_text_data(self,crawl_url,post_data):
        res = self.s.post(crawl_url,post_data)
        # print res.text
        return res.text

    def crawl_https_text_data(self,crawl_url,post_data):
        '''
            https请求方法
            :param crawl_url:
            :param post_data:
            :return:
        '''
        header_info = {
            'Content-Type':'application/json'
        }
        res = self.s.post(crawl_url,json=post_data,headers=header_info,verify=False)
        # print res.text
        return res.text

    def get_data(self,crawl_url,request_data):
        res = self.s.get(crawl_url,params=request_data)
        # print res.content
        # return res.json()
        return res.text

    def download_file(self,download_url,file_path):
        r = requests.get(download_url)
        with open(file_path, "wb") as code:
            code.write(r.content)