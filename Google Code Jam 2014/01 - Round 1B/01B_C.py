# Round 1B
# "The Bored Traveling Salesman"
# Kyra
# April 3, 2014

from time import time
from copy import copy

#inpath = "C-sample.in"
inpath = "C-large.in"
#inpath = 'C-small-attempt0.in'
outpath = "C.out"


# trying to get to the new city
def AddNode(tripstack, sequence):
    if len(sequence) < 36:
        print sequence
    # seeking for the next city
    if len(sequence) == C:
        return sequence
    for i in range(C):
        if i in sequence:
            continue
        # trying to attach it
        last = len(tripstack) - 1
        #print "trying to attach", i
        while last >= 0:
            if roads[city[i]][city[tripstack[last]]]:
                new_trip = tripstack[:last + 1] + [i]
                new_seq = sequence + [i]
                res = AddNode(new_trip, new_seq)
                if not res == None:
                    return res
            last -= 1
    return None

def Traveller():
    global city
    visited = [False] * C
    city_pairs = sorted([(cities[i], i) for i in range(C)])
    city = [p[1] for p in city_pairs]
    for i in range(C):
        print i
        trip = [i]
        seq = [i]
        res = AddNode(trip, seq)
        if not res == None:
            return res
    return None

ts = time()
fin = open(inpath, 'r')

fout = open(outpath, 'w')
cases = int(fin.readline())
for n in range(1, cases+1):
    C, R = map(int, fin.readline().split())
    cities = []
    city = []
    for i in range(C):
        cities += [int(fin.readline())]
    roads = [[False] * C for i in range(C)]
    for i in range(R):
        r1, r2 = map(int, fin.readline().split())
        roads[r1 - 1][r2 - 1] = True
        roads[r2 - 1][r1 - 1] = True
    res = Traveller()
    assert res != None
    s = ''
    for x in res:
        s += str(cities[city[x]])
    print "\nCase #%d: done" % n
    fout.write("Case #%d: %s\n" % (n, s))


print "Done!"
fin.close()
fout.close()
print "Time:", round(time() - ts, 4)
