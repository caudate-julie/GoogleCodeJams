# May, 21, 2011
# Round 1B
# "PRI"
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

def PRI(teams, table):
    wins = [0]*teams
    games = [0]*teams
    wp = [0]*teams
    owp = [0]*teams
    oowp = [0]*teams
    for i in range(teams):
        wins[i] = sum(1 for j in range(teams) if table[i][j] == 1)
        games[i] = float(sum(1 for j in range(teams) if table[i][j] != '.'))
        wp[i] = wins[i] / games[i]
    for i in range(teams):
        owp[i] = sum((wins[j] - table[j][i])/(games[j] - 1)
                     for j in range(teams) if not table[i][j] == '.')/games[i]
    for i in range(teams):
        oowp[i] = sum(owp[j] for j in range(teams)
                   if not table[i][j] == '.')/games[i]
    return list((0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i])
                for i in range(teams))
    
fout = open(outpath, 'w')
cases = int(lines.pop(0))
print "Cases:", cases

for n in range(1, cases+1):
    teams = int(lines.pop(0))
    for i in range(teams):
        table.append(list(lines.pop(0))[:teams])                     
    for i in range(teams):
        for j in range(teams):
            if not table[i][j] == '.':
                table[i][j] = int(table[i][j])
    pri = PRI(teams, table)
    fout.write("Case #%d:\n" % n)
    for i in range(teams):
        fout.write("%f\n" % round(pri[i], 8))
                          

print "Done!"
fout.close()
print "Time:", round(time() - ts, 4)
