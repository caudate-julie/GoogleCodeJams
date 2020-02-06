# May, 6, 2011
# Qualification Round
# "GoroSort"
# Kyra

from time import time

#inpath = "C-sample.in"
inpath = "C-large.in"
#inpath = 'C-small-attempt0.in'
outpath = "C.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

def GetDigits(a):
    digits = []
    while a > 0:
        digits.append(a%2)
        a /= 2
    return digits

def GetInteger(a):
    return sum(a[i]*2**i for i in range(len(a)))

def PatrickSum(a, b):
    d = max(len(a), len(b))
    a += [0]*(d - len(a))
    b += [0]*(d - len(b))
    c = [(a[i]+b[i]) % 2 for i in range(d)]
    return c

fout = open(outpath, 'w')
cases = int(lines.pop(0))
print "Cases:", cases

for n in range(1, cases+1):
    candy = int(lines.pop(0))
    pieces = map(int, lines.pop(0).split())
    sean_sum = GetInteger(reduce(PatrickSum, map(GetDigits, pieces)))
    if not sean_sum == 0:
        fout.write("Case #%d: NO\n" % n)
    else:
        fout.write("Case #%d: %d\n" % (n, sum(pieces) - min(pieces)))
                          

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
