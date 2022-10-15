
import mylib
mylib.setup()

import subprocess
f= subprocess.Popen
p= subprocess.PIPE


def i0fpn():
    sp= '/storage/emulated/0/DCIM/Screenshots'
    c= "ls -t %s | head -n 1" % sp
    x= f(c, stdin=p, stdout=p, shell=True)
    v= x.communicate()
    n= v[0].decode('utf-8').strip()
    return '%s/%s' % (sp,n)


#c= "cp -i %s %s" % (fpn,i1)
#x= f(c, stdin=p, stdout=p, shell=True)
#v= x.communicate()
#print(v)


def url2imgfpn():
    imgp= '/storage/emulated/0/Download/prose/mylog/bbcbs/BBCBS_img'
    import sys
    u= sys.argv[1]
    u= u.split('/')
    def g(x):
        b= len(x)==7
        b= b and x[0]=='z'
        return b
    u= [x for x in u if g(x)]
    fn= '%s.jpg' % u[0]
    from myfilelib_mydir import MyDir
    d= MyDir(imgp)
    f= d.touch(fn)
    print ('filename %s' % f)
    if f.exists():
        print ('exists')
        return None
    fpn= '%s/%s' % (imgp,fn)
    return fpn


i0= i0fpn()
i2= url2imgfpn()

if i2:
    c= "ffmpeg -i %s -q:v 31 %s" % (i0,i2)
    print (c)
    x= f(c, stdin=p, stdout=p, shell=True)
    v= x.communicate()
    #n= v[0].decode('utf-8').strip()
    print (v)
