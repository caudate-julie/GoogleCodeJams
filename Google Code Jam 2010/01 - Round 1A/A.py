# May, 22, 2010
# Round 1A
# "Rotate"

from time import time

#inpath = "A-sample.in"
#inpath = "A-large.in"
inpath = 'A-small-attempt2.in'
outpath = "A.out"

def DelEmpty(array):
    return list(x for x in array if x != '.')

def Rotate(table):
    for i in range(len(table)):
        pieces = DelEmpty(table[i])
        table[i] = ['.']*(len(table) - len(pieces)) + pieces

def Count(array, c):
    m = 0
    i = 0
    while i < len(array):
        k = i
        while k < len(array) and array[k] == c:
            k += 1
        m = max(m, k - i)
        i = k+1
    return m

def HasHorisontal(table, K, c):
    for x in table:
        if K <= Count(x, c):
            return True
    return False

def HasVertical(table, K, c):
    for j in range(len(table)):
        if list(table[i][j] for i in range(len(table))) == [c]*K:
            return True
    return False

def GetDiagonal(table, x, y, d):
    diag = []
    i, j = x, y
    while i < len(table) and j < len(table) and i >= 0:
        diag.append(table[i][j])
        i += d
        j += 1
    return diag

def HasRightDiagonal(table, K, c):
    for i in range(len(table)):
        diag = GetDiagonal(table, i, 0, 1)
        if K <= Count(diag, c):
            return True
    for j in range(len(table)):
        diag = GetDiagonal(table, 0, j, 1)
        if K <= Count(diag, c):
            return True
    return False

def HasLeftDiagonal(table, K, c):
    for i in range(len(table)):
        diag = GetDiagonal(table, i, 0, -1)
        if K <= Count(diag, c):
            return True
    for j in range(len(table)):
        diag = GetDiagonal(table, len(table)-1, j, -1)
        if K <= Count(diag, c):
            return True
    return False

def Play(K, table):
    Rotate(table)
    bresult = HasHorisontal(table, K, 'B') or \
              HasVertical(table, K, 'B') or \
              HasRightDiagonal(table, K, 'B') or \
              HasLeftDiagonal(table, K, 'B')
    rresult = HasHorisontal(table, K, 'R') or \
              HasVertical(table, K, 'R') or \
              HasRightDiagonal(table, K, 'R') or \
              HasLeftDiagonal(table, K, 'R')
    if bresult and rresult:
        return "Both"
    elif bresult:
        return "Blue"
    elif rresult:
        return "Red"
    else:
        return "Neither"

fin = open(inpath)
fout = open(outpath, 'w')

timestart = time()
T = int(fin.readline())
for case in range(1, T+1):
    N, K = map(int, fin.readline().split())
    table = list(list(fin.readline()[:-1]) for i in range(N))
    assert len(table) == len(table[-1])
    result = Play(K, table)
    print result
    fout.write("Case #%d: %s\n" % (case, result))
    
fin.close()
fout.close()
print "\nTime: %.4f" % (time() - timestart)
