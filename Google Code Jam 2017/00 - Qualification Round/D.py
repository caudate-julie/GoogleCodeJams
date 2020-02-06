# Julie
# April, 8, 2017
# Qualification Round
# "Fashion Show"

from time import time
from copy import deepcopy
from sets import Set

# + : bishop, x : rook

class FashionShow:
    def __init__(self, N):
        self.N = N
        self.rooks = [[False] * N for i in xrange(N)]
        self.bishops = [[False] * N for i in xrange(N)]
        self.changes = Set([])

    def NextCell(self, x, y, direction):
        x += direction[0]
        y += direction[1]
        if x >= self.N or y >= self.N or x < 0 or y < 0:
            return (None, None)
        return x, y

    def MaximizeRooks(self):
        for i in range(self.N):
            if any(self.rooks[i]):
                continue
            for j in range(self.N):
                if any(self.rooks[k][j] for k in range(self.N)):
                    continue
                self.rooks[i][j] = True
                self.changes.add((i, j))
                break

    def DiagonalIsFree(self, i, j, direction):
        i_cur, j_cur = i, j
        while not i_cur is None:
            if self.bishops[i_cur][j_cur]:
                return False
            i_cur, j_cur = self.NextCell(i_cur, j_cur, direction)
        i_cur, j_cur = i, j
        while not i_cur is None:
            if self.bishops[i_cur][j_cur]:
                return False
            i_cur, j_cur = self.NextCell(i_cur, j_cur, (-direction[0], -direction[1]))
        return True

    def MaximizeBishops(self):
        diags = ((0, 1), (self.N - 1, -1))
        for iteration in range((self.N + 1) / 2):
            for j, direct in diags:
                for i in range(self.N):
                    i_cur, j_cur = i + iteration * direct, j + iteration * direct
                    if i_cur >= self.N or j_cur >= self.N or i_cur < 0 or j_cur < 0: continue
                    downIsFree = self.DiagonalIsFree(i_cur, j_cur, (1, direct))
                    upIsFree = self.DiagonalIsFree(i_cur, j_cur, (-1, direct))
                    if downIsFree and upIsFree:
                        self.bishops[i_cur][j_cur] = True
                        self.changes.add((i_cur, j_cur))
                        continue
                    if upIsFree and self.DiagonalIsFree(j_cur, i_cur, (1, direct)):
                        self.bishops[j_cur][i_cur] = True
                        self.changes.add((j_cur, i_cur))
                        continue
                    if downIsFree and self.DiagonalIsFree(self.N - j_cur - 1, self.N - i_cur - 1, (-1, direct)):
                        self.bishops[self.N - j_cur - 1][self.N - i_cur - 1] = True
                        self.changes.add((self.N - j_cur - 1, self.N - i_cur - 1))
                        continue

    # + : bishop, x : rook
    def AddModels(self, modelset):
        for model, x, y in modelset:
            if model == 'x':
                self.rooks[x][y] = True
            elif model == '+':
                self.bishops[x][y] = True
            else:
                assert False   # no other model!

    def ShowGrid(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.bishops[i][j] and self.rooks[i][j]: print "o",
                elif self.bishops[i][j]: print '+',
                elif self.rooks[i][j]: print 'x',
                else: print '.',
            print
        print

    def GetScore(self):
        return sum(self.bishops[i][j] for i in range(self.N) for j in range(self.N)) + \
               sum(self.rooks[i][j] for i in range(self.N) for j in range(self.N))

    # + : bishop, x : rook
    def GetAnswerLines(self):
        answer = []
        for i, j in self.changes:
            if self.bishops[i][j] and self.rooks[i][j]:
                answer.append('o %d %d\n' % (i + 1, j + 1))
            elif self.bishops[i][j]:
                answer.append('+ %d %d\n' % (i + 1, j + 1))
            elif self.rooks[i][j]:
                answer.append('x %d %d\n' % (i + 1, j + 1))
        return answer

    def Solve(self):
        #self.ShowGrid()
        self.MaximizeBishops()
        self.MaximizeRooks()
        #self.ShowGrid()
        #print self.N, self.GetScore(), 3 * self.N - 2, "\n"
        #assert self.N == 1 or self.GetScore() == 3 * self.N - 2
        return (self.GetScore(), len(self.changes), self.GetAnswerLines())

        
#inpath = "D-sample.in"
inpath = "D-large.in"
#inpath = 'D-small-attempt1.in'
#inpath = "simulated.in"
outpath = "D.out"

fin = open(inpath)
fout = open(outpath, 'w')

timestart = time()
    
T = int(fin.readline())
for case in range(1, T+1):
    N, M = map(int, fin.readline().split())
    modelset = []
    for i in xrange(M):
        model, x, y = fin.readline().split()
        x, y = int(x), int(y)
        if model == 'o':
            modelset += [['x', x - 1, y - 1], ['+', x - 1, y - 1]]
        else:
            modelset += [[model, x - 1, y - 1]]   # numerate array from zero
    fs = FashionShow(N)
    fs.AddModels(modelset)
    S, M, lines = fs.Solve()
    fout.write("Case #%d: %d %d\n" % (case, S, M))
    for line in lines:
        fout.write(line)
    
fin.close()
fout.close()
print "time elapsed: %.4f" % (time() - timestart)
