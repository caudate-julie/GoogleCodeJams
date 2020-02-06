# April, 10, 2016
# Qualification Round
# "Counting Sheep"

from time import time
from copy import copy
from random import randint

#inpath = "A-sample.in"
inpath = "A-large.in"
#inpath = 'A-small-attempt0.in'
outpath = "A.out"

fin = open(inpath)
fout = open(outpath, 'w')

def Digits(T):
    d = []
    while T > 0:
        d += [T % 10]
        T /= 10
    return d

def SheepCounting(T):
    if T == 0: return "INSOMNIA"
    found = [False] * 10
    i = 1
    while not reduce(lambda x, y: x and y, found):
        for n in Digits(T * i):
            found[n] = True
        i += 1
    return T * (i - 1)   # because we incremented it before leaving the loop

        
timestart = time()
N = int(fin.readline())

for case in range(1, N + 1):
    T = int(fin.readline())
    result = SheepCounting(T)
    #print SheepCounting(T)
    fout.write("Case #%d: %s\n" % (case, result))
                 
fin.close()
fout.close()
print "%.4f" % (time() - timestart)
