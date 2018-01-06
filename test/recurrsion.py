def subsets(s):
    if len(s) <= 1:
        return [s, []]

    first = s[0]
    remaining_subsets = subsets(s[1:])
    more = []
    for subset in remaining_subsets:
        new_subset = list(subset)
        new_subset.append(first)
        more.append(new_subset)
    return more + remaining_subsets


def permute(s):
    if len(s) <= 1:
        return [s]

    first = s[0]
    permutations = permute(s[1:])
    more = []
    for str in permutations:
        for i in range(len(str) + 1):
            more.append(str[:i] + first + str[i:])
    return more


def paranthesis(l, r, str):
    if 0 == l and 0 == r:
        print str
    if l > 0:
        paranthesis(l - 1, r, str + '(')
    if r > 0:
        paranthesis(l, r - 1, str + ')')


def letter_phone(digit_str):
    digit_map = {0: '0', 1: '1', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
    if digit_str and len(digit_str) == 1:
        return list(digit_map[int(digit_str)])

    combinations = letter_phone(digit_str[1:])
    res = []
    for combination in combinations:
        res += [c + combination for c in digit_map[int(digit_str[0])]]

    return res


# print letter_phone("123")

def gray_code(n):
    if n == 1:
        return ['0', '1']

    codes = gray_code(n - 1)
    return ['0' + c for c in codes] + ['1' + c for c in codes[::-1]]


# print gray_code(2)


def generate_paranthesis(A, n):
    if len(A) == 2 * n:
        if isvalid(A):
            print ''.join(A)
        return
    A.append('(')
    generate_paranthesis(A, n)
    A.pop()
    A.append(')')
    generate_paranthesis(A, n)
    A.pop()


def isvalid(A):
    bal = 0
    for ch in A:
        if ch == '(':
            bal += 1
        else:
            bal -= 1
        if bal < 0:
            return False
    return bal == 0


generate_paranthesis([], 2)
