# June, 5, 2010
# Round 2
# "World Cup 2010"

from time import time
from math import log

inpath = "B-sample.in"
#inpath = "B-bigsample.in"
#inpath = 'B-small-attempt0.in'
#inpath = "B-large.in"
outpath = "B.out"

fin = open(inpath)
fout = open(outpath, 'w')

timestart = time()
T = int(fin.readline())
for case in range(1, T+1):
    L, P, C = map(int, fin.readline().split())
    result = Testing(L, P, C)
    print result
    fout.write("Case #%d: %s\n" % (case, result))

fin.close()
fout.close()
print "\nTime: %.4f" % (time() - timestart)
