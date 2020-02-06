# September, 3, 2009
# Qualification Round
# "Watersheds"

from time import time

#inpath = "B-sample.in"
inpath = "B-large.in"
#inpath = 'B-small-attempt0.in'
outpath = "B.out"

def Neighbours(i, j, H, W):
    neigh = [(i-1, j),(i, j-1),(i, j+1),(i+1, j)]
    for k in (3, 2, 1, 0):
        if neigh[k][0]<0 or neigh[k][0]>=H or neigh[k][1]<0 or neigh[k][1]>=W:
            del neigh[k]
    return neigh

def MapWork (H, W, region):
    drainage = {}
    for i in range(H):
        for j in range(W):
            drainage[i, j] = [True, [(i, j)]]
    for i in range(H):
        for j in range(W):
            minh = region[i, j]
            neigh = Neighbours(i, j, H, W)
            for x, y in neigh:
                if region[x, y] < minh:
                    minh = region[x, y]
                    sink = (x, y)
            if region[i, j] == minh:
                continue
            if not drainage[sink][0]:
                sink = drainage[sink][1]
            drainage[i, j][0] = False
            flow = drainage[i, j][1]
            for x in flow:
                drainage[sink][1].append(x)
                drainage[x][1] = sink
    basin = list([None]*W for i in range(H))
    curletter = ord('a')
    for i in range(H):
        for j in range(W):
            if basin[i][j] is not None:
                continue
            if drainage[i, j][0]:
                xr, yr = (i, j)
            else:
                xr, yr = drainage[i, j][1]
            for x, y in drainage[xr, yr][1]:
                basin[x][y] = chr(curletter)
            curletter += 1
    return basin

def AtlasWork(inpath, outpath):
    fin = open(inpath)
    fout = open(outpath, 'w')
    s = fin.readline()
    iternum = int(s.split()[0])
    for k in range(iternum):
        s = fin.readline()
        H, W = map(int, s.split())
        region = {}
        for i in range(H):
            s = fin.readline()
            mapline = map(int, s.split())
            for j in range(W):
                region[i, j] = mapline[j]
        fout.write('Case #%d:\n' % (k+1))
        basin = MapWork(H, W, region)
        for i in range(H):
            for j in range(W):
                fout.write('%c ' % basin[i][j])
            fout.write('\n')
    fin.close
    fout.close
    return

ts = time()
AtlasWork(inpath, outpath)
print "Time:", round(time() - ts, 4)
