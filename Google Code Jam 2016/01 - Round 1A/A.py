# April, 16, 2016
# Kyra
# Round 1A
# "The Last Word"

from time import time

#inpath = "A-sample.in"
inpath = "A-large-practice.in"
#inpath = 'A-small-practice.in'
outpath = "A.out"

def AddLetter(word, c):
    if word == "":
        return c
    if c > word[0]:
        return c + word
    if c < word[0]:
        return word + c
    else:
        return word[0] + AddLetter(word[1:], c)

def LastWord(S):
    myword = S[0]
    for c in S[1:]:
        myword = AddLetter(myword, c)
    return myword

def LastWordNoRecursion(S):
    myword = S[0]
    for c in S[1:]:
        compare = 0
        while compare < len(myword) and myword[compare] == c:
            compare += 1
        if compare == len(myword) or c > myword[compare]:
            myword = c + myword
        else:
            myword = myword + c
    return myword
            

fin = open(inpath)
fout = open(outpath, 'w')

timestart = time()
T = int(fin.readline())
for case in range(1, T+1):
    S = fin.readline().strip("\n")
    result = LastWordNoRecursion(S)
    #print result
    fout.write("Case #%d: %s\n" % (case, result))
    
fin.close()
fout.close()
print "\nTime: %.4f" % (time() - timestart)
