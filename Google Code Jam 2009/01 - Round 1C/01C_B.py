# September, 13, 2009
# Round 1C
# "Center of Mass"
# - Kyra -
# done

from time import time
from math import sqrt

#inpath = "B-sample.in"
inpath = "B-large-practice.in"
#inpath = "B-small-practice.in"
outpath = "B.out"

EPS = -10

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

fout = open(outpath, 'w')
cases = int(lines[0])
curline = 1
print "Cases:", cases
for n in range(1, cases+1):
    fireflynum = int(lines[curline])
    fireflies = list(map(int, lines[i].split())
                     for i in range(curline+1, curline+fireflynum+1))
    curline += fireflynum+1
    startcoord = [float(sum(x[i] for x in fireflies))/fireflynum
                  for i in range(3)]
    avervel = [float(sum(x[i] for x in fireflies))/fireflynum
               for i in range(3, 6)]
    tdenom = sum(v**2 for v in avervel)
    tnumer = sum(startcoord[i]*avervel[i] for i in range(3))
    if tdenom < 10**EPS or tnumer > 0:
        tmin = 0
    else:
        tmin = - tnumer/tdenom
    dmin = sqrt(sum((startcoord[i]+avervel[i]*tmin)**2 for i in range(3)))
    print "Case #%d: %.6f %.6f" % (n, dmin, tmin)
    fout.write("Case #%d: %.6f %.6f\n" % (n, dmin, tmin))
print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
