from random import randrange

out = 'simulated.in'
fout = open(out, 'w')

fout.write('3\n')
for T in range(3):
    fout.write(f'{10**5}\n')
    for i in range(10**5):
        fout.write(f'{i * 10} {randrange(10**6)} {randrange(10**6)}\n')
fout.close