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

inpath = "A-sample.in"
#inpath = "A-large-practice.in"
#inpath = 'A-small-practice.in'
outpath = "A.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

fout = open(outpath, 'w')
cases = int(lines[0])
subs = {}
print "Cases:", cases
for n in range(1, cases+1):
    bases = map(int, lines[n].split())
    happyint = 1
    happiness = False
    m = len(bases)
    for i in range(2**m):
        subseq = []
        for j in range(m):
            if i&2**j:
                subseq.append(bases[j])
        subseq = tuple(subseq)
        if subs.has_key(subseq) and subs[subseq] > happyint:
            happyint = subs[subseq]
    while not happiness:
        happyint += 1
        happiness = True
        for b in bases:
            if not HappyIntBase(happyint, b):
                happiness = False
                break
    subs[tuple(bases)] = happyint
    fout.write("Case #%d: %d\n" % (n, happyint))
    if n%10 == 0:
        print "Case #%d: %d" % (n, happyint)
        print "curtime:", round(time() - ts, 4)

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
