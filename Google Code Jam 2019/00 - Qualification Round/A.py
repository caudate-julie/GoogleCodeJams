# Julie
# April, 6, 2019
# Qualification Round
# "Foregone Solution"

from time import time

def MakeSum(check):
    first = ''
    second = ''
    for c in check:
        if c == '4':
            first += '3'
            second += '1'
        else:
            first += c
            second += '0'

    count = 0
    while second[count] == '0':
        count += 1
    second = second[count:]
    return (first, second)

       
N = int(input())

for case in range(1, N + 1):
    N = input()
    A, B = MakeSum(N)
    print("Case #%d: %s %s" % (case, A, B))
