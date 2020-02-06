# September, 12, 2009
# Round 1B
# "The Next Number"
# - Kyra -

from time import time

#inpath = "B-sample.in"
inpath = "B-large.in"
#inpath = 'B-small-attempt4.in'
outpath = "B.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

def nullreversed (a):
    b = sorted(a)
    n = 0
    while b[0] == 0:
        del b[0]
        n += 1
    b = list(reversed(b))
    b[-1:-1] = [0]*n
    return b

fout = open(outpath, 'w')
cases = int(lines[0])
for n in range(1, cases+1):
    number = int(lines[n]) 
    digits = []
    while number > 0:
        digits.append(number%10)
        number /= 10
    i = 0
    if len(digits) == 1:
        res = digits[0]*10
    elif digits == sorted(digits):
        digits = list(nullreversed(digits))
        digits[-1:-1] = [0]
        res = sum(digits[i]*10**i for i in range(len(digits)))
    else:
        while digits[i] <= digits[i+1]:
            i += 1
        chdig = digits[i+1]
        t = sorted(digits[:i+2])
        for j in range(len(t)):
            if t[j] > chdig:
                maxdig = t.pop(j)
                break
        t = list(reversed(t)) + [maxdig]
        digits[:i+2] = t
        res = sum(digits[i]*10**i for i in range(len(digits)))
    fout.write("Case #%d: %d\n" % (n, res))

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
