# April, 11, 2015
# Qualification Round
# "Ominous Omino"

from time import time

#inpath = "D-sample.in"
inpath = "D-large.in"
#inpath = 'D-small-attempt0.in'
outpath = "D.out"

timestart = time()

fin = open(inpath)
fout = open(outpath, 'w')

def TooNarrow(X, R, C):
    if X >= 3:
        if C == 1 or R == 1:
            return True
    if X >= 4:
        if C == 2 or R == 2:
            return True
    if X >= 6:
        if C == 3 or R == 3:
            return True

def Omino(X, R, C):
    if X >= 7:
        return "RICHARD"
    if not R * C % X == 0:
        return "RICHARD"
    if TooNarrow(X, R, C):
        return "RICHARD"
    return "GABRIEL"
    
T = int(fin.readline())
for case in range(1, T+1):
    X, R, C = map(int, fin.readline().split())
    result = Omino(X, R, C)
    print result
    fout.write("Case #%d: %s\n" % (case, result))
    #print case
    
fin.close()
fout.close()
print "%.4f" % (time() - timestart)
