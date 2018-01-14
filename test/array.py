import heapq
import sys
from collections import defaultdict


def plusOne(A):
    j = len(A) - 1
    while j >= 0 and A[j] == 9:
        A[j] = 0
        j -= 1

    if j != -1:
        A[j] += 1
    else:
        A = [1] + A

    while A[0] == 0:
        A.pop(0)
    return A


# print plusOne([0, 3, 7, 6, 4, 0, 5, 5, 5])



class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


def hotel_booking(arrive, depart, k):
    arrive.sort()
    depart.sort()
    i = j = 0
    while i < len(arrive) or j < len(depart):
        print i, j
        if i < len(arrive) and (j == len(depart) or arrive[i] < depart[j]):
            i += 1
            k -= 1
        elif j < len(depart) and (i == len(arrive) or depart[j] < arrive[i]):
            j += 1
            k += 1
        else:
            i += 1
            j += 1
        if k < 0:
            return False
    return k >= 0


# print hotel_booking([1, 2, 3, 4], [10, 2, 6, 14], 4)


def intersect(A, B):
    i = j = 0
    res = []

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            res.append(A[i])
            i += 1
            j += 1

    return res


def merge(A, B):
    print A
    k = len(A) + len(B) - 1
    i = len(A) - 1
    j = len(B) - 1
    while i >= 0 and j >= 0:
        if A[i] > A[j]:
            A[k] = A[i]
            i -= 1
            k -= 1
        else:
            A[k] = A[j]
            j -= 1
            k -= 1
        print A
    while i >= 0:
        A[k] = A[i]
        k -= 1
        i -= 1

    while j >= 0:
        A[k] = A[j]
        k -= 1
        j -= 1

    return A


# print merge([-4, 3], [-2, -2])


def sortColors1(A):
    low = 0
    high = len(A) - 1
    itera = 0

    while itera <= high:
        if A[itera] == 0:
            A[low], A[itera] = A[itera], A[low]
            itera += 1
            low += 1
        elif A[itera] == 1:
            itera += 1
        elif A[itera] == 2:
            A[high], A[itera] = A[itera], A[high]
            high -= 1
    return A


# print sortColors1([0, 1, 2, 0, 1, 2])

def slidingMaximum(A, k):
    queue = []
    B = []
    for i in range(k):
        while len(queue) and A[i] >= A[queue[-1]]:
            queue.pop()
        queue.append(i)

    for i in range(k, len(A)):
        B.append(A[queue[0]])
        while queue and queue[0] <= i - k:
            queue.pop(0)

        while queue and A[i] >= A[queue[-1]]:
            queue.pop()

        queue.append(i)

    B.append(A[queue[0]])
    return B


# print slidingMaximum([1, 2, 3, 1, 4, 5, 2, 3, 6], 3)

def next_greater(A):
    G = [-1] * len(A)
    stack = []
    for i in range(len(A) - 1, -1, -1):
        while stack and A[i] > stack[-1]:
            stack.pop()
        if stack:
            G[i] = stack[-1]
        stack.append(A[i])
    return G


# print next_greater([13, 7, 6, 12])

def binary_search(A, l, h, key):
    while l <= h:
        mid = (l + h) / 2
        if A[mid] == key:
            return mid
        if A[mid] > key:
            h = mid - 1
        else:
            l = mid + 1
    return -1


def lower(A, key):
    l = 0
    h = 1
    val = A[0]
    while val < key:
        l = h
        h = h * 2
        val = A[h]
    return binary_search(A, l, h, key)


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums_index = sorted(enumerate(nums), cmp=lambda i1, i2: i1[1] - i2[1])
    # print nums_index
    i = 0
    j = len(nums) - 1
    while i < j:
        print i, j, nums_index[i][1] + nums_index[j][1], target
        if nums_index[i][1] + nums_index[j][1] == target:
            return [nums_index[i][0], nums_index[j][0]]
        if nums_index[i][1] + nums_index[j][1] > target:
            j -= 1
        else:
            i += 1


# print twoSum([1, 4, 2, 3], 10)


def searchInsert(nums, target):
    l = 0
    h = len(nums) - 1
    while l <= h:
        mid = (l + h) / 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            h = mid - 1
        else:
            l = mid + 1
    return l


# print searchInsert([1, 3, 5, 6], 2)

def dominantIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    largest = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[largest]:
            if nums[i] < 2 * nums[largest]:
                return -1
            largest = i
        else:
            if nums[i] != nums[largest] and 2 * nums[i] > nums[largest]:
                print i, largest
                print "sda"
                return -1

    return largest


# print dominantIndex([0, 1, 1, 2])

def minCostClimbingStairs(cost):
    def do(cost, i):
        if i == len(cost) - 1:
            return cost[i]
        if i >= len(cost):
            return 0

        return min(do(cost, i + 1), do(cost, i + 2)) + cost[i]

    cost.append(0)
    print cost
    return do(cost, -1)


# print minCostClimbingStairs([0, 0, 0, 1])

def findMedian(A_list):
    min_heap = []
    n = len(A_list)
    m = len(A_list[0])
    for i in range(n):
        heapq.heappush(min_heap, (A_list[i].pop(0), i))

    k = (n * m) / 2 + 1

    while k:
        e, ind = heapq.heappop(min_heap)
        if A_list[ind]:
            heapq.heappush(min_heap, (A_list[ind].pop(0), ind))
        else:
            heapq.heappush(min_heap, (sys.maxint, -1))

        k -= 1
    return e

def kthSmallest(self, matrix, k):
    def do(matrix, k):
        import heapq
        min_heap = []
        for i in range(len(matrix[0])):
            heapq.heappush(min_heap, (matrix[0][i], 0, i))

        for i in range(k):
            pop = heapq.heappop(min_heap)
            if pop[1] < len(matrix) - 1:
                heapq.heappush(min_heap, (matrix[pop[1] + 1][pop[2]], pop[1] + 1, pop[2]))

        return pop

    return do(matrix, k)[0]
# print findMedian([
#     [1, 3, 5],
#     [2, 6, 9],
#     [3, 6, 9]
# ])

def threeSum(nums):
    nums.sort()
    sol = set()
    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            tmp = nums[i] + nums[j] + nums[k]
            if tmp == 0:
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                sol.add((nums[i], nums[j], nums[k]))
            if tmp > 0:
                k -= 1
            else:
                j += 1
    return list(list(x) for x in sol)


# print threeSum([0, 0, 0, 0, 0])

def fourSum(nums, target):
    Aux = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            Aux.append((nums[i] + nums[j], nums[i], nums[j]))
    Aux.sort()
    i = 0
    j = len(Aux) - 1
    sol = set()

    while i < j:
        if Aux[i][0] + Aux[j][0] > target:
            j -= 1
        elif Aux[i][0] + Aux[j][0] < target:
            i += 1
        else:
            if not (Aux[i][1] == Aux[j][1] or Aux[i][1] == Aux[j][2] or Aux[i][2] == Aux[j][1] or Aux[i][2] == Aux[j][
                2]):
                sol.add((Aux[i][1], Aux[i][2], Aux[j][1], Aux[j][2]))
            i += 1
            j -= 1
    return sol


# print fourSum([1, 0, -1, 0, -2, 2], 1)
def largestRectangleArea(height):
    height.append(0)
    stack = [0]
    r = 0
    for i in range(1, len(height)):
        while stack and height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            r = max(r, w * h)
        stack.append(i)
    return r


# print largestRectangleArea([2, 1, 5, 6, 2, 3])

def printNthElement(n):
    arr = [1] * (n + 1)
    arr[1] = 4
    arr[2] = 13
    for i in range(3, n + 1):
        if i % 2 != 0:
            arr[i] = arr[i / 2] * 10 + 4
        else:
            arr[i] = arr[(i / 2) - 1] * 10 + 13
    return arr


# print printNthElement(4)

def reductionCost(num):
    heapq.heapify(num)
    cost = 0
    while len(num) > 1:
        t1 = heapq.heappop(num)
        t2 = heapq.heappop(num)
        cost += t1 + t2
        heapq.heappush(num, t1 + t2)

    return cost


def waitingTime(tickets, p):
    time = 0
    while True:
        popped = tickets.pop(0)
        time += 1
        if popped == 1:
            if p == 0:
                return time
        else:
            tickets.append(popped - 1)
        p = p - 1 if p > 0 else len(tickets) - 1


# print waitingTime([2, 6, 3, 4, 5], 2)


def buildbridge(cities):
    cities.sort(cmp=lambda x, y: x[1] - y[1])


# cities = [[2, 6], [5, 4], [8, 1], [10, 2]]
# buildbridge(cities)

# s = ["cat", "dog", "tac", "god", "act"]
# print sorted(s, cmp=lambda x, y: 1 if ''.join(sorted(x)) > ''.join(sorted(y))else -1)
def candies():
    INF = 10 ** 9  # a number larger than all ratings
    a = [5, 10, 15, 13, 10, 4, 6, 9]
    n = 8
    # add sentinels
    a = [INF] + a + [INF]

    candies = [0] * (n + 1)
    # populate 'valleys'
    for i in xrange(1, n + 1):
        if a[i - 1] >= a[i] <= a[i + 1]:
            candies[i] = 1

    print candies
    # populate 'rises'
    for i in xrange(1, n + 1):
        if a[i - 1] < a[i] <= a[i + 1]:
            candies[i] = candies[i - 1] + 1
    print candies
    # populate 'falls'
    for i in xrange(n, 0, -1):
        if a[i - 1] >= a[i] > a[i + 1]:
            candies[i] = candies[i + 1] + 1
    print candies
    # populate 'peaks'
    for i in xrange(1, n + 1):
        if a[i - 1] < a[i] > a[i + 1]:
            candies[i] = max(candies[i - 1], candies[i + 1]) + 1

    print candies
    # print the total number of candies
    print sum(candies)
