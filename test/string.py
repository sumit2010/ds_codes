from Queue import Queue
from collections import Counter, OrderedDict, defaultdict

import sys


def cmp(x, y):
    if (''.join(sorted(x))) == (''.join(sorted(y))):
        return 0
    if (''.join(sorted(x))) > (''.join(sorted(y))):
        return +1
    else:
        return -1


def sort_anagrams(strs):
    strs.sort(cmp)
    print strs


# sort_anagrams(["abc", "xyz", "bca"])

def reverse(str):
    if str == '':
        return ''
    rev = reverse(str[1:])
    return rev + str[0]


# print reverse("ab1c1")

def hash(str):
    letters = "ab0cd1ef2gh3ij4kl5mno6"
    h = 9
    for i in range(len(str)):
        h = h * 39 + letters.index(str[i])

    return h


def unhash(h):
    letters = "ab0cd1ef2gh3ij4kl5mno6"
    str = ''
    while h > 9:
        str += letters[h % 39]
        h /= 39

    return str[::-1]


# print unhash(hash("abc"))

def titletonumber(str):
    number = 0
    for ch in str:
        number = number * 26 + (ord(ch) - ord('A') + 1)
    return number


# print titletonumber("A")

# without repeat
def lengthOfLongestSubstring(str):
    visited = [-1] * 256
    visited[ord(str[0])] = 0
    cur_len = 1
    max_len = 1
    for i in range(1, len(str)):
        prev_ind = visited[ord(str[i])]

        if prev_ind == -1 or i - cur_len > prev_ind:
            cur_len += 1
        else:
            max_len = max(max_len, cur_len)
            cur_len = i - prev_ind

        visited[ord(str[i])] = i

    return max(max_len, cur_len)


def removeInvalidParentheses(str):
    def isvalid(s):
        paran_count = 0
        for ch in str:
            if ch == '(':
                paran_count += 1
            elif ch == ')':
                paran_count -= 1
            if paran_count < 0:
                return False
        return paran_count == 0

    level = Queue()
    level.put(str)
    visited_set = set()
    l = False
    while not level.empty():
        str = level.get()
        if isvalid(str):
            print str
            l = True
        if l:
            continue

        for i in range(len(str)):
            if (str[i] not in ['(', ')']):
                continue
            tmp = str[:i] + str[i + 1:]
            if tmp not in visited_set:
                level.put(tmp)
                visited_set.add(tmp)


# removeInvalidParentheses("()())()")

def paranthesis(l, r, str):
    if 0 == l and 0 == r:
        print str
    if l > 0:
        paranthesis(l - 1, r, str + '(')
    if r > 1:
        paranthesis(l, r - 1, str + ')')


def lps(str, i, j):
    if i == j:
        return str[i]
    if i + 1 == j and str[i] == str[j]:
        return str[i:j + 1]
    if str[i] == str[j]:
        s = lps(str, i + 1, j - 1)
        return str[i] + s + str[j]
    left = lps(str, i + 1, j)
    right = lps(str, i, j - 1)
    if len(left) > len(right):
        return left
    else:
        return right


# str = "GEEKSFORGEEKS"
# print lps(str, 0, len(str) - 1)

def isPal(s, i, j):
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    return i == j


def minPalPartion(str, i, j):
    if i == j:
        return 0
    if isPal(str, i, j):
        return 0
    return min((minPalPartion(str, i, k) + 1 + minPalPartion(str, k + 1, j)) for k in range(i, j))


# s = "ababbbabbababa"
# print minPalPartion(s, 0, len(s) - 1)

def subsets(l):
    if not l:
        return [[]]

    remaining = subsets(l[1:])
    print remaining
    more_subsets = []
    for rem in remaining:
        new_list = list(rem)
        new_list.append(l[0])
        more_subsets.append(new_list)
    return remaining + more_subsets


# print subsets([1, 2, 3])


def findFirstNonRepeating(str):
    d = OrderedDict()
    i = 0
    l = len(str)
    while i < l:
        ch = str[i]
        if ch in d:
            d.pop(ch)
        else:
            d[ch] = True
        print str[i], d.items()[0][0]
        i += 1


def gen(str):
    i = 0
    l = len(str)
    while i < l:
        yield str[i]
        i += 1


#
# str = "geeksforgeeksandgeeksquizfor"
# # stream = gen(str)
# findFirstNonRepeating(str)


def longestChain(words):
    def dfs(u):
        if not graph[u]:
            return 1
        return max(dfs(v) + 1 for v in graph[u])

    # visited = set()
    dictionary = set(words)
    graph = defaultdict(list)

    for word in words:
        for i in range(len(word)):
            connect = word[:i] + word[i + 1:]
            if connect in dictionary:
                graph[word].append(connect)

    print graph

    return max(dfs(word) for word in words)


# words = ["a", "b", "ba", "bca", "bda", "bdca"]
# print longestChain(words)

def letterCombinations(self, digit_str):
    digit_map = {0: '0', 1: '1', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
    if len(digit_str) == 1:
        return list(digit_map[int(digit_str)])

    combinations = self.letterCombinations(digit_str[1:])
    lettercombinations = list(digit_map[int(digit_str[0])])
    new_comp = []
    for each in lettercombinations:
        for combination in combinations:
            new_comp.append(each + combination)
    return new_comp


def minWindow(s, t):
    counter = Counter(t)
    print counter
    begin = end = 0
    count = len(t)
    d = sys.maxint
    head = 0
    while end < len(s):
        if s[end] in counter:  # in t
            counter[s[end]] -= 1
            count -= 1
            end += 1
        while count == 0:
            if end - begin < d:
                d = end - begin
                head = begin
            if counter[s[begin]] == 0:
                counter[s[begin]] += 1
                count += 1
            begin += 1

    return "" if d == sys.maxint else s[head:d]


s = "this is a test string"
t = "tist"
print minWindow(s, t)
c = Counter(t)
c['i'] -= 1
print c
