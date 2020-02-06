# May, 22, 2011
# Round 1C
# "Perfect Harmony"
# Kyra

from time import time

#inpath = "C-sample.in"
#inpath = "C-large.in"
inpath = 'C-small-practice.in'
outpath = "C.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

def LCD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

def LCM(a, b):
    if a == 0 or b == 0:
        return a + b
    return a * b / LCD(a, b)

def Harmony(L, H, players):
    if L == 1:
        return 1
    players.sort()
    i = 0
    while i < len(players) - 1:
        d = players[i]
        while i < len(players) - 1 and players[i+1] == d:
            del players[i+1]
        i += 1
    multiple = 1
    left = 0
    
    # dealing with left tail
    while left < len(players) and players[left] < L:
        multiple = LCM(multiple, players[left])
        left += 1
    if multiple > H:
        return None
    right = len(players) - 1

    divisible = 0
    divisibles = []

    # dealing with right tail
    while right >= 0 and players[right] > H:
        divisible = LCD(divisible, players[right])
        right -= 1
    right_edge = right

    # tail condition
    if divisible % multiple != 0 or (divisible != 0 and divisible < L):
        return None

    # adding right tail
    while divisible % multiple == 0 and right >= left:
        divisibles.append(divisible)
        divisible = LCD(divisible, players[right])
        if divisible < L:
            divisible = divisibles.pop(-1)
            break
        right -= 1

    # adding left tail
    while left <= right:
        multiple = LCM(multiple, players[left])
        if multiple > H:
            return None
        left += 1

    # left tails goes to the right
    while not divisible % multiple == 0 or left <= right_edge:
        divisible = divisibles.pop(-1)
        multiple = LCM(multiple, players[left])
        if multiple > H:
            return None
        left += 1
        right += 1
    result = multiple
    while result < L or not divisible % result == 0:
        result += multiple
        if result > H or result > divisible:
            return None
    return result

fout = open(outpath, 'w')
cases = int(lines.pop(0))
print "Cases:", cases

for n in range(1, cases+1):
    N, L, H = map(int, lines.pop(0).split())
    players = map(int, lines.pop(0).split())
    note = Harmony(L, H, players)
    if note is None:
        fout.write("Case #%d: NO\n" % n)
    else:
        fout.write("Case #%d: %d\n" % (n, note))

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
