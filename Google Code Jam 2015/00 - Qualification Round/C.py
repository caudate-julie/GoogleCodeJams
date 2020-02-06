# April, 11, 2015
# Qualification Round
# "Dijkstra"

from time import time

#inpath = "C-sample.in"
inpath = "C-large.in"
#inpath = "C-small-attempt2.in"
outpath = "C.out"

timestart = time()

fin = open(inpath)
fout = open(outpath, 'w')


Quaternions = (((0, 1), (1, 1), (2, 1), (3, 1)),
               ((1, 1), (0, -1), (3, 1), (2, -1)),
               ((2, 1), (3, -1), (0, -1), (1, 1)),
               ((3, 1), (2, 1), (1, -1), (0, -1)))

def Convert(symb):
    if symb == "i":   return 1
    elif symb == "j": return 2
    else:             return 3

def NextChar(line, i, needed):
    symbol = 0
    sign = 1
    while i < len(line):
        current = Convert(line[i])
        x, y = Quaternions[symbol][current]
        symbol = x
        sign *= y
        if symbol == needed and sign == 1:
            return i
        i += 1
    return -1

def MultiplyRest(line, i):
    symbol = 0
    sign = 1
    while i < len(line):
        current = Convert(line[i])
        x, y = Quaternions[symbol][current]
        symbol = x
        sign *= y
        i += 1
    return symbol == 0 and sign == 1

def CutRepeats(repeats):
    if repeats <= 12:
        return repeats
    else:
        return 12 + repeats % 4

def Dijkstra(line, R):
    R = CutRepeats(R)
    line *= R
    position = 0
    found = 0
    while found < 3:
        if position == len(line):
            return "NO"
        pos = NextChar(line, position, found + 1)
        if pos == -1:
            return "NO"
        found += 1
        position = pos + 1
    if MultiplyRest(line, position):
        return "YES"
    else:
        return "NO"
    
T = int(fin.readline())
for case in range(1, T+1):
    N, R = map(int, fin.readline().split())
    line = fin.readline()[:-1]
    result = Dijkstra(line, R)
    fout.write("Case #%d: %s\n" % (case, result))
    
fin.close()
fout.close()
print "%.4f" % (time() - timestart)
