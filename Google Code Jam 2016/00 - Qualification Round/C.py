# April, 10, 2016
# Qualification Round
# "Coin Jam"

from time import time
from math import sqrt

inpath = "C-sample.in"
#inpath = "C-large.in"
#inpath = "C-small-attempt2.in"
outpath = "C.out"

timestart = time()

fin = open(inpath)
fout = open(outpath, 'w')

primes = [2, 3]

# n goes right-to-left
def ConvertToDec(n, base):
    return sum(n[i] * base ** i for i in range(len(n)))

def FindDivider(k):
    global primes
    for p in primes:
        if k % p == 0: return p
    new = primes[-1]
    while primes[-1] < sqrt(k):
        new += 2
        for p in primes:
            if p > sqrt(new):
                primes += [new]
                if k % new == 0:
                    return new
                break
    return -1

def AddDigit(m):
    for i in range(1, len(m)-1):
        if m[i] == 1:
            m[i] = 0
        else:
            m[i] = 1
            break
    return m

def FindNext(N, J):
    current = [0] * N
    current[0] = current[-1] = 1
    while J > 0:
        while True:
            dividers = []
            is_prime = False
            for base in range(2, 11):
                k = ConvertToDec(current, base)
                print k, base, ":", primes[-1]
                d = FindDivider(k)
                if d == -1:
                    is_prime = True
                    break
                else:
                    dividers += [d]
            if is_prime:
                current = AddDigit(current)
                print current
            else: break
        line = ''.join(map(str, reversed(current))) + ' ' \
               + ' '.join(map(str, dividers)) + '\n'
        print "\nANSWER:", line, "\n"
        fout.write(line)
        J -= 1
        current = AddDigit(current)

    
fin.readline()
N, J = map(int, fin.readline().split())

fout.write("Case #%1:\n")
FindNext(N, J)

fin.close()
fout.close()
print "%.4f" % (time() - timestart)
