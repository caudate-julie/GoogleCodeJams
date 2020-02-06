from random import randrange

out = 'simulated.in'
fout = open(out, 'w')

fout.write("100\n")
for i in range(100):
    fout.write("1000 1000\n")
    for _ in range(1000):
        fout.write("%d %d\n" % (randrange(10 ** 6), randrange(10 ** 6)))
fout.close