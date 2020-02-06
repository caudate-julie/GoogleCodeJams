from itertools import *
import re

def solveA(input, output):
	l, d, n = map(int, input.readline().split())
	words = set(w.strip() for w in islice(input, d))
	for casen, rx in enumerate(islice(input, n)):
		rx = rx.strip()
		rx = rx.replace('(', '[')
		rx = rx.replace(')', ']')
		rx = re.compile(rx)
		cnt = 0
		for w in words:
			if rx.match(w):
				cnt += 1
		output.write('Case #%d: %d\n' % (casen + 1, cnt))


solveA(open('A-large.in', 'r'), open('A-large.out', 'w'))

print 'Yay!' 