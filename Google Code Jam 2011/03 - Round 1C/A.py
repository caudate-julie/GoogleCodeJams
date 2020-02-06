# May, 22, 2011
# Round 1C
# "Square Tiles "
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

def NewPicture(picture, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if picture[i][j] != '#':
                continue
            if i == (rows - 1) or j == (columns - 1):
                return None
            if picture[i][j+1] == '.' or picture[i+1][j] == '.' or picture[i+1][j+1] == '.':
                return None
            picture[i][j] = picture[i+1][j+1] = "/"
            picture[i+1][j] = picture[i][j+1] = "\\"
    for i in range(rows):
        s = ''.join(picture[i][j] for j in range(columns))
        picture[i] = s
    return picture
    
fout = open(outpath, 'w')
cases = int(lines.pop(0))
print "Cases:", cases

for n in range(1, cases+1):
    rows, columns = map(int, lines.pop(0).split())
    picture = []
    for i in range(rows):
        picture.append(list(lines.pop(0))[:columns])
    new_picture = NewPicture(picture, rows, columns)
    if new_picture is None:
        fout.write("Case #%d:\nImpossible\n" % n)
    else:
        fout.write("Case #%d:\n" % n)
        for i in range(rows):
            fout.write("%s\n" % new_picture[i])

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
