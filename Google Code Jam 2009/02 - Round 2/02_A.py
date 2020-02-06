# September, 26, 2009
# Round 2
# ""
# - Kyra -

from time import time

#inpath = "A-sample.in"
inpath = "A-large.in"
#inpath = "A-small-attempt1.in"
outpath = "A.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

def Value(x, m, c):
    if c not in x:
        return 0
    return m - 1 - x.index(c)

def minswaps(matrix):
    m = len(matrix)
    ranks = list(Value(x, m, '1') for x in matrix)
    swaps = 0
    for i in range(m-1):
        if ranks[i] <= i:
            continue
        k = min(j for j in range(i+1, m) if ranks[j] <= i)
        ranks[i:i] = [ranks[k]]
        del ranks[k+1]
        swaps += k - i
    return swaps

fout = open(outpath, 'w')
cases = int(lines[0])
print "Cases:", cases
lines[-1] += '\n'
curline = 1
for n in range(1, cases+1):
    rows = int(lines[curline])
    matrix = list(list(reversed(a[:-1])) for a in lines[curline+1:curline+rows+1])
    curline += rows + 1
    result = minswaps(matrix)
    fout.write("Case #%d: %d\n" % (n, result))

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
