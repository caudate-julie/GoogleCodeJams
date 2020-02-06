# September, 26, 2009
# Round 2
# ""
# - Kyra -

from time import time
from copy import deepcopy
from math import sqrt

inpath = "D-sample.in"
#inpath = "D-large.in"
#inpath = "D-small-attempt.in"
outpath = "D.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

def lenght(s):
    a, b = s[0], s[1]
##    print a, b
##    print sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2) + a[2] + b[2]
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2) + a[2] + b[2]

def Radius(plants):
    num = len(plants)
    if num == 1:
        return plants[0][2]
    if num == 2:
        return max(x[2] for x in plants)
    radius = []
    for i in range(3):
        newplant = deepcopy(plants)
        p = newplant.pop(i)
        radius.append(max(lenght(newplant), p[2]))
    return min(radius)

fout = open(outpath, 'w')
cases = int(lines[0])
print "Cases:", cases
curline = 1
for n in range(1, cases+1):
    plantnum = int(lines[curline])
    plants = []
    for i in range(plantnum):
        plants.append(map(int, lines[curline + i + 1].split()))
    result = Radius(plants)
    print '%.6f' % result
    fout.write("Case #%d: %.6f\n" % (n, result))

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
