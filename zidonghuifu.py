# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:42:56 2019

@author: 洛林
"""
#引入itchat包
import requests
import itchat
#自动登陆（括号内参数可以保持一段时间登录状态）
itchat.auto_login()

#name = itchat.search_friends(name=u'曹培信')
#XiaoMing = name[0]["UserName"]
#message_concent = 'Hey,dude'
#itchat.send(message_concent,XiaoMing)



KEY = '440a48c5f559402ea4a0ce9a5dda7fa3'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    name=itchat.search_friends(name=u'蔡根花宝贝')
    xiaoming=name[0]["UserName"]
    
    if msg['FromUserName']==xiaoming:
        reply = get_response(msg['Text'])
        return reply or defaultReply

#itchat.auto_login(hotReload=True)
itchat.run()
itchat.logout()