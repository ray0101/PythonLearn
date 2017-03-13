#!/usr/bin/python
# -*- coding: UTF-8 -*-
print 'hello, world'
'''可以以,分开,输入显示空格'''
"""这里是注释"""
print 'hello', 'world'
'''加法'''
print 100 + 100
print '100+200=', 100 + 200
print '请输入您的名字:'
name = raw_input();
print "您的名字是:", name
"""True False"""
age = int(raw_input("请输入您的年龄:"));
if int(age) > 30:
    print name, "您都30多了还瞎玩呢"
elif int(age) > 18:
    print name, "您还不到30,别光玩了"
else:
    print name, "您还是个小孩儿,赶紧玩吧"
"""IF ELSE"""
names=['曹操','大乔','小乔']
for name in names:
    print name;