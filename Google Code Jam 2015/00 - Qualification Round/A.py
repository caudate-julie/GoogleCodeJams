# April, 11, 2015
# Qualification Round
# "Standing Ovation"

from time import time
from copy import copy
from random import randint

#inpath = "A-sample.in"
inpath = "A-large.in"
#inpath = 'A-small-attempt0.in'
outpath = "A.out"

fin = open(inpath)
fout = open(outpath, 'w')

def Ovations(K):
    audience = map(int, K)
    stand = 0
    friends = 0
    for i in xrange(len(audience)):
        if stand < i:
            friends += i - stand
            stand = i
        stand += audience[i]
    return friends

timestart = time()
T = int(fin.readline())

for case in range(1, T+1):
    K = fin.readline().split()
    result = Ovations(K[1])
    fout.write("Case #%d: %s\n" % (case, result))
                 
fin.close()
fout.close()
print "%.4f" % (time() - timestart)
