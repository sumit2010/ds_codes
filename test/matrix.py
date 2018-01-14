import collections
import sys


def coverPoints(self, X, Y):
    return sum(max(abs(X[i] - X[i - 1]), abs(Y[i] - Y[i - 1])) for i in range(1, len(X)))


def calculateMinimumHP(A, i, j):
    if i == len(A) - 1 and j == len(A[0]) - 1:
        return A[i][j]
    if i < len(A) and j < len(A[0]):
        return min(calculateMinimumHP(A, i + 1, j), calculateMinimumHP(A, i, j + 1)) + A[i][j]
    return sys.maxint


# print calculateMinimumHP([[1, 3, 2],''
#                           [4, 3, 1],
#                           [5, 6, 1]], 0, 0)


dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(matrix, i, j, str, recu_flag):
    if ((i, j)) in recu_flag:
        return False
    if len(str) == 0:
        return True
    if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]):
        if str[0] == matrix[i][j]:
            recu_flag.add((i, j))
            return any(dfs(matrix, i + d[0], j + d[1], str[1:], recu_flag) for d in dir)

    return False


# Board = [
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E']
# ]
# word = "ABCEFSADEESE"
# print any(dfs(Board, i, j, word, set()) for i in range(len(Board)) for j in range(len(Board[0])))



def kthSmallest(matrix, k):
    import heapq
    min_heap = []
    for i in range(len(matrix[0])):
        heapq.heappush(min_heap, (matrix[0][i], 0, i))

    for i in range(k):
        pop = heapq.heappop(min_heap)
        if pop[1] < len(matrix) - 1:
            heapq.heappush(min_heap, (matrix[pop[1] + 1][pop[2]], pop[1] + 1, pop[2]))

    return pop


# print kthSmallest([
#     [1, 5, 9],
#     [10, 11, 13],
#     [12, 13, 15]
# ], 8)


def shortestDistance(grid):
    if not grid or not grid[0]: return -1
    M, N, buildings = len(grid), len(grid[0]), sum(val for line in grid for val in line if val == 1)
    hit, distSum = [[0] * N for i in range(M)], [[0] * N for i in range(M)]

    def BFS(start_x, start_y):
        visited = [[False] * N for k in range(M)]
        visited[start_x][start_y], count1, queue = True, 1, collections.deque([(start_x, start_y, 0)])
        while queue:
            x, y, dist = queue.popleft()
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= i < M and 0 <= j < N and not visited[i][j]:
                    visited[i][j] = True
                    if not grid[i][j]:
                        queue.append((i, j, dist + 1))
                        hit[i][j] += 1l
                        distSum[i][j] += dist + 1
                    elif grid[i][j] == 1:
                        count1 += 1
        return count1 == buildings


def do():
    dir = [(0, 1), (-1, 1), (1, 1)]
    gold = [[1, 3, 1, 5],
            [2, 2, 4, 1],
            [5, 0, 2, 3],
            [0, 6, 1, 2]]

    def getMaxGold(gold, i, j):
        if 0 <= i < len(gold) and 0 <= j < len(gold[0]):
            return max(gold[i][j] + getMaxGold(gold, i + d[0], j + d[1]) for d in dir)
        return 0

    print max(getMaxGold(gold, i, 0) for i in range(len(gold)))

# print getMaxGold(gold, 0, 0)
