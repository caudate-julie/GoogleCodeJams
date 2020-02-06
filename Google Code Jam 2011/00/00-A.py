# May, 6, 2011
# Qualification Round
# "Bot Trust"
# Kyra

from time import time

#inpath = "A-sample.in"
inpath = "A-large.in"
#inpath = 'A-small-attempt0.in'
outpath = "A.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

fout = open(outpath, 'w')
cases = int(lines.pop(0))
print "Cases:", cases

for n in range(1, cases+1):
    line = lines.pop(0).split()[1:]
    sequence = list((line[2*i], int(line[2*i+1])) for i in range(len(line)/2))
    orange_general = 0
    blue_general = 0
    orange_position = 1
    blue_position = 1
    while len(sequence) > 0:
        turn = sequence.pop(0)
        if turn[0] == "O":
            move = abs(turn[1] - orange_position)
            if orange_general > blue_general - move:
                orange_general += move + 1
            else:
                orange_general = blue_general + 1
            orange_position = turn[1]
        else:
            move = abs(turn[1] - blue_position)
            if blue_general > orange_general - move:
                blue_general += move + 1
            else:
                blue_general = orange_general + 1
            blue_position = turn[1]
    fout.write("Case #%d: %d\n" % (n, max(orange_general, blue_general)))

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
