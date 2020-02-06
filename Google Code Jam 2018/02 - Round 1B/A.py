# Julie
# April, 29, 2018
# Round 1B
# "Rounding Error"

from time import time

def Remainder(x, N):
    return x / N - x // N


def AddUpRemainders(roundsUp, roundsDown, N):
    return sum(x // N + 1 for x in roundsUp) + sum(x // N for x in roundsDown)


def Increase(x, N):
    if Remainder(100, N) == 0:
        return None
    count = 0
    while Remainder(x, N) < 0.5:
        x += 100
        count += 1
    return count

def RoundingError(N, C):
    unanswered = N - sum(C)
    C = [x * 100 for x in C]

    onerem = Remainder(100, N)
    if onerem >= 0.5:
        C += [100] * unanswered
        unanswered = 0

    C.sort(key=lambda x: Remainder(x, N), reverse=True)
    roundsUp = []
    roundsDown = []

    for index, x in enumerate(C):
        incr = Increase(x, N)
        if incr is None or incr > unanswered or Remainder(x, N) < onerem:
            roundsDown = C[index:]
            break
        roundsUp.append(x + incr * 100)
        unanswered -= incr

    onesets = Increase(0, N)
    if onesets is not None:
        roundsUp += [onesets * 100] * (unanswered // onesets)
        unanswered -= (unanswered // onesets) * onesets
    roundsDown += [100 * unanswered]

    return AddUpRemainders(roundsUp, roundsDown, N)

T = int(input())

for case in range(1, T + 1):
    N, _ = map(int, input().split(' '))
    C = list(map(int, input().split(' ')))
    result = RoundingError(N, C)
    print("Case #%d: %s" % (case, result))
                 
