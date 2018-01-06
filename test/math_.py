import sys


def primes(n):
    for i in range(2, n):
        count = 0
        while n % i == 0:
            n /= i
            count += 1
        if count:
            print i, count


# print primes(18)
def ugly_numbers(n):
    ugly = [1, 1, 1]
    next = 1
    for i in range(1, n):
        print next,
        new_ugly = 2 * ugly[0], 3 * ugly[1], 5 * ugly[2]
        next = min(new_ugly)
        indx = new_ugly.index(next)
        ugly[indx] = next
        print ugly

    return next


def getNthUglyNo(n):
    ugly = [0] * n  # To store ugly numbers

    # 1 is the first ugly number
    ugly[0] = 1

    # i2, i3, i5 will indicate indices for 2,3,5 respectively
    i2 = i3 = i5 = 0

    # set initial multiple value
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    # start loop to find value from ugly[1] to ugly[n]
    for l in range(1, n):

        # choose the min value of all available multiples
        ugly[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

        # increment the value of index accordingly
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2

        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3

        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
        print ugly
    # return ugly[n] value
    return ugly[-1]


# print getNthUglyNo(7)

def reverse(x):
    sign = 1
    if x < 0:
        sign = -1
        x *= -1
    rev = 0
    while x:
        rev = rev * 10 + x % 10
        x /= 10

    print rev, sys.maxint
    return rev * sign if rev <= sys.maxint else 0


# print reverse(1534236469)

def isPower( A):
    if A <= 2:
        return 0
    for i in range(2, A):
        count = 0
        while A % i == 0:
            A /= i
            count += 1

        if count > 0:
            return 1 if A == 1 else 0

# print isPower(1024000000)