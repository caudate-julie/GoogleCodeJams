# April 12, 2014
# Qualification Round
# "Deceitful War"
# = Kyra =

from time import time
from copy import copy
from random import randrange

#inpath = "D-sample.in"
inpath = "D-large.in"
#inpath = 'D-small-attempt0.in'
outpath = "D.out"

fin = open(inpath)
fout = open(outpath, 'w')


def KenChoice(bricks, key):
    if key > bricks[-1] or key < bricks[0]:
        return 0
    lower = 0
    higher = len(bricks) - 1
    while higher - lower > 1:
        mid = lower + (higher - lower) / 2;
        if   key < bricks[mid]:  higher = mid
        elif key > bricks[mid]:  lower = mid
        else:                    return mid
    return higher;

def War(Naomi, Ken):
    score = 0
    while len(Naomi) > 0:
        j = KenChoice(Ken, Naomi[0])
        if Naomi[0] > Ken[j]: score += 1
        del Naomi[0]
        del Ken[j]
    return score

def Turn(Naomi, i, Ken, j):
    if Naomi[i] > Ken[j]:
        score = 1
    else:
        score = 0
    del Naomi[i]
    del Ken[j]
    return score

# we can persuade Ken remove [0] by telling him a number
# bigger than his maximum: we must use any number bigger
# or smaller than minimum: we must use any number less
# anyway we can both get rid of [0]-s
def DeleteMin(Naomi, Ken):
    return Turn(Naomi, 0, Ken, 0)

# just the same we can make Ken get rid of max, getting rid of min ourselves
def DeleteMax(Naomi, Ken):
    return Turn(Naomi, 0, Ken, -1)

def DeceptiveWar2(Naomi, Ken, score, max_score):
    if len(Naomi) <= max_score - score: return max_score
    Naomi2 = copy(Naomi)
    Ken2 = copy(Ken)
    score1 = score + DeleteMin(Naomi, Ken)
    score2 = score + DeleteMax(Naomi2, Ken2)
    max_score = max((score, score1, score2))
    res1 = DeceptiveWar(Naomi, Ken, score1, max_score)
    res2 = DeceptiveWar(Naomi2, Ken2, score2, max_score)
    return max (res1, res2, max_score)

def DeceptiveWar(Naomi, Ken):
    N = len(Naomi)
    j = len(Naomi) - 1
    score = 0
    for i in range(N - 1, -1, -1):
        while j >= 0 and Naomi[i] < Ken[j]:
            j -= 1
        if j < 0:
            return score
        score += 1
        j -= 1
    return score
    
timestart = time()
T = int(fin.readline())
for case in range(1, T+1):
    fin.readline()
    Naomi = map(float, fin.readline().split())
    Naomi.sort()
    Naomi1 = copy(Naomi)
    Ken = map(float, fin.readline().split())
    Ken.sort()
    Ken1 = copy(Ken)
    w = War(Naomi, Ken)
    dw = DeceptiveWar(Naomi1, Ken1)
    print case, ":", dw, w
    fout.write("Case #%d: %d %d\n" % (case, dw, w))

fin.close()
fout.close()
#print "%.4f" % (time() - timestart)
