# May, 8, 2010
# Qualification Round
# "Theme Park"

from time import time

#inpath = "C-sample.in"
inpath = "C-large.in"
#inpath = 'C-small-attempt0.in'
outpath = "C.out"

timestart = time()

fin = open(inpath)
fout = open(outpath, 'w')

def GetMoney(roller, start, n):
    money = 0
    count = start
    for i in range(n):
        money += roller[count][0]
        count = roller[count][1]
    return money

def GetCycle(roller):
    cycle = end = lenght = 0
    cells = [True]*len(roller)
    while cells[cycle]:
        cells[cycle] = False
        cycle = roller[cycle][1]
        end += 1
    cycle_2 = cycle
    while True:
        cycle_2 = roller[cycle_2][1]
        lenght += 1
        if cycle_2 == cycle: break
    return (end - lenght, lenght, cycle)

def Gain (R, k, N, groups):
    roller = []
    for i in range(N):
        count = end = i
        money = 0
        seats = k
        while groups[count] <= seats:
            seats -= groups[count]
            money += groups[count]
            count = (count+1)%N
            if count == end: break
        roller.append((money, count))
    before, lenght, start = GetCycle(roller)
    a = GetMoney(roller, 0, before)
    b = GetMoney(roller, start, lenght)*(R/lenght)
    c = GetMoney(roller, start, (R-before)%lenght)
    return a + b + c
    
T = int(fin.readline())
for case in range(1, T+1):
    R, k, N = map(int, fin.readline().split())
    groups = map(int, fin.readline().split())
    fout.write("Case #%d: %d\n" % (case, Gain(R, k, N, groups)))
    #print case
    
fin.close()
fout.close()
print "%.4f" % (time() - timestart)
