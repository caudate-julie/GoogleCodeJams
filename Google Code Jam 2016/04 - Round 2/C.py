# 2016 practice
# Round 2
# "The Gardener of Seville"

from time import time
from math import log

inpath = "C-sample.in"
#inpath = "C-bigsample.in"
#inpath = 'C-small-attempt0.in'
#inpath = "C-large.in"
outpath = "C.out"

fin = open(inpath)
fout = open(outpath, 'w')

def Bacteria()

timestart = time()
T = int(fin.readline())
for case in xrange(1, T+1):
    print "Case:", case
    N = int(fin.readline())
    gridcoords = []
    for i in xrange(N):
        gridcoords.append(map(int, fin.readline().split()))
    result = Bacteria(gridcoords)
    print result
    fout.write("Case #%d: %s\n" % (case, result[0]))
    for x, y in result[1:]:
        fout.write("%d %d\n" % (x, y))
    print
        
fin.close()
fout.close()
print "\nTime: %.4f" % (time() - timestart)
