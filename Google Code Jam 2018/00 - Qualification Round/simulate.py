from random import randrange
from random import random

out = 'simulated.in'
fout = open(out, 'w')

fout.write('100\n')
for i in range(100):
	fout.write('%.6f\n' % (random() * 0.414213 + 1))
fout.close