#coding=utf8
import itchat, time,hashlib,requests
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    apiUrl="http://www.tuling123.com/openapi/api"

    data={
        'key':"cdc9255cb280425789f158a38506b1a3",
        'info':msg['Text'],
        'userid':get_md5_value(msg['FromUserName']),
    }
    returnmsg='';
    try:
        r=requests.post(apiUrl,data=data).json()
        returnmsg=r.get('text')
    except:
        returnmsg=""
    time.sleep(3)
    itchat.send('%s' % returnmsg, msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])
def get_md5_value(src):
    myMd5=hashlib.md5()
    myMd5.update(src)
    myMd5_digest=myMd5.hexdigest()
    return myMd5_digest
itchat.auto_login(True)
itchat.run()
