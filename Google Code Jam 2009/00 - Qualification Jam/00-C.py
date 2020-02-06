# September, 3, 2009
# Qualification Round
# "Welcome to Code Jam"

from time import time
DIG_NUM = 4

#inpath = "C-sample.in"
inpath = "C-large.in"
#inpath = 'C-small-attempt0.in'
outpath = "C.out"

def OneWelcomeString(plen, letters, s):
    curletter = 0
    count = [0]*plen + [1]
    for c in s:
        if letters.has_key(c):
            for n in letters[c]:
                count[n] += count[n-1]
    return count[-2]    

# I must say that I assume no double letters in the pattern string
def Welcome(inpath, outpath, pattern):
    fin = open(inpath)
    fout = open(outpath, 'w')
    s = fin.readline()
    iternum = int(s.split()[0])
    letters = {}
    for i in range(len(pattern)):
        if letters.has_key(pattern[i]):
            letters[pattern[i]] += [i]
        else:
            letters[pattern[i]] = [i]
    for k in range(iternum):
        s = list(fin.readline())
        res = str(OneWelcomeString(len(pattern), letters, s))
        while len(res) < DIG_NUM:
            res = '0' + res
        fout.write("Case #%d: %s\n" % (k+1, res[-4:]))
    fin.close
    fout.close
    return

ts = time()
pattern = 'welcome to code jam'
Welcome (inpath, outpath, pattern)
print "Time:", round(time() - ts, 4)
