# Julie
# 22.04.2017
# Round 1B
# "Cruise Control"

from time import time
from copy import copy
from random import randint

def CruiseControl(D, horses):
    max_time = 0
    for position, speed in horses:
        max_time = max(max_time, (D - position) / speed)   
        # second is the time where horse passes point D
    return D / max_time


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
    D, N = map(int, fin.readline().split(' '))
    horses = []
    for horse in range(N):
        horses.append(map(float, fin.readline().split()))
    result = CruiseControl(D, horses)
    #print result
    fout.write("Case #%d: %.6f\n" % (case, result))

    #for row in range(R):
    #	fout.write("%s\n" % (result[row]))
                 
print "\ntime elapsed: %.4f" % (time() - timestart)
fin.close()
fout.close()

