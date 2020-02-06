# Julie
# April, 7, 2018
# Qualification Round
# "Trouble Sort"

def TroubleSort(V):
    V1 = sorted(V[::2])
    V2 = sorted(V[1::2])
    for i in range(len(V) // 2):
        if V1[i] > V2[i]: return i * 2
        if 2 * (i+1) < len(V) and V2[i] > V1[i + 1]: return 2*i + 1
    return "OK"

T = int(input())
for case in range(1, T + 1):
    N = input()
    V = list(map(int, input().split()))
    result = TroubleSort(V)
    print("Case #%d: %s" % (case, str(result)))

