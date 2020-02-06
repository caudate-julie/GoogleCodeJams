# June, 5, 2010
# Round 2
# "Elegant Diamond"

from time import time

inpath = "A-sample.in"
#inpath = "A-bigsample.in"
#inpath = 'A-small-attempt0.in'
#inpath = "A-large.in"
outpath = "A.out"

fin = open(inpath)
fout = open(outpath, 'w')

def CheckSymmetry(matrix):
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix)):
            if (matrix[i][j] != matrix[j][i]
                or matrix[i][j] != matrix[-j][-i]):
                return False
    return True

def Enhance(diamond, k):
    matrix = MakeMatrix(diamond, k)
    for x in matrix:
        print x
    if CheckSymmetry(matrix):
        return 0
    for d in xrange(1, k-1):
        if any(map(CheckSymmetry, (
            list(x[d:] for x in matrix[d:]),
            list(x[d:] for x in matrix[:-d]),
            list(x[:-d] for x in matrix[d:]),
            list(x[:-d] for x in matrix[:-d]),
        ))):
            d = k - d
            print "d:", d
            return (k-d)*(3*k-d)
    return (2*k-1)**2 - 1

def MakeMatrix(diamond, k):
    matrix = [[] for i in range(k)]
    for i in xrange(2*k-1):
        for j in xrange(len(diamond[i])):
            matrix[min(i, k-1)-j].append(diamond[i][j])
    return matrix

timestart = time()
T = int(fin.readline())
for case in xrange(1, T+1):
    k = int(fin.readline())
    diamond = list(map(int, fin.readline().split())
                   for i in xrange(2*k-1))
    result = Enhance(diamond, k)
    print result
    fout.write("Case #%d: %s\n" % (case, result))
    
fin.close()
fout.close()
print "\nTime: %.4f" % (time() - timestart)
