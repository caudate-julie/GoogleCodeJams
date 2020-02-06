from random import randrange

out = 'simulated.in'
fout = open(out, 'w')

fout.write("100\n")
for i in range(100):
    fout.write("900 200 100 200 100 200 100\n")
fout.close