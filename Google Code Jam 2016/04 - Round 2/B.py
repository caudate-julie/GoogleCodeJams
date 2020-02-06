# 2016 practice
# Round 2
# "Red Tape Committee"

from time import time
#from math import log

inpath = "B-sample.in"
#inpath = "B-bigsample.in"
#inpath = 'B-small-attempt0.in'
#inpath = "B-large.in"
outpath = "B.out"

fin = open(inpath)
fout = open(outpath, 'w')

from time import time

def OneVariantProbability(probs, choices):
	return reduce(lambda x, y: x * y, (probs[i] if choices & 2 ** i else 1 - probs[i] for i in range(len(probs))))

def HasChoices(N):
	choices = 0
	while N > 0:
		choices += N % 2
		N /= 2
	return choices

def SumProbability(committee):
	K = len(committee)
	return sum(OneVariantProbability(committee, n) for n in xrange(2 ** K) if HasChoices(n) == K / 2)

def MinAvailable(probabilities, chosen):
	i = len(probabilities) - 1
	while i >= 0 and chosen[i]:
		i -= 1
	return None if i < 0 else i

def MaxAvailable(probabilities, chosen):
	i = 0
	while i < len(probabilities) and chosen[i]:
		i += 1
	return None if i >= len(probabilities) else i

def ChangeMember(i, probabilities, chosen, p_sum):
	if p_sum - probabilities[i] < (K - 1) / 2:
		j = MaxAvailable(probabilities, chosen)
		if probabilities[i] >= probabilities[j]:
			return -1
		assert chosen[i] and not chosen[j]
		return j
	if p_sum - probabilities[i] > (K - 1) / 2:
		j = MinAvailable(probabilities, chosen)
		if probabilities[i] <= probabilities[j]:
			return -1
		assert chosen[i] and not chosen[j]
		return j

def ChooseCommittee(probabilities, K):
	chosen = [True] * K + [False] * (len(probabilities) - K)
	assert len(chosen) == len(probabilities)
	p_sum = sum(probabilities[:K])
	while True:
		switched = False
		for i in range(len(probabilities)):
			if not chosen[i]:
				continue
			j = ChangeMember(i, probabilities, chosen, p_sum) 
			if j == -1:
				continue
			chosen[i] = False
			chosen[j] = True
			p_sum += probabilities[j] - probabilities[i]
	return

def RedTapeCommittee(probabilities, K):
	probabilities.sort()
	print N, K
	print probabilities
	chosen = ChooseCommittee(probabilities, K)
	print chosen
	assert len(chosen) == K
	return SumProbability(chosen)

timestart = time()
T = int(fin.readline())
for case in range(1, T + 1):
	N, K = map(int, fin.readline().split(' '))
	probabilities = map(float, fin.readline().split(' '))
	assert len(probabilities) == N
	answer = RedTapeCommittee(probabilities, K)
	print answer
	fout.write("Case #%d: %s\n" % (case, answer))

print "\nTime elapsed: %.4f" % (time() - timestart)
fin.close()
fout.close()
