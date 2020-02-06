# September, 13, 2009
# Round 1C
# "All Your Base"
# - Kyra -
# done

from time import time

#inpath = "A-sample.in"
inpath = "A-large-practice.in"
#npath = "A-small-practice.in"
outpath = "A.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

fout = open(outpath, 'w')
cases = int(lines[0])
print "Cases:", cases
for n in range(1, cases+1):
    s = lines[n].split()[0]
    symbols = []
    for c in s:
        if c not in symbols:
            symbols.append(c)
    if len(symbols) == 1:
        result = 2**len(s) - 1
    else:
        base = len(symbols)
        null = symbols.pop(1)
        symbols[:0] = [null]
        s = list(reversed(list(s)))
        result = sum(symbols.index(s[i])*base**i for i in range(len(s)))
#    print n, result        
    fout.write("Case #%d: %d\n" % (n, result))

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
