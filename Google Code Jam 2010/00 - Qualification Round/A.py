# May, 8, 2010
# Qualification Round
# "Snapper Chain"

from time import time
from copy import copy

#inpath = "A-sample.in"
inpath = "A-large.in"
#inpath = 'A-small-attempt0.in'
outpath = "A.out"

fin = open(inpath)
fout = open(outpath, 'w')

def IsOn(b):
    if b: return "ON"
    else: return "OFF"

def Light(N, K):
    return IsOn((K+1)%2**N == 0)

timestart = time()
T = int(fin.readline())
for case in range(1, T+1):
    N, K = map(int, fin.readline().split())
    fout.write("Case #%d: %s\n" % (case, Light(N, K)))
    
fin.close()
fout.close()
print "%.4f" % (time() - timestart)
