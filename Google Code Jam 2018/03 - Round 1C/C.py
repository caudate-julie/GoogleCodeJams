# Julie
# 30.04.2017
# Round 1C
# "Core Training"

from time import time

def Probability_K_of_N(probabilities, K, current):
    probset = [[None] * (i + 2) for i in range(len(probabilities))]
    probset[0][0] = 1 - probabilities[0]
    probset[0][1] = probabilities[0]
    for i in range (1, len(probabilities)):
        probset[i][0] = probset[i - 1][0] * (1 - probabilities[i])
        for j in range(1, i + 1):
            probset[i][j] = probset[i - 1][j - 1] * probabilities[i] + probset[i - 1][j] * (1- probabilities[i])
        probset[i][i + 1] = probset[i - 1][i] * probabilities[i]
    #print
    #print probabilities
    #for x in probset: print x
    return sum(probset[-1][K:])

def CoreTraining(K, U, probabilities):
    cutoff = len(probabilities) - K   # we maximize last K elements: from cutoff to len(probabilities) - 1
    probabilities.sort()

    i = cutoff
    while i < len(probabilities) - 1 and U > 0:
        diff = probabilities[i + 1] - probabilities[i]
        units_spent = min(diff * (i - cutoff + 1), U) / (i - cutoff + 1)
        for j in range(cutoff, i + 1):
            probabilities[j] += units_spent
            U -= units_spent
            assert probabilities[j] <= 1
        #U -= units_spent * (i - cutoff + 1)
        i += 1

    if U > 0:
        units_spent = min(probabilities[cutoff] + U / K, 1) - probabilities[cutoff]
        for j in range(cutoff, len(probabilities)):
            probabilities[j]  += units_spent
            U -= units_spent
    assert (U < 10 ** -10) or all(x == 1 for x in probabilities[cutoff:])

    j = cutoff - 1
    while U > 0 and j >= 0: 
        units_spent = min(probabilities[j] + U, 1) - probabilities[j]
        probabilities[j]  += units_spent
        U -= units_spent
        j -= 1
    assert (U < 10 ** -10) or all(x == 1 for x in probabilities)

    return Probability_K_of_N(probabilities, K, 0)

#inpath = "C-sample.in"
#inpath = "C-large.in"
#inpath = "simulated.in"
inpath = "C-small-2-attempt6.in"
outpath = "C.out"

fin = open(inpath)
fout = open(outpath, 'w')

timestart = time()

T = int(fin.readline())
for case in range(1, T+1):
    N, K = map(int, fin.readline().split())
    U = float(fin.readline())
    probabilities = (map(float, fin.readline().split()))
    assert len(probabilities) == N

    result = CoreTraining(K, U, probabilities)
    print result
    fout.write("Case #%d: %.6f\n" % (case, result))

fin.close()
fout.close()
print "time elapsed: %.4f" % (time() - timestart)
