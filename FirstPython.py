#!/usr/bin/python
# -*- coding: UTF-8 -*-
print 'hello, world'
# '''可以以,分开,输入显示空格'''
# """这里是注释"""
print 'hello', 'world'
# '''加法'''
print 100 + 100
print '100+200=', 100 + 200

num1=123
print num1
num1='1234'
print num1
# '''输入输出'''
# print '请输入您的名字:'
# name = raw_input();
# print "您的名字是:", name
"""True False"""
# age = int(raw_input("请输入您的年龄:"));
# if int(age) > 30:
#     print name, "您都30多了还瞎玩呢"
# elif int(age) > 18:
#     print name, "您还不到30,别光玩了"
# else:
#     print name, "您还是个小孩儿,赶紧玩吧"
# """IF ELSE"""
# '''可变list 以中括号'''
names=['曹操','大乔','小乔']

for index in range(len(names)):
    print '第',index,'个人是:',names[index];
names.append('周瑜')
names.insert(0, '黄盖')
print '''最后追加周瑜,追加黄盖到第一个'''
for index in range(len(names)):
    print '第',index,'个人是:',names[index];
print'删除末尾'
names.pop()
for index in range(len(names)):
    print '第',index,'个人是:',names[index];
print'删除第二个'
names.pop(1)
for index in range(len(names)):
    print '第',index,'个人是:',names[index];
'''长度'''
print  'list总长度是:',len(names)
'''不可变lsit'''
pnames=('诸葛亮','刘备','关羽')
print pnames
num1=12345
print num1
# '''ASCII编码解码'''
print ord('A') #ASCII 值
print chr(65) #获取对应的字符
# print '汉字'
print u'\u4e2d'
utf8test=u'\u4e2d'.encode('utf-8');
str=u'编码测试'.encode('utf-8');
destr='\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print utf8test
print str
print destr
#格式化字符
smsinfo='亲爱的%s你好！截止到%d号，余额是%s' %('李白',2,33)
print smsinfo
n=100
while n>10:
    print n
    n=n-2;
dict={'Ray':1333,'Bob':264,'Skay':12399}
print dict["Ray"]
print "DB"in dict
print dict.get("Ray")  #如果不存在会返回None
#删除一个key 用pop
dict.pop("Ray")
print dict
s=set([1,2,3,4,5,5,6,6,6,4])
print s
s.add(4)
print s
s.remove(4)
print s
def mymethod(x=1):
    return x+1
sum=mymethod(3)
print sum