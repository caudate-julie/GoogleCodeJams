# Julie
# April, 7, 2018
# Qualification Round
# "Saving The Universe Again"

from time import time

def Damage(P):
    dmg = 1
    total = 0
    for x in P:
        if x == 'C':    dmg *= 2
        elif x == 'S':  total += dmg
        else:           raise ValueError('wrong char', x)
    return total

def Change(P):
    i = P.rfind('CS')
    if i == -1:
        return
    return P[:i] + 'SC' + P[i+2:]

def SavingUniverseAgain(D, P):
    count = 0
    while Damage(P) > D:
        P = Change(P)
        if P is None:
            return 'IMPOSSIBLE'
        count += 1
    return count
       
N = int(input())

for case in range(1, N + 1):
    D, P = input().split(' ')
    D = int(D)
    P = P.strip()
    result = SavingUniverseAgain(D, P)
    print("Case #%d: %s" % (case, result))
                 
