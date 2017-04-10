#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'Monkey.D.xiao'

#国内服务器地址
host_ip = '127.0.0.1'
#端口
cn_port = 22
#用户名
cn_username = 'root'
#密码
cn_password = '123456'

#live war包maven私服地址
nexus_live_url = 'http://127.0.0.1:8080/nexus/service/local/artifact/maven/resolve?_dc=1491389885127&r=snapshots&g=com.xxx&a=live-web&v=0.0.1-SNAPSHOT&c=&e=war&isLocal=true'

#netty war包maven私服地址
nexus_netty_url = 'http://127.0.0.1:8080/nexus/service/local/artifact/maven/resolve?_dc=1491391157005&r=snapshots&g=com.xxx&a=tv-web&v=0.0.1-SNAPSHOT&c=&e=war&isLocal=true'
