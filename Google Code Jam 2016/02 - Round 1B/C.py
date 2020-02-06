# April, 16, 2016
# Kyra
# Round 1A
# "BFFs"

from time import time
from copy import copy

inpath = "C-sample.in"
#inpath = "C-large.in"
#inpath = 'C-small-attempt2.in'
outpath = "C.out"

def CloseCircle(BBFs, circle):
    

def AddFriend(BBFs, circle):
    

def FriendCircle(BBFs, N):
    maxlen = 0
    for i in xrange(N):
        circle = [i]
        

fin = open(inpath)
fout = open(outpath, 'w')

timestart = time()
T = int(fin.readline())
for case in range(1, T+1):
    N = int(fin.readline())
    BFFs = map(int, fin.readline().split(' '))
    assert len(BBFs) == N
    result = FriendCircle(BBFs, N)
    print result
    fout.write("Case #%d: %s\n" % (case, result))
    
fin.close()
fout.close()
print "\nTime: %.4f" % (time() - timestart)
