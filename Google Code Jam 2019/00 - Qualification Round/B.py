# Julie
# April, 6, 2019
# Qualification Round
# "You Can Go Your Own Way"


def YourOwnWay(path, n):
    if path[0] == 'S':
        prime, second = 'E', 'S'
    else:
        prime, second = 'S', 'E'
    if path[-1] == prime:
        return (prime * n) + (second * n)

    count = 1
    for i in range(2*n - 1):
        if path[i] == path[i + 1] == prime:
            return (prime * count) + (second * n) + (prime * (n - count))
        if path[i] == prime:
            count += 1

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    P = input()
    result = YourOwnWay(P, N-1)
    print("Case #%d: %s" % (case, result))

