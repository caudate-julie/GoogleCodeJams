# Julie
# 22.04.2017
# Round 1B
# "Pony Express"

from time import time
import math

def MakeMetrics(edges):
    for i in xrange(len(edges)):
        Dijkstra(edges, i)

def Dijkstra(edges, start):
    N = len(edges)
    visited = [False] * N
    distances = [float('inf')] * N
    count = 0

    distances[start] = 0
    while (count < N):
        nearest = NearestUnvisited(visited, distances)
        #print visited
        #print distances
        if (nearest == -1): break
        edges[start][nearest] = distances[nearest]
        visited[nearest] = True
        count += 1
        for endpoint in xrange(N):
            distances[endpoint] = min(distances[endpoint], distances[nearest] + edges[nearest][endpoint])

# next node under Dijkstra algorithm to be processed
def NearestUnvisited(visited, distances):
    nearest = -1
    current_min = float('inf')
    for i in xrange(len(distances)):
        if not visited[i] and (distances[i] < current_min):
            nearest = i
            current_min = distances[i]
    return nearest

def TryInterims(times):
    for i in range(len(times)):
        for j in range(len(times)):
            for interim in range(len(times)):
                times[i][j] = min(times[i][j], times[i][interim] + times[interim][j])

# find the fastest route between cities A and B given horses and distances.
def PonyExpress(horses, distances):
    N = len(distances)
    MakeMetrics(distances)
    #for x in distances: print x
    #print "\n"
    times = [[float('inf')] * N for _ in xrange(N)]
    for i in xrange(N):
        horse = horses[i]
        for j in xrange(N):
            if distances[i][j] <= horse[0]:
                times[i][j] = min(times[i][j], distances[i][j] / horse[1])
    MakeMetrics(times)
    #for x in times: print x
    #print "\n"
    return times
    
def ParseDistance(dist_string):
    dist = float(dist_string)
    return dist if dist > 0 else float('inf')

#inpath = "C-sample.in"
inpath = "C-large-practice.in"
#inpath = "simulated.in"
#inpath = "C-small-practice.in"
outpath = "C.out"

fin = open(inpath)
fout = open(outpath, 'w')

timestart = time()

# how it works:
# Dijkstra gives us shortest routes from given A to any.
# so we have shortest_routes all set to infinity at the beginning,
# and after processing A C we have the whole row defined.
T = int(fin.readline())
for case in range(1, T+1):
    N, Q = map(int, fin.readline().split())   # N is number of cities, Q is number of routes

    horses = []                               # max total distance, speed
    for i in range(N):
        horses.append(map(float, fin.readline().split()))

    distances = []                            # [i][j] - distance from i to j, -1 meaning no direct road
    for i in range(N):
        distances.append(map(ParseDistance, fin.readline().split()))

    routes = []                               # (i, j) - we need a route from i to j
    for i in range(Q):
        routes.append(map(int, fin.readline().split()))

    assert len(horses) == N
    shortest_routes = [[float('inf')] * N for _ in xrange(N)]

    fout.write("Case #%d: " % case)
    #print "Case #%d: " % case
    times = PonyExpress(horses, distances)
    for A, B in routes:
        fout.write("%.6f " % times[A - 1][B - 1])
        #print "%.6f " % times[A - 1][B - 1]
    fout.write("\n")

fin.close()
fout.close()
print "time elapsed: %.4f" % (time() - timestart)
