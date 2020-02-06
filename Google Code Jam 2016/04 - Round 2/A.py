# 2016 practice
# Round 2
# "Rather Perplexing Showdown"

from time import time
from math import log

#inpath = "A-sample.in"
#inpath = "A-bigsample.in"
#inpath = 'A-small-practice.in'
inpath = "A-large-practice.in"
outpath = "A.out"

fin = open(inpath)
fout = open(outpath, 'w')

class Node:
    def __init__(self, parent):
        self.parent = parent
        self.left = None
        self.right = None
        self.value = None

    def add_levels(self, count):
        if count == 0:
            return
        if self.left is None:   self.left = Node(self)
        if self.right is None:  self.right = Node(self)
        self.left.add_levels(count - 1)
        self.right.add_levels(count - 1)

    def leftmost_child(self):
        current = self
        while True:
            if current.left is None:  return current
            current = current.left    

    def next(self, top):
        current = self
        while not current is top and current.parent.right is current:
            current = current.parent
        if current is top: return None
        current = current.parent.right
        return current.leftmost_child()

    def sort(self):
        if self.left is None or self.right is None:
            return
        self.left.sort()
        self.right.sort()
        l = self.left.leftmost_child()
        r = self.right.leftmost_child()
        while not l is None and not r is None and l.value == r.value:
            l = l.next(self.left)
            r = r.next(self.right)
        if l is None or r is None:
            assert l is None and r is None
            return
        if l.value < r.value:
            return
        self.left, self.right = self.right, self.left
        return

    # P = 0, R = 1, S = 2
    def set_children_values(self):
        if self.left is None or self.right is None:
            assert self.left is None and self.right is None
            return
        self.left.value = self.value
        self.right.value = (self.value + 1) % 3
        self.left.set_children_values()
        self.right.set_children_values()

class PlayersTree:


    def __init__(self, depth):
        self.root = Node(None)
        self.root.add_levels(depth)
        self.depth = depth


    def get_result(self):
        res = ''
        letters = ['P', 'R', 'S']
        current = self.root.leftmost_child()
        while not current is None:
            res += letters[current.value]
            current = current.next(self.root)
        return res

    def show_tree(self):
        print 
        letters = ['P', 'R', 'S']
        result = []
        queue = [self.root]
        while len(queue) > 0:
            current = queue.pop(0)
            result.append(letters[current.value])
            if current.left is None or current.right is None:
                assert current.left is None and current.right is None
                continue
            queue += [current.left, current.right]
        for i in range(len(result)):
            if log(i + 1, 2) == int(log(i + 1, 2)):
                print
            print result[i],
        print

# P = 0, R = 1, S = 2
def RockPaperScissors(N, R, P, S):
    if R == P and abs(S - R) == 1:
        winner = (2 + N) % 3
    elif P == S and abs(R - S) == 1:
        winner = (1 + N) % 3
    elif S == R and abs(P - S) == 1:
        winner = N % 3
    else:
        return "IMPOSSIBLE"
    game = PlayersTree(N)
    game.root.value = winner
    game.root.set_children_values()
    #game.show_tree()
    game.root.sort()
    #game.show_tree()
    return game.get_result()

    return "Possible"



timestart = time()
T = int(fin.readline())
for case in xrange(1, T + 1):
    N, R, P, S = map(int, fin.readline().split(' '))
    answer = RockPaperScissors(N, R, P, S)
    #print answer
    fout.write("Case #%d: %s\n" % (case, answer))
    
print "\nTime elapsed: %.4f" % (time() - timestart)

fin.close()
fout.close()