# April, 6, 2019
# Qualification Round
# Dat Bae

import math
import sys

nxt = { '0' : '1', '1' : '0' }

def expect(i, N, L):
    num = N // L
    if i < num:
        return L
    if i == num:
        return N - L * num
    return 0


def make_request(N, L):
    result = []
    symbol = '1'
    for i in range(math.ceil(N / L)):
        symbol = nxt[symbol]
        result.append(symbol * expect(i, N, L))
    return ''.join(result)


def cut_list(s, cuts):
    result = []
    pivot = 0
    for c in cuts:
        result.append(s[pivot : pivot + c])
        pivot += c
    return result


def find_bit(responce, expected, prefix, bit):
    working = len(responce[bit])
    if working == expected:
        return []

    if bit == -1:
        return [prefix] * (expected - working)

    answers = []
    template = 1 << bit
    left_work = sum(1 for r in responce[bit] if r == '0')
    right_work = working - left_work

    left_exp = expect(0, expected, template)
    right_exp = expect(1, expected, template)

    left_responce = [r[:left_work] for r in responce]
    right_responce = [r[left_work:] for r in responce]

    
    left_list = find_bit(left_responce, left_exp, prefix, bit - 1)
    right_list = find_bit(right_responce, right_exp, prefix | template, bit - 1)
    return left_list + right_list


def broken_prefixe_count(responce, N):
    count = []
    symbol = '0'
    cluster = 0
    pivot = 0
    for i in range(len(responce) + 1):
        if i < len(responce) and responce[i] == symbol:
            continue

        count.append(i - pivot)
        symbol = nxt[symbol]
        cluster += 1
        pivot = i

    if cluster < math.ceil(N / 16):
        count.append(expect(cluster + 1, N, 16))
    return count


def dat_bae():
    N, B, F = map(int, input().split())
    sys.stdout.write(make_request(N, 1) + '\n')
    sys.stdout.write(make_request(N, 2) + '\n')
    sys.stdout.write(make_request(N, 4) + '\n')
    sys.stdout.write(make_request(N, 8) + '\n')
    sys.stdout.write(make_request(N, 16) + '\n')
    sys.stdout.flush()

    responce = []
    for _ in range(5):
        responce.append(input())

    cuts = broken_prefixe_count(responce[-1], N)
    for i in range(5):
        responce[i] = cut_list(responce[i], cuts)

    result = []
    for i in range(len(cuts)):
        resp_slice = [r[i] for r in responce]
        result += find_bit(resp_slice, expect(i, N, 16), i * 16, 3)

    assert len(result) == B, (len(result), B)
    sys.stdout.write(' '.join(map(str, result)) + '\n')
    sys.stdout.flush()
    return int(input())



def main():
    T = int(input())
    for case in range(T):
        assert dat_bae() == 1


main()
