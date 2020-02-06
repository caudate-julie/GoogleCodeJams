from random import randrange
import math

f = open('D-sample.in', 'w')
g = open('answ.in', 'w')
T = 100
f.write(f'{T}\n')

nxt = { '0' : '1', '1' : '0' }


def expect(i, N, L):
    num = N // L
    if i < num:
        return L
    if i == num:
        return N - L * num
    return 0

def make_request(N, L):
    result = []
    symbol = '1'
    for i in range(math.ceil(N / L)):
        symbol = nxt[symbol]
        result.append(symbol * expect(i, N, L))
    return ''.join(result)


for case in range(T):
    N = randrange(2, 1024)
    B = randrange(1, min(15, N - 1))
    F = 5
    f.write(f'{N} {B} {F}\n')

    brokens = []
    while len(brokens) < B:
        b = randrange(0, N)
        if b not in brokens:
            brokens.append(b)

    g.write(repr(sorted(brokens)))
    g.write('\n')
    
    for i in range(5):
        r = make_request(N, 2 ** i)
        for i in range(N):
            if i not in brokens:
                f.write(r[i])
        f.write('\n')
    f.write('1\n')

f.close()
g.close()