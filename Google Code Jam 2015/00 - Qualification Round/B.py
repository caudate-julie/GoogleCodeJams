# April, 11, 2015
# Qualification Round
# "Infinite House of Pancakes"

from time import time
from math import sqrt

#inpath = "B-sample.in"
#inpath = "B-large.in"
inpath = 'B-small-attempt0.in'
outpath = "B.out"

def Breakfast(pancakes):
    minutes = 0
    largest = max(pancakes)
    while largest > 3:
        minutes += 1
        i = pancakes.index(largest)
        if largest == 4:
            pancakes[i] = 2
            pancakes.append(2)
        else:
            pancakes[i] = largest - 3
            pancakes.append(3)
        largest = max(pancakes)
    return minutes + largest
        
    
timestart = time()

fin = open(inpath)
fout = open(outpath, 'w')

T = int(fin.readline())
for case in range(1, T+1):
    fin.readline()

    pancakes = map(int, fin.readline().split())
    fout.write("Case #%d: %d\n" % (case, Breakfast(pancakes)))
    
fin.close()
fout.close()
print "%.4f" % (time() - timestart)
