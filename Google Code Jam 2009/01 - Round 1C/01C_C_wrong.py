# September, 13, 2009
# Round 1C
# "Bribe the Prisoners"
# - Kyra -
# not yet

from time import time
from bisect import bisect

inpath = "C-sample.in"
#inpath = "C-large-practice.in"
#inpath = "C-small-practice.in"
outpath = "C.out"

class prisoner(object):
    def __init__(self, cellnumber, pnumber):
        self.number = pnumber
        self.left = 0
        self.right = cellnumber+1

class prisonrelease(object):
    def __init__(self, cellnumber):
        self.unordered = []
        self.cellnumber = cellnumber
        self.ordered = []
    def addprisoners(self, prisoners):
        for i in range(len(prisoners)):
            newone = prisoner(self.cellnumber, prisoners[i])
            self.unordered.append(newone)
    def chooseone(self, A, B):
        alefts = A.number-A.left-1
        arights = A.right-A.number-1
        blefts = B.number-B.left-1
        brights = B.right-B.number-1
        if A.number<B.number and alefts<brights or B.number<A.number and arights<blefts:
            return B
        else:
            return A
    def addordered(self, A):
        del self.unordered[self.unordered.index(A)]
        self.ordered.append(A)
        for B in self.unordered:
            if B.number<A.number<B.right:
                B.right = A.number
            elif B.left<A.number<B.number:
                B.left = A.number
    def printrelease(self):
        for A in self.ordered:
            print A.number,
        print
    def countbribe(self):
        bribe = 0
        for A in self.ordered:
            bribe += A.right - A.left - 2
        return bribe
    def release(self):
        while len(self.unordered) > 0:
            C = self.unordered[0]
            for A in self.unordered[1:]:
                C = self.chooseone(A, C)
            self.addordered(C)
        return self.countbribe()

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

fout = open(outpath, 'w')
cases = int(lines[0])
print "Cases:", cases
for n in range(1, cases+1):
    cellnumber = int(lines[2*n-1].split()[0])
    released = map(int,lines[2*n].split())
    prison = prisonrelease(cellnumber)
    prison.addprisoners(released)
    bribe = prison.release()
    fout.write("Case #%d: %d\n" % (n, bribe))

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
