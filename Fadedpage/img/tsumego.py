
import mylib
mylib.setup()



def i0fn():
    c= "find ./*.jpg -maxdepth 1 -type f | head -n 1"
    print (c)
    x= f(c, stdin=p, stdout=p, shell=True)
    v= x.communicate()
    print (v)
    v= v[0].decode('utf-8').strip()
    v= '"%s"' % v
    #v= v.split(' ')[1:]
    #v= ' '.join(v)
    print (v)
    return v


#c= "cp -i %s %s" % (fpn,i1)
#x= f(c, stdin=p, stdout=p, shell=True)
#v= x.communicate()
#print(v)


def small(i0):
    s= '%s.small.jpg'
    i2= s % i0
    c= "ffmpeg -i %s -q:v 31 %s" % (i0,i2)
    print (c)
    x= f(c, stdin=p, stdout=p, shell=True)
    v= x.communicate()
    n= v[0].decode('utf-8').strip()
    print (n)
    c= "mv %s done/." % i0
    print (c)
    x= f(c, stdin=p, stdout=p, shell=True)
    v= x.communicate()
    c= "mv %s small/." % i2
    print (c)
    x= f(c, stdin=p, stdout=p, shell=True)
    v= x.communicate()

def dojob():
    i0= i0fn()
    print (i0)
    if not 'jpg.small.jpg' in i0:
        small(i0)

if __name__=="__main__":
    import sys
    v= sys.argv[1]
    if not v[-1]=='.':
        v= '%s.' % v
    a= 'e1 e2 m1 m2 h1 h2'
    a= a.split(' ')
    d= '/storage/emulated/0/ScreenshotTouch/Screenshot'
    s= '%s%s.jpg'
    a= [s % (v,x) for x in a]
    c= "ffmpeg -i %s/%s -q:v 31 small/Tsumego/Tsumego-Pro/%s.small.jpg"
    a= [c % (d,x,x) for x in a]
    import subprocess
    f= subprocess.Popen
    p= subprocess.PIPE
    for x in a:
        print (x)
        v= f(x, stdin=p, stdout=p, shell=True)
        v= v.communicate()
        v= v[0].decode('utf-8').strip()
        print (v)

