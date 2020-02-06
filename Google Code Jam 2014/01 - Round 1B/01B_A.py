# Round 1B
# "The Repeater"
# Kyra
# April 3, 2014


from time import time

#inpath = "A-sample.in"
inpath = "A-large.in"
#inpath = 'A-small-attempt0.in'
outpath = "A.out"

def NoRepeat(line):
    new_line = str(line[0])
    for i in range(1, len(line)):
        if line[i] <> line[i - 1]:
            new_line = new_line + line[i]
    return new_line

def Distance(line, no_repeat):
    repeats = [0] * len(no_repeat)
    index = 0
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            repeats[index] += 1
        else:
            index += 1
    return repeats

def Game(s):
    first = NoRepeat(s[0])
    dist_set = [Distance(s[0], first)]
    for line in s[1:]:
        if NoRepeat(line) <> first:
            return None
        else:
            dist_set += [Distance(line, first)]
    count = 0
    for i in range(len(first)):
        distances = list(d[i] for d in dist_set)
        if min(distances) == max(distances):
            continue
        distances.sort()
        mid = distances[len(distances) / 2]
        for x in distances:
            count += abs(x - mid)
    return count
    

ts = time()
fin = open(inpath, 'r')

fout = open(outpath, 'w')
cases = int(fin.readline())
print "Cases:", cases
curline = 1
for n in range(1, cases+1):
    str_number = int(fin.readline())
    s = []
    for i in range(str_number):
        s += [fin.readline()[:-1]]
    answer = Game(s)
    if answer == None:
        answer = "Fegla Won"
    else:
        answer = str(answer)
    fout.write("Case #%d: %s\n" % (n, answer))

fin.close()
print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
