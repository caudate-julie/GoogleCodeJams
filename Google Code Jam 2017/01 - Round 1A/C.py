# Julie
# -- practice --
# Round 1A
# "Play the Dragon"

from time import time

def AddSpaces(space, increment, spaces):
    i = 0
    while i < len(spaces) and spaces[i][0] > space:
        i += 1
    if i < len(spaces) and spaces[i][0] == space:
        spaces[i][1] += increment
        return spaces
    return spaces[:i] + [[space, increment]] + spaces[i:]

def DeleteSpaces(space, decrement, spaces):
    i = 0
    while spaces[i][0] > space:
        i += 1
    if spaces[i][1] == decrement:
        return spaces[:i] + spaces[i + 1:]
    assert spaces[i][1] > decrement
    spaces[i][1] -= decrement
    return spaces

def BathroomStalls(N, K):
    spaces = [[N, 1]]
    clients = K - 1
    while clients > 0:
        max_space = spaces[0][0]
        ingoing = min(spaces[0][1], clients)
        spaces = AddSpaces(max_space / 2, ingoing, spaces)
        spaces = AddSpaces((max_space - 1) / 2, ingoing, spaces)
        spaces = DeleteSpaces(max_space, ingoing, spaces)
        clients -= ingoing
    return spaces[0][0] / 2, (spaces[0][0] - 1) / 2

#inpath = "C-sample.in"
inpath = "C-large.in"
#inpath = "simulated.in"
#inpath = "C-small-2-attempt0.in"
outpath = "C.out"

fin = open(inpath)
fout = open(outpath, 'w')

timestart = time()

T = int(fin.readline())
for case in range(1, T+1):
    N, K = map(int, fin.readline().split())
    max_s, min_s = BathroomStalls(N, K)
    fout.write("Case #%d: %d %d\n" % (case, max_s, min_s))

fin.close()
fout.close()
print "%.4f" % (time() - timestart)
