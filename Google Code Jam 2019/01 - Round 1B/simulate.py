from random import randrange
from random import choice
import math

f = open('C-sim.in', 'w')
T = 8
f.write(f'{T}\n')

for case in range(T):
    f.write('100000 100000\n')
    for _ in range(100000):
        f.write(f'{randrange(0, 10**5)} ')
    f.write('\n')
    for _ in range(100000):
        f.write(f'{randrange(0, 10**5)} ')
    f.write('\n')

f.close()
