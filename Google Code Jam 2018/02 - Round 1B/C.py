# Julie
# April, 29, 2018
# Round 1B
# "Transmutation"

from time import time
from collections import deque

def DepthTransmute(formulae, treasury, needed, todo):
    assert needed in todo
    alef, beth = formulae[needed]

    if alef in todo or beth in todo:
        return False
    if treasury[alef] > 0:
        treasury[alef] -= 1
    else:
        todo.add(alef)
        if not DepthTransmute(formulae, treasury, alef, todo):
            return False

    if treasury[beth] > 0:
        treasury[beth] -= 1
    else:
        todo.add(beth)
        if not DepthTransmute(formulae, treasury, beth, todo):
            return False

    treasury[needed] += 1
    todo.remove(needed)
    return True


def Transmutation(formulae, treasury):
    todo = set()
    while True:
        assert len(todo) == 0
        todo.add(0)
        if not DepthTransmute(formulae, treasury, 0, todo):
            return treasury[0]
       
N = int(input())

for case in range(1, N + 1):
    M = int(input())
    formulae = [tuple(map(lambda x: int(x)-1, input().split(' '))) for i in range(M)]
    treasury = list(map(int, input().split(' ')))
    result = Transmutation(formulae, treasury)
    print("Case #%d: %s" % (case, result))
                 
