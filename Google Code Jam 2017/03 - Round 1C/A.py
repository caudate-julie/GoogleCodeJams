# Julie
# 30.04.2017
# Round 1C
# "Ample Syrup"

from time import time
from copy import copy
from random import randint
import math

def AmpleSyrup(K, pancakes):
    map(lambda x: x.append(math.pi * x[0] * x[1] * 2), pancakes)
    pancakes.sort(key=lambda x : x[2], reverse=True)
    # pancake = [radius, height, side area]

    max_sidesum = sum(pancake[2] for pancake in pancakes[:K])
    high_radius = max(pancake[0] for pancake in pancakes[:K])
    max_sidesum += high_radius ** 2 * math.pi
    
    max_radius = max(pancake[0] for pancake in pancakes)
    if max_radius == high_radius: 
        return max_sidesum

    for pancake in pancakes[K:]:
        if pancake[0] == max_radius:
            max_wide_side = pancake[2]
            break

    wide_sum = max_sidesum - high_radius ** 2 * math.pi - pancakes[K - 1][2] + max_wide_side + max_radius ** 2 * math.pi
    return max(max_sidesum, wide_sum)

#inpath = "A-sample.in"
#inpath = "simulated.in"
inpath = "A-large.in"
#inpath = 'A-small-attempt0.in'
outpath = "A.out"

fin = open(inpath)
fout = open(outpath, 'w')
       
timestart = time()
T = int(fin.readline())

for case in range(1, T + 1):
    N, K = map(int, fin.readline().split(' '))
    pancakes = []
    for _ in range(N):
        pancakes.append(map(float, fin.readline().split()))
    result = AmpleSyrup(K, pancakes)
    #print result
    fout.write("Case #%d: %.6f\n" % (case, result))
                 
print "\ntime elapsed: %.4f" % (time() - timestart)
fin.close()
fout.close()

