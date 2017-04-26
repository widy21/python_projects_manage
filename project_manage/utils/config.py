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

#sdk ip白名单
sdk_ip = ['127.0.0.1']
#bi ip白名单
bi_ip = ['127.0.0.1']
#admin ip白名单
manager_ip = ['127.0.0.1']

#语音直播调用url
grant_item_callback = 'https://xxx.com/xxx/tv/xxx'

#语音直播key
sign_key = '123'