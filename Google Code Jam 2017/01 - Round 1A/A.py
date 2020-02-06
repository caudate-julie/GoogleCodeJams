# Julie
# -- practice --
# Round 1A
# "Alphabet Cake"

from time import time
from copy import copy
from random import randint

def AlphabetCake(cake, R, C):
	children = list(letter for row in cake for letter in row if not letter == "?")
	assign_pieces = dict((c, 0) for c in children)
	for i in range(R):
		for j in range(C):
			if not cake[i][j] == '?':
				assign_pieces[cake[i][j]] |= 


inpath = "A-sample.in"
#inpath = "simulated.in"
#inpath = "A-large.in"
#inpath = 'A-small-attempt0.in'
outpath = "A.out"

fin = open(inpath)
fout = open(outpath, 'w')
       
timestart = time()
N = int(fin.readline())

for case in range(1, N + 1):
	R, C = map(int, fin.readline().split(' '))
	cake = []
	for row in range(R):
		cake.append(fin.readline()[:C]);
	result = AlphabetCake(cake, R, C)
	print result
    #fout.write("Case #%d: %s\n" % (case))
    #for row in range(R):
    #	fout.write("%s\n" % (result[row]))
                 
print "\ntime elapsed: %.4f" % (time() - timestart)
fin.close()
fout.close()

