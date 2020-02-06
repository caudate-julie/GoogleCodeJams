# May, 21, 2011
# Round 1B
# "Revenge of the Hot Dogs"
# Kyra

from time import time

#inpath = "B-sample.in"
#inpath = "B-large.in"
inpath = 'B-small-practice.in'
outpath = "B.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

def Timing(points, positions, distance):
    start = positions[0][0]
    ways = []
    for i in range(points):
        point = positions[i]
        line = (point[1] - 1) * distance
        ways += [start - point[0], start + line - point[0]]
        start += line + distance
    m = min(ways)
    n = max(ways)
    print m, n
    return float(n - m) / 2
    
fout = open(outpath, 'w')
cases = int(lines.pop(0))
print "Cases:", cases

for n in range(1, cases+1):
    points, distance = map(int, lines.pop(0).split())
    positions = []
    for i in range(points):
        positions.append(map(int, lines.pop(0).split()))                     
    best_time = Timing(points, positions, distance)
    fout.write("Case #%d: %f\n" % (n, round(best_time, 8)))

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
