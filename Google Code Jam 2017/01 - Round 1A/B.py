# Julie
# -- practice --
# Round 1A
# "Ratatouille"

from time import time
from math import sqrt

def LastTidyNumber(n):
    number = str(n)
    edge = len(number)
    for i in xrange(0, len(number) - 1):
        if int(number[i]) > int(number[i + 1]):
            edge = i
            break
    if edge == len(number): 
        return n
    while edge > 0 and number[edge] == number[edge - 1]:
        edge -= 1
    return int(number[:edge] + str(int(number[edge]) - 1) + '9' * (len(number) - edge - 1))

    
#inpath = "B-sample.in"
#inpath = "simulated.in"
inpath = "B-large.in"
#inpath = 'B-small-attempt2.in'
outpath = "B.out"

fin = open(inpath)
fout = open(outpath, 'w')

timestart = time()

T = int(fin.readline())
for case in range(1, T + 1):
    N, P = map(int, fin.readline().split())
    requirements = map(int, fin.readline().split())
    packages = [[] for i in range(N)]
    for i in range(P):
    	
    result = LastTidyNumber(N)
    #print result
    fout.write("Case #%d: %d\n" % (case, result))
    
fin.close()
fout.close()
print "%.4f" % (time() - timestart)
