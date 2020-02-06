# Julie
# April, 8, 2017
# Qualification Round
# "Oversized Pancake Flipper"

from time import time
from copy import copy
from random import randint

def PancakeFlip(pancakes, size):
    N = len(pancakes)
    count = 0
    for i in range(N - size + 1):
        if pancakes[i]: continue    # already the right side
        for j in range(i, i + size):
            pancakes[j] = not pancakes[j]
        count += 1
    # if the remaining size - 1 pancake is not the right side, it's impossible to flip them
    # we could check all of them, but it's faster to look only at the last one
    if not all(pancakes[-size:]): return "IMPOSSIBLE"
    assert all(pancakes)
    return count

#inpath = "A-sample.in"
#inpath = "simulated.in"
inpath = "A-large.in"
#inpath = 'A-small-attempt0.in'
outpath = "A.out"

fin = open(inpath)
fout = open(outpath, 'w')
       
timestart = time()
N = int(fin.readline())

for case in range(1, N + 1):
    S, K = fin.readline().split(' ')
    pancakes = [c == '+' for c in S]
    K = int(K)
    result = PancakeFlip(pancakes, K)
    #print result
    fout.write("Case #%d: %s\n" % (case, result))
                 
fin.close()
fout.close()
print "\ntime elapsed: %.4f" % (time() - timestart)
