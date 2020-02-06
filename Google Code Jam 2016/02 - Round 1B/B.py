# April, 16, 2016
# Kyra
# Round 1A
# "Rank and File "

from time import time

#inpath = "B-sample.in"
inpath = "B-large-practice.in"
#inpath = 'B-small-practice.in'
outpath = "B.out"

def RankedSearch(array, n):
    for i in range(len(array)):
        if array[i] == n:
            return i
        if array[i] > n:
            return -1
    return -1

def Rank(N, grid):
    missing = []
    for i in xrange(2 * N - 1):
        for j in xrange(N):
            if grid[i][j] == 0: continue
            for k in xrange(i + 1, 2 * N - 1):
                t = RankedSearch(grid[k], grid[i][j])
                if t != -1:
                    grid[i][j] = grid[k][t] = 0
                    break
            if grid[i][j] > 0:
                missing.append(grid[i][j])
    assert len(missing) == N
    missing.sort()
    return missing


fin = open(inpath)
fout = open(outpath, 'w')

timestart = time()
T = int(fin.readline())
for case in range(1, T+1):
    N = int(fin.readline())
    grid = list(map(int, fin.readline().split(' ')) for i in range(2 * N - 1))
    result = Rank(N, grid)
    #print result
    fout.write("Case #%d: " % case)
    for x in result:
        fout.write("%d " % x)
    fout.write("\n")
        
fin.close()
fout.close()
print "\nTime: %.4f" % (time() - timestart)
