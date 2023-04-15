
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
    d= '/storage/emulated/0/DCIM/Screenshots'
    d2= 'small/Duolingo/French/Story'
    c= "ffmpeg -i %s/q.jpg -q:v 31 %s/%s.jpg.small.jpg"
    c= c % (d,d2,v)
    print (c)
    import subprocess
    f= subprocess.Popen
    p= subprocess.PIPE
    v= f(c, stdin=p, stdout=p, shell=True)
    v= v.communicate()
    v= v[0].decode('utf-8').strip()
    print (v)

