# September, , 2009
# Round 1B
# "Decision Tree"
# Kyra

from time import time

#inpath = "A-sample.in"
inpath = "A-large.in"
#inpath = 'A-small-attempt0.in'
outpath = "A.out"

ts = time()
fin = open(inpath, 'r')
lines = fin.readlines()
fin.close()

class TreeNode(object):
    def __init__(self, w):
        self.parent = None
        self.left = None
        self.right = None
        self.weight = w
        self.feature = None
    def add(self, other, t):
        self.parent = other
        if t:
            other.left = self
        else:
            other.right = self

class DecTree(object):
    def __init__(self, w):
        self.root = TreeNode(w)
    def addsubtree (self, other, t):
        other.root.add(self.root, t)

def Decision(characters, tree):
    weight = 1
    curnode = tree.root
    while True:
        weight *= curnode.weight
        if curnode.feature is None:
            break
        if curnode.feature in characters:
            curnode = curnode.left
        else:
            curnode = curnode.right
    return weight
            
def DescrTree(s, pars, pref):
    tree = DecTree(float(s[0]))
    if len(s) == 1:
        return tree
    tree.root.feature = s[1]
    lim = pars[pref+2]-pref
    tree.addsubtree(DescrTree(s[3:lim], pars, pref+3), True)
    tree.addsubtree(DescrTree(s[lim+2:-1], pars, pref+lim+2), False)
    return tree
    
def MakeTree(treelines):
    s = ''
    for x in treelines:
        s += x[:-1]
    s = s.replace('(', ' ( ')
    s = s.replace(')', ' ) ')
    s = s.split()
    pars = {}
    for i in range(len(s)):
        if s[i] == '(':
            count = 0
            for j in range(i, len(s)):
                if s[j] == '(':
                    count += 1
                elif s[j] == ')':
                    count -= 1
                if count == 0:
                    pars[i] = j
                    pars[j] = i
                    break
    return DescrTree(s[1:-1], pars, 1)
    
fout = open(outpath, 'w')
cases = int(lines[0])
print "Cases:", cases
curline = 1
for n in range(1, cases+1):
    fout.write("Case #%d:\n" % n)
    treelines = int(lines[curline])
    treedescr = lines[curline+1:curline+treelines+1]
    curline += treelines + 1
    animalnum = int(lines[curline])
    animallines = list(lines[curline+1:curline+animalnum+1])
    animals = list(anline.split() for anline in animallines)
    curline += animalnum + 1
    tree = MakeTree(treedescr)
    for a in animals:
        fout.write('%.7f\n' % (Decision(a[2:], tree)))

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
