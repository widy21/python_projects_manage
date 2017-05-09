#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
直播平台处理工具类
"""
import hashlib
import types
from lxml import etree
import os
import sys

reload(sys)
from project_manage.utils.crawl_util import CrawlUtil
from project_manage.utils.serverUtil import ServerUtil
import config as config
import logging
import logging.config

__author__ = 'hua.xiao'


class PlatUtil(object):
    def __init__(self):
        self.serverUtil = ServerUtil()
        self.crawlUtil = CrawlUtil()
        logging.config.fileConfig(sys.path[0] + '/logging.config')
        self.logger = logging.getLogger("example01")

    def get_file_name(self, upload_local_dir, type):
        for root, dirs, files in os.walk(upload_local_dir):
            for file in files:
                if (type in file):
                    return os.path.join(root, file)


    def deal_live(self):
        self.logger.debug('========deal_live============')
        self.download_live_war()
        remote_dir = '/export/sdk/hx/xx_live'

        # 上传war包
        upload_local_dir = sys.path[0] + '/upload_files'

        srcfile = self.get_file_name(upload_local_dir, 'live')
        self.logger.debug('srcfile --> ', srcfile)

        # 修改war包名称
        tofile = os.path.join(upload_local_dir, "xx-live.war")
        os.rename(srcfile, tofile)
        self.logger.debug('rename success. ')

        self.serverUtil.upload_single_file(config.host_ip, config.cn_port, config.cn_username, config.cn_password,
                                           tofile, remote_dir, "xx-live.war")
        self.logger.debug('upload war file success .')

        # 执行部署脚本
        commond = 'sh /export/sdk/hx/xx_live/deploy_live_tomcat.sh'
        result = self.serverUtil.exec_command_pwd(config.host_ip, config.cn_port, config.cn_username,
                                                  config.cn_password, commond)
        for i in result:
            self.logger.debug(i)

        if result[1] is not None and str(result[1]).strip() != '':
            self.logger.debug('deploy war file error .')
        else:
            self.logger.debug('deploy war file success .')

        return ' '.join(result)

    def deal_netty(self):
        self.logger.debug('========deal_netty============')
        self.download_netty_war()
        remote_dir = '/export/sdk/hx/xx_netty'

        # 上传war包
        upload_local_dir = sys.path[0] + '/upload_files'

        srcfile = self.get_file_name(upload_local_dir, 'chat')
        self.logger.debug('srcfile --> ', srcfile)

        # 修改war包名称
        tofile = os.path.join(upload_local_dir, "chat.war")
        os.rename(srcfile, tofile)
        self.logger.debug('rename success. ')

        self.serverUtil.upload_single_file(config.host_ip, config.cn_port, config.cn_username, config.cn_password,
                                           tofile, remote_dir, "chat.war")
        self.logger.debug('upload war file success .')

        # 执行部署脚本
        commond = 'sh /export/sdk/hx/xx_netty/deploy_netty_tomcat.sh'
        result = self.serverUtil.exec_command_pwd(config.host_ip, config.cn_port, config.cn_username,
                                                  config.cn_password, commond)
        for i in result:
            self.logger.debug(i)

        if result[1] is not None and str(result[1]).strip() != '':
            self.logger.debug('deploy war file error .')
        else:
            self.logger.debug('deploy war file success .')

        return ' '.join(result)

    def deal_bi_motan(self):
        self.logger.debug('========deal_bi_motan============')
        self.download_motan_war()
        remote_dir = '/export/sdk/hx/xx_motan'

        # 上传war包
        upload_local_dir = sys.path[0] + '/upload_files'

        srcfile = self.get_file_name(upload_local_dir, 'ROOT')
        self.logger.debug('srcfile --> ', srcfile)

        # 修改war包名称
        tofile = os.path.join(upload_local_dir, "ROOT.war")
        os.rename(srcfile, tofile)
        self.logger.debug('rename success. ')

        self.serverUtil.upload_single_file(config.host_ip, config.cn_port, config.cn_username, config.cn_password,
                                           tofile, remote_dir, "ROOT.war")
        self.logger.debug('upload war file success .')

        # 执行部署脚本
        commond = 'sh /export/sdk/hx/xx_motan/deploy_motan_tomcat.sh'
        result = self.serverUtil.exec_command_pwd(config.host_ip, config.cn_port, config.cn_username,
                                                  config.cn_password, commond)
        for i in result:
            self.logger.debug(i)

        if result[1] is not None and str(result[1]).strip() != '':
            self.logger.debug('deploy war file error .')
        else:
            self.logger.debug('deploy war file success .')

        return ' '.join(result)

    def deal_bi_admin(self):
        self.logger.debug('========deal_bi_admin============')
        self.download_admin_war()
        remote_dir = '/export/sdk/hx/xx_admin'

        # 上传war包
        upload_local_dir = sys.path[0] + '/upload_files'

        srcfile = self.get_file_name(upload_local_dir, 'ROOT')
        self.logger.debug('srcfile --> %s' % srcfile)

        # 修改war包名称
        tofile = os.path.join(upload_local_dir, "ROOT.war")
        os.rename(srcfile, tofile)
        self.logger.debug('rename success. ')

        self.serverUtil.upload_single_file(config.admin_ip, config.cn_port, config.cn_username, config.cn_password,
                                           tofile, remote_dir, "ROOT.war")
        self.logger.debug('upload war file success .')

        # 执行部署脚本
        commond = 'sh /export/sdk/hx/xx_admin/deploy_admin_tomcat.sh'
        result = self.serverUtil.exec_command_pwd(config.admin_ip, config.cn_port, config.cn_username,
                                                  config.cn_password, commond)
        for i in result:
            self.logger.debug(i)

        if result[1] is not None and str(result[1]).strip() != '':
            self.logger.debug('deploy war file error .')
        else:
            self.logger.debug('deploy war file success .')

        return ' '.join(result)

    def download_live_war(self):
        self.logger.debug('begin to download live_war...')
        # 从私服获取下载信息
        ret = self.crawlUtil.get_data(config.nexus_live_url, '')
        j = etree.XML(ret)
        relative_url = j.find('data').find('repositoryPath').text
        self.logger.debug('relative_url-->%s' % relative_url)
        download_url = 'http://10.237.181.73:8081/nexus/service/local/repositories/snapshots/content%s' % relative_url
        self.logger.debug('download_live_url-->%s' % download_url)
        down_local_dir = sys.path[0] + '/upload_files'
        tofile = os.path.join(down_local_dir, "xx-live.war")
        # 下载文件
        self.crawlUtil.download_file(download_url, tofile)
        self.logger.debug('download success...')

    def download_netty_war(self):
        self.logger.debug('begin to download netty_war...')
        ret = self.crawlUtil.get_data(config.nexus_netty_url, '')
        j = etree.XML(ret)
        relative_url = j.find('data').find('repositoryPath').text
        self.logger.debug('relative_url-->%s' % relative_url)
        download_url = 'http://10.237.181.73:8081/nexus/service/local/repositories/snapshots/content%s' % relative_url
        self.logger.debug('download_netty_url-->%s' % download_url)
        down_local_dir = sys.path[0] + '/upload_files'
        tofile = os.path.join(down_local_dir, "chat.war")
        # 下载文件
        self.crawlUtil.download_file(download_url, tofile)
        self.logger.debug('download success...')

    def download_motan_war(self):
        self.logger.debug('begin to download motan_war...')
        ret = self.crawlUtil.get_data(config.nexus_motan_url, '')
        j = etree.XML(ret)
        relative_url = j.find('data').find('repositoryPath').text
        self.logger.debug('relative_url-->%s' % relative_url)
        download_url = 'http://10.237.181.73:8081/nexus/service/local/repositories/snapshots/content%s' % relative_url
        self.logger.debug('download_motan_url-->%s' % download_url)
        down_local_dir = sys.path[0] + '/upload_files'
        tofile = os.path.join(down_local_dir, "ROOT.war")
        # 下载文件
        self.crawlUtil.download_file(download_url, tofile)
        self.logger.debug('download success...')

    def download_admin_war(self):
        self.logger.debug('begin to download admin_war...')
        ret = self.crawlUtil.get_data(config.nexus_admin_url, '')
        j = etree.XML(ret)
        relative_url = j.find('data').find('repositoryPath').text
        self.logger.debug('relative_url-->%s' % relative_url)
        download_url = 'http://10.237.181.73:8081/nexus/service/local/repositories/releases/content%s' % relative_url
        self.logger.debug('download_motan_url-->%s' % download_url)
        down_local_dir = sys.path[0] + '/upload_files'
        tofile = os.path.join(down_local_dir, "ROOT.war")
        # 下载文件
        self.crawlUtil.download_file(download_url, tofile)
        self.logger.debug('download success...')

    def getMd5Data(self,radamPassword):
        if type(radamPassword) is types.StringType:
            m = hashlib.md5()
            m.update(radamPassword)
            return m.hexdigest()
        else:
            return ''