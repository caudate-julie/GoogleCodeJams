# September, 26, 2009
# Round 2
# ""
# - Kyra -

from time import time

inpath = "C-sample.in"
#inpath = "C-large.in"
#inpath = "C-small-attempt.in"
outpath = "C.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

fout = open(outpath, 'w')
cases = int(lines[0])
print "Cases:", cases
for n in range(1, cases+1):

    fout.write("Case #%d: %d\n" % (n, result))

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
