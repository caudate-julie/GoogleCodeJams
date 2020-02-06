# Julie
# 30.04.2017
# Round 1C
# "Parenting Partnering"

from time import time
from math import sqrt

complements = {'': ['R', 'Y', 'B', 'GR', 'VY', 'OB'],
             'Y': ['VY', 'B', 'R'],
             'R': ['GR', 'B', 'Y'],
             'B': ['OB', 'Y', 'R']}

cycles = {'Y': ['V', 'B', 'R'],
             'R': ['G', 'B', 'Y'],
             'B': ['O', 'Y', 'R']}

def OneColors(colors):
    colors.sort(key=lambda x: x[0], reverse=True)
    result = (
              (colors[0][1] + colors[1][1] + colors[2][1]) * (colors[2][0] - colors[0][0] +colors[1][0])
              + (colors[0][1] + colors[1][1]) * (colors[0][0] - colors[2][0])
              + (colors[0][1] + colors[2][1]) * (colors[0][0] - colors[1][0])
              )
    return result

def Stable(unicorns):
    # N ==> R, O, Y, G, B, V
    if (unicorns['V'] > unicorns["Y"]
            or unicorns["O"] > unicorns["B"]
            or unicorns["G"] > unicorns["R"]):
        return "IMPOSSIBLE"
    if (unicorns["R"] + unicorns["O"] + unicorns['V'] > unicorns["N"] / 2
            or unicorns["Y"] + unicorns["O"] + unicorns["G"] > unicorns["N"] / 2
            or unicorns["G"] + unicorns["B"] + unicorns['V'] > unicorns["N"] / 2):
        return "IMPOSSIBLE"
    # now we pair every V with Y, every O with B and every G with R
    one_colored = [(unicorns['R'] - unicorns['G'], 'R'),
                   (unicorns['B'] - unicorns['O'], 'B'),
                   (unicorns['Y'] - unicorns['V'], 'Y')]
    basic = OneColors(one_colored)
    x = basic.find('Y')
    basic = basic[:x] + 'YV' * unicorns['V'] + basic[x:]
    x = basic.find('R')
    basic = basic[:x] + 'RG' * unicorns['G'] + basic[x:]
    x = basic.find('B')
    basic = basic[:x] + 'BO' * unicorns['O'] + basic[x:]
    return basic

#inpath = "B-sample.in"
#inpath = "simulated.in"
inpath = "B-large.in"
#inpath = 'B-small-attempt0.in'
outpath = "B.out"

fin = open(inpath)
fout = open(outpath, 'w')

timestart = time()

T = int(fin.readline())
for case in range(1, T + 1):
    unicorns = dict(zip(
        ("N", "R", "O", "Y", "G", "B", 'V'), 
        map(int, fin.readline().split())
    ))
    result = Stable(unicorns)
    #print result
    
    fout.write("Case #%d: %s\n" % (case, result))

fin.close()
fout.close()
print "%.4f" % (time() - timestart)
