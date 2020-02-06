# June, 5, 2010
# Round 2
# "Making Chess Boards"

from time import time
from math import log

inpath = "C-sample.in"
#inpath = "C-bigsample.in"
#inpath = 'C-small-attempt0.in'
#inpath = "C-large.in"
outpath = "C.out"

fin = open(inpath)
fout = open(outpath, 'w')

timestart = time()
T = int(fin.readline())
for case in range(1, T+1):
    print "Case:", case
    M, N = map(int, fin.readline().split())
    print M, N
    bark = list(fin.readline().strip() for i in range(M))
    assert len(bark[0]) == N/4
    result = Boards(bark, M, N)
    fout.write("Case #%d: %s\n" % (case, result[0]))
    for x, y in result[1:]:
        fout.write("%d %d\n" % (x, y))
    print
        
fin.close()
fout.close()
print "\nTime: %.4f" % (time() - timestart)
