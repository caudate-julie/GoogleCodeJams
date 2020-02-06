# April 12, 2014
# Qualification Round
# "Magic Trick"
# =  =

from time import time
from copy import copy

#inpath = "A-sample.in"
#inpath = "A-large.in"
inpath = 'A-small-attempt0.in'
outpath = "A.out"

fin = open(inpath)
fout = open(outpath, 'w')

def MagicTrick(first, second):
    matches = []
    for a in first:
        if a in second:
            matches += [a]
    if len(matches) > 1:
        return "Bad magician!"
    elif len(matches) == 0:
        return "Volunteer cheated!"
    else:
        return matches[0]

timestart = time()
T = int(fin.readline())
for case in range(1, T+1):
    first_opt = int(fin.readline())
    first_set = list(map(int, fin.readline().split()) for i in range(4))
    first = first_set[first_opt - 1]
    second_opt = int(fin.readline())
    second_set = list(map(int, fin.readline().split()) for i in range(4))
    second = second_set[second_opt - 1]
    fout.write("Case #%d: %s\n" % (case, MagicTrick(first, second)))
    
fin.close()
fout.close()
print "%.4f" % (time() - timestart)
