# April, 28, 2019
# Round 1B
# "Fair Fight"


def fair_fight(C, D, K):
    count = 0
    L = 0

    while L < len(C):
        c_max = L
        d_max = L
        R = L
        while abs(C[c_max] - D[d_max]) > K:
            R += 1
            if R >= len(C): break
            if C[R] > C[c_max]: c_max = R
            if D[R] > D[d_max]: d_max = R

        L_fix = min(c_max, d_max)
        R_fix = max(c_max, d_max)

        if abs(C[c_max] - D[d_max]) > K:
            L = L + 1
            continue
        
        while abs(C[c_max] - D[d_max]) <= K:
            R += 1
            if R >= len(C): break
            if C[R] > C[c_max]: c_max = R
            if D[R] > D[d_max]: d_max = R
        
        count += (L_fix - L + 1) * (R - R_fix)
        L = L + 1

    return count


T = int(input())
for case in range(1, T + 1):
    _, K = map(int, input().split())
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))


    result = fair_fight(C, D, K)
    print("Case #%d: %s" % (case, result))

