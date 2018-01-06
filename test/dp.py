import sys


def jumps(A, i):
    # print i
    if i == len(A) - 1:
        return 0
    elif A[i] == 0:
        return sys.maxint

    min_jump = sys.maxint
    for j in range(1, A[i] + 1):
        if i + j < len(A):
            min_jump = min(min_jump, 1 + jumps(A, i + j))
    return min_jump


def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))


def coin_change(coins, amount):
    if amount == 0:
        return 0
    if not coins:
        return sys.maxint
    if coins[0] > amount:
        return coin_change(coins[1:], amount)
    return min(coin_change(coins, amount - coins[0]) + 1, coin_change(coins[1:], amount))


print coin_change([1, 2, 5], 11)
