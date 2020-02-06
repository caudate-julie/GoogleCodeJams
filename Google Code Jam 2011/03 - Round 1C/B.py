# May, 22, 2011
# Round 1C
# "Space Emergency"
# Kyra

from time import time

inpath = "B-sample.in"
#inpath = "B-large.in"
#inpath = 'B-small-attempt0.in'
outpath = "B.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

def Fly(boosters, booster_time, destination, distances):
    stars = distances*(destination/len(distances) + 1)
    
    return 0
    
fout = open(outpath, 'w')
cases = int(lines.pop(0))
print "Cases:", cases

for n in range(1, cases+1):
    data = map(int, lines.pop(0).split())
    boosters = data[0]
    booster_time = data[1]
    destination = data[2]
    distances = data[4:]
    flying_time = Fly(boosters, booster_time, destination, distances)
    fout.write("Case #%d: %d\n" % (n, flying_time))

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
