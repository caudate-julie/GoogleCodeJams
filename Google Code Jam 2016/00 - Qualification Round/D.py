# April, 10, 2016
# Qualification Round
# "Fractiles"

from time import time
from math import ceil

#inpath = "D-sample.in"
inpath = "D-large.in"
#inpath = 'D-small-attempt1.in'
outpath = "D.out"

timestart = time()

fin = open(inpath)
fout = open(outpath, 'w')

def IntoDec(line, base):
    return sum(line[-i-1] * base ** i for i in range(len(line)))

def Fractile(K, C, S):
    if C * S < K:
        return ["IMPOSSIBLE"]
    result = []
    digit = 0
    for i in range(ceil(float(K) / C)):
        word = []
        for j in range(C):
            #word.append(min(digit, K - 1))
            if digit == K:
                word.append(0)
            else:
                word.append(digit)
            digit = min(digit + 1, K)
        result += [IntoDec(word, K) + 1]
        assert result[-1] <= K ** C
    return result
        
    
T = int(fin.readline())
for case in range(1, T+1):
    K, C, S = map(int, fin.readline().split())
    fout.write("Case #%d: " % case)
    for x in Fractile(K, C, S):
        fout.write("%s " % str(x))
    fout.write("\n")
    
fin.close()
fout.close()
print "%.4f" % (time() - timestart)
