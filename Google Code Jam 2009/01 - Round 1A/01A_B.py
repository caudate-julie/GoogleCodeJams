# September, 12, 2009
# Round 1A
# "Crossing the Road"
# - Kyra -

from time import time

inpath = "B-sample.in"
#inpath = "B-large-practice.in"
#inpath = 'B-small-practice.in'
outpath = "B.out"
BLOCTIME = 2
ROADTIME = 1
MAX = 10
#MAX = 10**7

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

def GoTime(knot, direction, gtime):
    if (knot[direction[0]]+direction[1])%2 == 1:
        return BLOCTIME
    S, W, T = lights[knot[0]/2][knot[1]/2]
    period = S + W
    while T < gtime:
        T += period
    while T > gtime:
        T -= period
    if direction[0] == 0:
        if gtime - T <= S:
            return ROADTIME
        return period - gtime + ROADTIME
    else:
        if gtime - T <= S:
            return ROADTIME
        return period - gtime + ROADTIME

fout = open(outpath, 'w')
cases = int(lines[0])
curline = 1
for n in range(1, cases+1):
    hroads, vroads = map(int, lines[curline].split())
    lights = []
    for x in range(hroads):
        roadline = map(int, lines[curline+x+1].split())
        roadlights = []
        while len(roadline) > 0:
            roadlights.append(roadline[:3])
            del roadline[:3]
        lights.append(roadlights)
    curline += hroads + 1
    corners = [[MAX*2*(hroads+vroads)]*2*vroads for i in range(2*hroads)]
    corners[-1][0] = 0
    flag = True
    print "CASE:", n
    for x in range(hroads):
        for y in range(vroads):
            print GoTime((x, y), (0, 0), 0), GoTime((x, y), (1, 0), 0)
        print
                        
    fout.write("Case #%d: " % n)
    fout.write('\n')

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
