from time import time

def LCD(a, b):
    while b > 0:
        a = a%b
        a, b = b, a
    return a

def Check(a, b):
    print a, b
    ts = time()
    print LCD(a, b)
    print "%.4f" % (time() - ts)

Check(10, 150)
Check(19191, 98374)
Check(2398474, 9238444)
Check(3298744444, 345435345555)
Check(234333, 34555545)
Check(2344432, 23432232)
Check(32355532, 2342344444322)
Check(234333234, 23422222234)
Check(23444234, 234444432)
Check(434444, 4)
Check(12342423322322, 233)
Check(124342344444222, 23)
Check(3444323424, 234324235235)
