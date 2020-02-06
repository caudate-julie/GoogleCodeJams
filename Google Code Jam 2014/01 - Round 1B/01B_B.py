# Round 1B
# "New Lottery Game"
# - Kyra -
# April 3, 2014

from time import time

inpath = "B-sample.in"
#inpath = "B-large.in"
#inpath = 'B-small-attempt4.in'
outpath = "B.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

def Lottery(A, B, K):
    if A <= K or B <= K: return A * B
    count = A * K + B * K - K * K
    for a in range(K, A):
        for b in range(K, B):
            if a & b < K:
                count += 1
    return count

fout = open(outpath, 'w')
cases = int(lines[0])
for n in range(1, cases+1):
    A, B, K = map(int, lines[n].split())
    res = Lottery(A, B, K)
    print res
    fout.write("Case #%d: %d\n" % (n, res))

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
