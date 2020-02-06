# September, 26, 2009
# Round 2
# "A Digging Problem"
# - Kyra -

from time import time

inpath = "B-sample.in"
#inpath = "B-large.in"
#inpath = "B-small-attempt.in"
outpath = "B.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

def DMin(a, b):
    if a == -1:
        return b
    if b == -1:
        return a
    return min(a, b)

def DMax(s):
    a, b = s[0], s[1]
    if DMin(a, b) == a:
        return b
    return a

def Hole(i, j, R):
    if i == R - 1:
        return None
    return cave[i+1][j] == 0

def HoleBottom(R, i, j):
    fall = 0
    i += 1
    while i <= R-1:
        if cave[i][j] == 1:
            break
        fall += 1
        i += 1
    return fall

def MinDigCell(i, j, C, cavedigs):
    le = max(0, j-1)
    re = min(C-1, j+1)
    return DMin(DMax(cavedigs[i-1][le:le+2]), DMax(cavedigs[i-1][re-1:re+1]))

def MinDigs(R, C, F):
    cavedigs = [[-1]*C for i in range(R)]
    i = 0
    print
    while cave[0][i] == 0:
        cavedigs[0][i] = 0
        i += 1
        if i >= C:
            break
    for i in range(1, R):
        for j in range(C):
            m = MinDigCell(i, j, C, cavedigs)
            if m != -1:
                m += cave[i][j]
            k = HoleBottom(R, i, j)
            if k < F:
                cavedigs[i+k][j] = DMin(cavedigs[i+k][j], m)
        if cave[i][0] == 0:
            cavedigs[i][0] = DMin(cavedigs[i][0], cavedigs[i][1])
        flag = True
        while Flag:
            flag = False
            for j in range(1, C):
                if cave[i][j] == 0:
                t = cavedigs[i][j]
                cavedigs[i][j] = DMin(cavedigs[i][j], cavedigs[i][j-1])
                if t != cavedigs[i][j]:
                    flag = True
        flag = True
        if cave[i][C-1] == 0:
            cavedigs[i][0] = DMin(cavedigs[i][0], cavedigs[i][1])
        while Flag:
            flag = False
            for j in range(1, C):
                if cave[i][j] == 0:
                t = cavedigs[i][j]
                cavedigs[i][j] = DMin(cavedigs[i][j], cavedigs[i][j-1])
                if t != cavedigs[i][j]:
                    flag = True
    for x in cavedigs:
        print x
    return min(cavedigs[-1])

fout = open(outpath, 'w')
cases = int(lines[0])
print "Cases:", cases
curline = 1
for n in range(1, cases+1):
    print n
    R, C, F = map(int, lines[curline].split())
    cave = []
    for i in range(1, R+1):
        row = []
        for c in lines[curline + i]:
            if c == '#':
                row.append(1)
            elif c == '.':
                row.append(0)
        cave.append(row)
    curline += R + 1
    for x in cave:
        print x
    result = MinDigs(R, C, F)
    print "ReSuLT", result
    fout.write("Case #%d: %d\n" % (n, result))

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
