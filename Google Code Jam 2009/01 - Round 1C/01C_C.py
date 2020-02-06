# September, 13, 2009
# Round 1C
# "Bribe the Prisoners"
# - Kyra -
# correct

from time import time
from bisect import bisect

#inpath = "C-sample.in"
inpath = "C-large-practice.in"
#inpath = "C-small-practice.in"
outpath = "C.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()
#MAXCELLS = 100
#MAXPRISONERS = 5
MAXCELLS = 10000
MAXPRISONERS = 100
MINBRIBE = MAXCELLS*MAXPRISONERS

def CountBribe(le, re):
    if bribes.has_key((le, re)):
        return bribes[(le, re)]
    minbribe = MINBRIBE
    releasing = list(y for y in prisoners if le < y < re)
    if len(releasing) == 0:
        minbribe = 0
    elif len(releasing) == 1:
        minbribe = re-le-2
    else:
        for x in releasing:
            bribe = re - le - 2 + CountBribe(le, x) + CountBribe(x, re)
            if bribe < minbribe:
                minbribe = bribe
    bribes[(le, re)] = minbribe
    return minbribe

fout = open(outpath, 'w')
cases = int(lines[0])
print "Cases:", cases
for n in range(1, cases+1):
#    print "CASE", n
    bribes = {}
    cellnumber = int(lines[2*n-1].split()[0])
    prisoners = map(int,lines[2*n].split())
#    print prisoners
    bribe = CountBribe(0, cellnumber+1)
#    print bribe
    fout.write("Case #%d: %d\n" % (n, bribe))
#    print "curtime:", round(time() - ts, 4)

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
