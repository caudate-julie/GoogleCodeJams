# Julie
# April, 6, 2019
# Qualification Round
# "Cryptopangrams"


def GCD(a, b):
    while (b > 0):
        a, b = min(a, b), max(a, b)
        b = b % a
    return a

def HalfDecypher(crypto, key, direction):
    uncrypt = [0] * len(crypto)
    i = 0 if direction == 1 else -1
    for c in crypto:
        uncrypt[i] = c / key
        key = c / key
        i += direction
    return uncrypt


def Decypher(crypto):
    i = 0
    while crypto[i] == crypto[i + 1]:
        i += 1
    key = GCD(crypto[i], crypto[i + 1])
    return HalfDecypher(crypto[:i+1], key, -1) + [key] + HalfDecypher(crypto[i+1:], key, 1)


def Cryptopangrams(crypto):
    uncrypt = Decypher(crypto)
    alphabet = sorted(list(set(uncrypt)))
    result = []
    for c in uncrypt:
        result.append(chr(alphabet.index(c) + 65))
    return ''.join(result)


T = int(input())
for case in range(1, T + 1):
    _ = input()
    C = list(map(int, input().split()))

    result = Cryptopangrams(C)
    print("Case #%d: %s" % (case, result))


