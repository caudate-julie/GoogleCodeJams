# September, 3, 2009
# Qualification Round
# "Alien Language"

from time import time

#inpath = "A-sample.in"
inpath = "A-large.in"
#inpath = 'A-small-attempt0.in'
outpath = "A.out"

def DichSearch(seq, s):
    n = len(s)
    a = 0
    c = len(seq)
    while True:
        if c - a == 1:
            return seq[a][:n] == s[:n]
        if a == c:
            return False
        b = (a+c)/2
        if seq[b][:n] == s[:n]:
            return True
        elif seq[b] > s:
            c = b
        else:
            a = b 

def Read1Line (s):
    numberlist = []
    t = s.split()
    for c in t:
        numberlist.append(int(c))
    return numberlist

##def ListVariants(words, s, L, letter, curword):
##    if letter >= L:
##        return 1
##    num = 0
##    for c in s[letter]:
##        curword += c
##        if not DichSearch(words, curword):
##            curword = curword[:-1]
##            continue
##        num += ListVariants(words, s, L, letter+1, curword)
##        curword = curword[:-1]
##    return num           
##
##def ListSearch (fpath):
##    f = open(fpath)
##    s = f.readline()
##    words = []
##    [L, D, N] = Read1Line(s)
##    for i in range(D):
##        s = f.readline()
##        words.append(s[:L])
##    words.sort()
##    for i in range(N):
##        s = list(f.readline())
##        misword = []
##        while len(s) > 0:
##            if s == ['\n']:
##                break
##            if s[0] != '(':
##                misword.append([s.pop(0)])
##            else:
##                fin = s.index(')')
##                misword.append(s[1:fin])
##                del s[:fin+1]
##        newres = ListVariants(words, misword, L, 0, '')
##        print "Case #%d:" % (i+1),
##        print newres
##    return

def DictVariants(words, s, L, letter, curword):
    if letter >= L:
        return 1
    num = 0
    for c in s[letter]:
        curword += c
        if not words.has_key(curword):
            curword = curword[:-1]
            continue
        num += DictVariants(words, s, L, letter+1, curword)
        curword = curword[:-1]
    return num           

def DictSearch (inpath, outpath):
    fin = open(inpath)
    fout = open(outpath, 'w')
    s = fin.readline()
    words = {}
    [L, D, N] = Read1Line(s)
    for i in range(D):
        s = fin.readline()
        for i in range(L):
            words[s[:i+1]] = None
    res = []
    for i in range(N):
        s = list(fin.readline())
        misword = []
        while len(s) > 0:
            if s == ['\n']:
                break
            if s[0] != '(':
                misword.append([s.pop(0)])
            else:
                j = s.index(')')
                misword.append(s[1:j])
                del s[:j+1]
        newres = DictVariants(words, misword, L, 0, '')
        res.append("Case #%d: %d\n" % (i+1, newres))
    fin.close()
    for s in res:
        fout.write(s)
    fout.close()
    return

ts = time()
DictSearch (inpath, outpath)
print "Time:", round(time() - ts, 4)
