import time,os,sys,svnconfig

dist=svnconfig.setting['dist']

def checkout():

    cmd='svn export  %(url)s %(dist)s --username %(user)s --password %(pwd)s'%svnconfig.setting
    print "execute %s"%cmd
    #print os.popen(cmd).read()
    os.system("rm -rf %(dist)s"%svnconfig.setting)
    return os.system(cmd)
def svnversion():
    cmd = 'svn info  %(url)s --username %(user)s --password %(pwd)s' % svnconfig.setting
    #print "execute %s" % cmd
    # print os.popen(cmd).read()
    return os.popen(cmd)
while True:
    ret=svnversion().read()
    print ret
    if(ret==0):
        print 'check out success'
    else:
        print 'check out fail'
    time.sleep(svnconfig.setting['interval'])