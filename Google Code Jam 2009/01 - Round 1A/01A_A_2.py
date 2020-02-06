# September, 12, 2009
# Round 1A
# "Multi-base happiness"
# Kyra

def SetDigits(n, base):
    digits = []
    while n != 0:
        digits.append(n%base)
        n /= base
    digits.sort()
    while digits[0] == 0:
        del digits[0]
    return digits

def HappyIntBase (n, base):
    digits = SetDigits(n, base)
    sequences = [digits]
    while True:
        sqsum = 0
        for x in digits:
            sqsum += x**2
        if sqsum == 1:
            return True
        digits = SetDigits(sqsum, base)
        if digits in sequences:
            return False
        sequences.append(digits)
    
from time import time

#inpath = "A-sample.in"
#inpath = "A-large-practice.in"
inpath = 'A-small-practice.in'
outpath = "A1.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

fout = open(outpath, 'w')
cases = int(lines[0])
subs = {}
happyints = [[] for i in range(11)]
for i in range(2, 11):
    n = 2
    while not HappyIntBase(n, i):
        n += 1
    happyints[i].append(n)
print "Cases:", cases
for n in range(1, cases+1):
    bases = map(int, lines[n].split())
    m = len(bases)
    for i in range(2**m):
        subseq = []
        for j in range(m):
            if i&2**j:
                subseq.append(bases[j])
        subseq = tuple(subseq)
        if subs.has_key(subseq) and subs[subseq] > happyint:
            happyint = subs[subseq]
    baseints = list(happyints[b] for b in bases)
    if n == 4:
        print list(x[0] for x in baseints)
    happymax = min(ints[-1] for ints in baseints)
    for i in range(len(bases)):
        j = 0
        while j<len(baseints[i]):
            flag = True
            for ints in (baseints[:i]+baseints[i:]):
                if baseints[i][j] not in ints:
                    flag = False
                    del baseints[i][j]
                    break
            if flag:
                j += 1
    ints = min(baseints)
    if len(ints) > 0:
        happyint = ints[0]
    else:
        happyint = happymax
        happiness = False
        while not happiness:
            happyint += 1
            happiness = True
            for b in bases:
                if HappyIntBase(happyint, b):
                    happyints[b].append(happyint)
                else:
                    happiness = False                  
    subs[tuple(bases)] = happyint
    fout.write("Case #%d: %d\n" % (n, happyint))
    if n%10 == 0:
        print "Case #%d: %d" % (n, happyint)
        print "curtime:", round(time() - ts, 4)

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
