# Julie
# April, 19 2018
# Round 1B
# "Mysterious Road Signs"

from time import time

class Sign:
    def __init__(self, d, a, b):
        self.westroad = d + a
        self.eastroad = d - b

    def road(self, letter):
        assert letter == 'W' or letter == 'E', letter
        if letter == 'W':
            return self.westroad
        else:
            return self.eastroad

    def otherroad(self, letter):
        assert letter == 'W' or letter == 'E', letter
        if letter == 'E':
            return self.westroad
        else:
            return self.eastroad


def DestFirst(signs, dest):
    max_start = 0
    max_count = 0
    max_pool = set()

    start = 0
    while start is not None and start < len(signs):
        if len(signs) - start < max_count:
            break
        firstdest = signs[start].road(dest)
        seconddest = None
        destbreak = None    # the first sign with another firstdest
        nxt = start + 1
        while nxt < len(signs):
            if signs[nxt].road(dest) == firstdest or signs[nxt].otherroad(dest) == seconddest:
                nxt += 1
                continue
            if seconddest is None:
                seconddest = signs[nxt].otherroad(dest)
                destbreak = nxt
                nxt += 1
                continue
            break
            # end of sequence
        length = nxt - start
        if length > max_count:
            max_count = length
            max_pool = set((start,))
        elif length == max_count:
            max_pool.add(start)
        start = destbreak
    return max_count, max_pool


def MysteriousRoadSigns(signs):
    westf = DestFirst(signs, 'W')
    eastf = DestFirst(signs, 'E')
    if westf[0] > eastf[0]:
        return westf[0], len(westf[1])
    elif westf[0] < eastf[0]:
        return eastf[0], len(eastf[1])
    else:
        westf[1].update(eastf[1])
        return westf[0], len(westf[1])
       
T = int(input())

for case in range(1, T + 1):
    S = int(input())
    signs = []
    for s in range(S):
        d, a, b = map(int, input().split(' '))
        signs.append(Sign(d, a, b))
    result = MysteriousRoadSigns(signs)
    print("Case #%d: %s %s" % (case, result[0], result[1]))
                 
