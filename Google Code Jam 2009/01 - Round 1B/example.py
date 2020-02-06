# September, , 2009
# Round 1B
# ""
# Kyra

from time import time

#inpath = "B-sample.in"
inpath = "B-large-practice.in"
#inpath = 'B-small-practice.in'
outpath = "B.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

fout = open(outpath, 'w')
cases = int(lines[0])
for n in range(1, cases+1):

    fout.write("Case #%d: " % n)
    fout.write('\n')

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
